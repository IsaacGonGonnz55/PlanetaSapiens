document.addEventListener("DOMContentLoaded", () => {

    const toggle = document.querySelector(".menu-toggle");
    const navLinks = document.querySelector(".nav-links");
    const navAuth = document.querySelector(".nav-auth");

    if (!toggle) return;

    toggle.addEventListener("click", (e) => {
        e.stopPropagation();

        toggle.classList.toggle("active");
        navLinks.classList.toggle("active");
        navAuth.classList.toggle("active");
    });

    // cerrar al hacer click fuera
    document.addEventListener("click", () => {
        toggle.classList.remove("active");
        navLinks.classList.remove("active");
        navAuth.classList.remove("active");
    });

    // evitar cierre interno
    navLinks.addEventListener("click", (e) => e.stopPropagation());
    navAuth.addEventListener("click", (e) => e.stopPropagation());

    // cerrar al seleccionar link
    document.querySelectorAll(".nav-links a").forEach(link => {
        link.addEventListener("click", () => {
            toggle.classList.remove("active");
            navLinks.classList.remove("active");
            navAuth.classList.remove("active");
        });
    });

});