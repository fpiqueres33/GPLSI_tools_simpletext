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
    document.getElementById('usePalabrasLargas').checked = checked;
    document.getElementById('usePalabrasDificiles').checked = checked;
    document.getElementById('useNominalizacion').checked = checked;
}

// Función para cambiar las opciones sintácticas
function toggleSintacticoOptions(checked) {
    document.getElementById('useComplejos').checked = checked;
    document.getElementById('useImpersonal').checked = checked;

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
    // Restaurar el estado de las casillas de verificación y opciones
    var checkboxStates = JSON.parse(localStorage.getItem('checkboxStates'));
    var optionsDisplay = JSON.parse(localStorage.getItem('optionsDisplay'));

    if (checkboxStates) {
        for (var id in checkboxStates) {
            var checkbox = document.getElementById(id);
            if (checkbox) {
                checkbox.checked = checkboxStates[id];
            }
        }
    }

    if (optionsDisplay) {
        document.getElementById('optionsLexico').style.display = optionsDisplay['optionsLexico'];
        document.getElementById('optionsSintactico').style.display = optionsDisplay['optionsSintactico'];
    }
};


// Agregar evento de clic al botón Dislexia
document.getElementById('botonDislexia').addEventListener('click', function() {
    // Marcar todas las opciones de léxico y sintáctico
    toggleLexicoOptions(true);
    toggleSintacticoOptions(true);
    // Asegurarse de que las opciones de Léxico y Sintáctico se muestren
    toggleOptions('optionsLexico', true);
    toggleOptions('optionsSintactico', true);
    // Desmarcar el botón Trastorno si está marcado
    document.getElementById('botonTrastorno').checked = false;
});

// Agregar evento de clic al botón Trastorno
document.getElementById('botonTrastorno').addEventListener('click', function() {
    // Desmarcar todas las opciones primero
    toggleLexicoOptions(false);
    toggleSintacticoOptions(false);
    // Marcar solo la opción de Palabras Largas y mostrar las opciones
    document.getElementById('usePalabrasLargas').checked = true;
    toggleOptions('optionsLexico', true);
    toggleOptions('optionsSintactico', true);
    // Desmarcar el botón Dislexia si está marcado
    document.getElementById('botonDislexia').checked = false;
});

function saveCurrentState() {
    // Guardar el estado de las casillas de verificación
    var checkboxes = document.querySelectorAll('.form-check-input');
    var checkboxStates = {};
    checkboxes.forEach(function (checkbox) {
        checkboxStates[checkbox.id] = checkbox.checked;
    });
    localStorage.setItem('checkboxStates', JSON.stringify(checkboxStates));

    // Guardar el estado de visibilidad de las opciones
    var optionsDisplay = {
        'optionsLexico': document.getElementById('optionsLexico').style.display,
        'optionsSintactico': document.getElementById('optionsSintactico').style.display
    };
    localStorage.setItem('optionsDisplay', JSON.stringify(optionsDisplay));
}

// Agregar el guardado de estado al botón de Lectura Facilitada
document.querySelector('button[value="simplify"]').addEventListener('click', saveCurrentState);