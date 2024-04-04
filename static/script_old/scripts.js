
    function downloadText() {
        var content = document.querySelector('textarea').value;
        var url = '/download?content=' + encodeURIComponent(content);
        window.location.href = url;
    }

     // Función para limpiar la textarea
    function clearTextArea() {
    document.querySelector('textarea').value = '';
    }

    document.getElementById('useLexico').addEventListener('change', function() {
    var checked = this.checked;
    console.log("useLexico checked:", checked); // Imprime el estado actual de 'useLexico'

    toggleOptions('optionsLexico', !checked);
    setAllOptions('optionsLexico', checked);

    // Aquí imprimes el estado antes de cambiarlo manualmente
    console.log("Estado inicial de usePalabrasLargas:", document.getElementById('usePalabrasLargas').checked);
    console.log("Estado inicial de usePalabrasDificiles:", document.getElementById('usePalabrasDificiles').checked);

    if (!checked) {
        document.getElementById('usePalabrasLargas').checked = false;
        document.getElementById('usePalabrasDificiles').checked = false;
    }

    // Aquí imprimes el estado después de intentar cambiarlo
    console.log("Estado final de usePalabrasLargas:", document.getElementById('usePalabrasLargas').checked);
    console.log("Estado final de usePalabrasDificiles:", document.getElementById('usePalabrasDificiles').checked);
});

    document.getElementById('useSintactico').addEventListener('change', function() {
        var checked = this.checked;
        toggleOptions('optionsSintactico', !checked);
        // Si la opción principal está seleccionada, se marcan también todas las subopciones.
        setAllOptions('optionsSintactico', checked);
    });

    function toggleOptions(divId, show) {
    document.getElementById(divId).style.display = show ? 'block' : 'none';
}

function setAllOptions(divId, checked) {
    let checkboxes = document.querySelectorAll('#' + divId + ' .form-check-input');
    checkboxes.forEach(function(checkbox) {
        checkbox.checked = checked;
    });
}

    // Escuchar tipo de botón marcado para cambiar color de marco
function changeBorder(value) {
    var textarea = document.getElementById('resultText');
    if (value === 'simplify') {
        textarea.style.borderColor = 'darkblue';
    }
}

function resetBorder() {
    var textarea = document.getElementById('resultText');
    textarea.style.borderColor = ''; // Esto restablecerá el color del borde al valor predeterminado
}

