
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
        toggleLexicoOptions(checked);
    });

    function toggleLexicoOptions(checked) {
        document.getElementById('useAdverbios').checked = checked;
        document.getElementById('useNumero').checked = checked;
        document.getElementById('useRomanos').checked = checked;
        document.getElementById('useSuperlativos').checked = checked;
        document.getElementById('useAbreviaturas').checked = checked;
    }

    document.getElementById('useSintactico').addEventListener('change', function() {
        var checked = this.checked;
        toggleSintacticoOptions(checked);
        // Esta línea también controlará la visibilidad de las opciones detalladas
        toggleOptions('optionsSintactico', !checked);
    });

    function toggleSintacticoOptions(checked) {
        document.getElementById('useComplejos').checked = checked;
        document.getElementById('useImpersonal').checked = checked;
        document.getElementById('useNominalizacion').checked = checked;
    }

    // Función auxiliar para controlar la visibilidad de las opciones
    function toggleOptions(divId, show) {
        document.getElementById(divId).style.display = show ? 'block' : 'none';
    }

    // Función auxiliar para marcar/desmarcar todas las opciones en un div
    function setAllOptions(divId, checked) {
        var checkboxes = document.getElementById(divId).getElementsByTagName('input');
        for (var i = 0; i < checkboxes.length; i++) {
            checkboxes[i].checked = checked;
        }
    }

    document.getElementById('useLexico').addEventListener('change', function() {
        var checked = this.checked;
        toggleLexicoOptions(checked);
        // Controlar la visibilidad de las opciones detalladas léxicas
        toggleOptions('optionsLexico', !checked);
    });

    function toggleLexicoOptions(checked) {
        document.getElementById('useAdverbios').checked = checked;
        document.getElementById('useNumero').checked = checked;
        document.getElementById('useRomanos').checked = checked;
        document.getElementById('useSuperlativos').checked = checked;
        document.getElementById('useAbreviaturas').checked = checked;
    }

    document.getElementById('useSintactico').addEventListener('change', function() {
        var checked = this.checked;
        toggleSintacticoOptions(checked);
        // Controlar la visibilidad de las opciones detalladas sintácticas
        toggleOptions('optionsSintactico', !checked);
    });

    function toggleSintacticoOptions(checked) {
        document.getElementById('useComplejos').checked = checked;
        document.getElementById('useImpersonal').checked = checked;
        document.getElementById('useNominalizacion').checked = checked;
    }

    // Función auxiliar para controlar la visibilidad de las opciones
    function toggleOptions(divId, show) {
        document.getElementById(divId).style.display = show ? 'block' : 'none';
    }

    // Función auxiliar para marcar/desmarcar todas las opciones en un div
    function setAllOptions(divId, checked) {
        var checkboxes = document.getElementById(divId).getElementsByTagName('input');
        for (var i = 0; i < checkboxes.length; i++) {
            checkboxes[i].checked = checked;
        }
    }


    // Función para marcar el botón seleccionado
function markSelected(button) {
    var buttons = document.querySelectorAll('.btn');

    // Iterar sobre todos los botones
    buttons.forEach(function(btn) {
        // Remover la clase 'selected-button' de todos los botones
        btn.classList.remove('selected-button');
    });

    // Agregar la clase 'selected-button' al botón seleccionado
    button.classList.add('selected-button');

    // Almacenar el valor del botón seleccionado en el almacenamiento local
    localStorage.setItem('selectedButton', button.value);
}

// Función para inicializar el estado del botón seleccionado al cargar la página
window.onload = function() {
    var selectedButtonValue = localStorage.getItem('selectedButton');
    if (selectedButtonValue) {
        var selectedButton = document.querySelector('button[value="' + selectedButtonValue + '"]');
        if (selectedButton) {
            selectedButton.classList.add('selected-button');
        }
    }
}

// Función para limpiar el área de texto
function clearTextArea() {
    document.querySelector('textarea').value = '';
}

// Escuchar eventos de cambio en los botones y marcar el botón seleccionado
document.querySelectorAll('.btn').forEach(function(button) {
    button.addEventListener('click', function() {
        markSelected(button);
    });
});

