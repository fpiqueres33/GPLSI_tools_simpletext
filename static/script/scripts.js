
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
        toggleOptions('optionsLexico', !checked);
        // Si la opción principal está seleccionada, se marcan también todas las subopciones.
        setAllOptions('optionsLexico', checked);
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
        var checkboxes = document.getElementById(divId).getElementsByTagName('input');
        for (var i = 0; i < checkboxes.length; i++) {
            checkboxes[i].checked = checked;
        }
    }

