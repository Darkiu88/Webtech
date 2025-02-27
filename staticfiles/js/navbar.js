document.addEventListener("DOMContentLoaded", function() {
    setTimeout(() => {
        fetch("/navbar/")
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            let container = document.getElementById("navbar-container");
            if (container) {
                container.innerHTML = data;
            } else {
                console.error("No se encontró el elemento navbar-container.");
            }
        })
        .catch(error => console.error("Error cargando navbar:", error));
    }, 100);  // Espera 100ms antes de ejecutar
});
