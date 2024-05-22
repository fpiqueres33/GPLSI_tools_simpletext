import torch
from transformers import BertTokenizer, BertForMaskedLM
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
#nltk.download('punkt')
from nltk.corpus import wordnet as wn


class Disambiguator:
    def __init__(self, model_name='dccuchile/bert-base-spanish-wwm-cased'):
        # Cargar el tokenizer y el modelo de BERT
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForMaskedLM.from_pretrained(model_name)
        self.model.eval()

    def tokenize_text(self, text):
        return self.tokenizer.encode_plus(text, return_tensors='pt')

    def get_synonyms(self, word, context_sentence, top_k=5):
        # Tokenizar el texto con el token [MASK] en lugar de la palabra objetivo
        tokens = self.tokenizer.tokenize(context_sentence)
        word_pieces = self.tokenizer.tokenize(word)

        if self.tokenizer.unk_token in word_pieces:
            print(f"La palabra '{word}' es desconocida para el modelo.")
            return [self.tokenizer.unk_token], [1.0]

        mask_index = tokens.index(word_pieces[0]) if word_pieces[0] in tokens else -1
        if mask_index == -1:
            raise ValueError("Palabra no encontrada en la oración")

        tokens[mask_index] = self.tokenizer.mask_token
        masked_sentence = self.tokenizer.convert_tokens_to_string(tokens)
        inputs = self.tokenize_text(masked_sentence)

        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = outputs.logits

        masked_index = torch.where(inputs['input_ids'][0] == self.tokenizer.mask_token_id)[0].item()
        probs = torch.nn.functional.softmax(predictions[0, masked_index], dim=-1)
        top_k_weights, top_k_indices = torch.topk(probs, top_k, sorted=True)

        synonyms = [self.tokenizer.decode([idx]).strip() for idx in top_k_indices]
        weights = [weight.item() for weight in top_k_weights]
        return synonyms, weights

    def wordnet_synonyms(self, word):
        # Obtener sinónimos de WordNet
        synsets = wn.synsets(word, lang='spa')
        synonyms = set()
        for synset in synsets:
            for lemma in synset.lemmas('spa'):
                synonyms.add(lemma.name())
        return list(synonyms)

    def disambiguate(self, word, context_sentence):
        synonyms_in_context, weights = self.get_synonyms(word, context_sentence)

        # Filtrar la palabra objetivo de los sinónimos en contexto
        synonyms_in_context_filtered = [syn for syn in synonyms_in_context if syn != word]
        weights_filtered = [weights[i] for i, syn in enumerate(synonyms_in_context) if syn != word]

        # Obtener sinónimos de WordNet y filtrar la palabra objetivo
        wordnet_synonyms = [syn for syn in self.wordnet_synonyms(word) if syn != word]
        relevant_synonyms = [
            (syn, f"{weights_filtered[synonyms_in_context_filtered.index(syn)] * 100:.2f}%")
            for syn in wordnet_synonyms if syn in synonyms_in_context_filtered
        ]

        if not relevant_synonyms and synonyms_in_context_filtered:
            relevant_synonyms.append((synonyms_in_context_filtered[0], f"{weights_filtered[0] * 100:.2f}%"))

        return {
            'Palabras de contexto': synonyms_in_context_filtered
            #'Pesos (%)': weights_filtered,
            #'Wordnet sinónimos': wordnet_synonyms,
            #'Sinónimo relevante:': relevant_synonyms
        }