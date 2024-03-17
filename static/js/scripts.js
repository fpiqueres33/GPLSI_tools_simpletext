// Función para limpiar el área de texto
function clearTextArea() {
    document.querySelector('textarea').value = '';
}

// Función para marcar el botón seleccionado
function markSelected(button) {
    var buttons = document.querySelectorAll('.btn');

    // Iterar sobre todos los botones
    buttons.forEach(function (btn) {
        // Remover la clase 'selected-button' de todos los botones
        btn.classList.remove('selected-button');
    });

    // Agregar la clase 'selected-button' al botón seleccionado
    button.classList.add('selected-button');

    // Almacenar el valor del botón seleccionado en el almacenamiento local
    localStorage.setItem('selectedButton', button.value);
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

// Función para aplicar el estilo de borde
function changeBorder(value) {
    var textarea = document.getElementById('resultText');
    if (value === 'simplify') {
        textarea.style.borderColor = 'darkblue';
        localStorage.setItem('borderStyleApplied', 'true');
    }
}

// Función para restablecer el estilo de borde
function resetBorder() {
    var textarea = document.getElementById('resultText');
    textarea.style.borderColor = ''; // Restablece el color del borde al predeterminado
}

// Función para preparar el cambio de borde
function prepareBorderChange() {
    // Esta función ahora solo prepara el cambio de estilo
    // El envío del formulario se maneja de manera predeterminada
    window.addEventListener('submit', function() {
        changeBorder('simplify');
    });
}

// Función para manejar la descarga de texto
function downloadText() {
    var content = document.querySelector('textarea').value;
    var url = '/download?content=' + encodeURIComponent(content);
    window.location.href = url;
}

// Función para cambiar las opciones léxicas
function toggleLexicoOptions(checked) {
    document.getElementById('useAdverbios').checked = checked;
    document.getElementById('useNumero').checked = checked;
    document.getElementById('useRomanos').checked = checked;
    document.getElementById('useSuperlativos').checked = checked;
    document.getElementById('useAbreviaturas').checked = checked;
    document.getElementById('useAnglicismos').checked = checked;
}

// Función para cambiar las opciones sintácticas
function toggleSintacticoOptions(checked) {
    document.getElementById('useComplejos').checked = checked;
    document.getElementById('useImpersonal').checked = checked;
    document.getElementById('useNominalizacion').checked = checked;
}

// Event listeners

// Escuchar eventos de cambio en los botones y marcar el botón seleccionado
document.querySelectorAll('.btn').forEach(function (button) {
    button.addEventListener('click', function () {
        markSelected(button);
    });
});

// Escuchar cambios en el checkbox de uso léxico
document.getElementById('useLexico').addEventListener('change', function () {
    var checked = this.checked;
    toggleLexicoOptions(checked);
    // Controlar la visibilidad de las opciones detalladas léxicas
    toggleOptions('optionsLexico', !checked);
});

// Escuchar cambios en el checkbox de uso sintáctico
document.getElementById('useSintactico').addEventListener('change', function () {
    var checked = this.checked;
    toggleSintacticoOptions(checked);
    // Controlar la visibilidad de las opciones detalladas sintácticas
    toggleOptions('optionsSintactico', !checked);
});

// Al cargar la página
window.onload = function() {
    // Aplicar el estilo del borde si fue almacenado en localStorage
    var borderStyleApplied = localStorage.getItem('borderStyleApplied');
    if (borderStyleApplied === 'true') {
        var textarea = document.getElementById('resultText');
        textarea.style.borderColor = 'darkblue';
    }

    // Marcar el botón seleccionado si su valor fue almacenado en localStorage
    var selectedButtonValue = localStorage.getItem('selectedButton');
    if (selectedButtonValue) {
        var selectedButton = document.querySelector('button[value="' + selectedButtonValue + '"]');
        if (selectedButton) {
            selectedButton.classList.add('selected-button');
        }
    }
};

