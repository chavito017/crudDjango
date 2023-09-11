(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Enserio vas a eliminar un User');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });

})();

// / Función para ocultar automáticamente los mensajes después de un tiempo
function hideMessages() {
    const messages = document.querySelectorAll(".message-item");

    messages.forEach(message => {
        setTimeout(() => {
            message.style.display = "none";
        }, 5000); // 5000 milisegundos (5 segundos) - ajusta este valor según tus preferencias
    });
}

    // Llama a la función después de que la página se haya cargado completamente
    window.addEventListener('load', hideMessages);