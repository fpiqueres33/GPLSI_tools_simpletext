from Facilitada.Lexico.Superlativos import Superlativos

class TestSuperlativos:

    @classmethod
    def setup_class(cls):
        cls.superlativos_instance = Superlativos()

    def setup_method(self):
        self.superlativos_instance = Superlativos()

    # Prueba para detectar superlativos en un texto
    def test_detectar_superlativos(self):
        input_text = "Este coche es rapidísimo. Su aceleración es velocísima"
        expected_superlatives = ["rapidísimo", "velocísima"]
        assert self.superlativos_instance.detectar_superlativos(input_text) == expected_superlatives

    # Prueba para obtener la forma base de un adjetivo superlativo
    def test_get_base_adjective(self):
        assert self.superlativos_instance.get_base_adjective("celebérrimo") == "celebre"
        assert self.superlativos_instance.get_base_adjective("tremendísimo") == "tremendo"

    # Prueba para ajustar las terminaciones "qu" en adjetivos superlativos
    def test_adjust_qu_endings(self):
        assert self.superlativos_instance.adjust_qu_endings("quos") == "cos"
        assert self.superlativos_instance.adjust_qu_endings("quas") == "cas"
        # Agregar más casos de prueba según sea necesario

    # Prueba para encontrar lemas de adjetivos superlativos
    def test_find_superlative_lemmas(self):
        input_text = "alegrísimo y velocísimo son adjetivos superlativos"
        # Llama a detectar_superlativos primero
        self.superlativos_instance.detectar_superlativos(input_text)
        expected_lemma = [("alegrísimo", "muy alegre"), ("velocísimo", "muy veloz")]
        assert self.superlativos_instance.find_superlative_lemmas(
            self.superlativos_instance.superlatives) == expected_lemma

    # Prueba para reemplazar superlativos en un texto
    def test_reemplazar_superlativos(self):
        input_text = "Miguel está contentísimo con la noticia. Es una buenísima noticia."
        expected_output = "Miguel está muy contento con la noticia. Es una muy buena noticia."
        assert self.superlativos_instance.reemplazar_superlativos(input_text) == expected_output


if __name__ == '__main__':
    pytest.main()