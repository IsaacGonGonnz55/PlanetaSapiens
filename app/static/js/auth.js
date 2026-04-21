document.addEventListener("DOMContentLoaded", () => {
    console.log("Login cargado");
});

document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.querySelector(".toggle-password");

    toggle.addEventListener("click", () => {
        const input = document.getElementById("password");
        const icon = toggle.querySelector("i");

        if (input.type === "password") {
            input.type = "text";
            icon.classList.replace("fa-eye", "fa-eye-slash");
        } else {
            input.type = "password";
            icon.classList.replace("fa-eye-slash", "fa-eye");
        }
    });
});