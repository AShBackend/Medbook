function applyTheme(theme) {
    document.documentElement.dataset.theme = theme;
    localStorage.setItem("medbook-theme", theme);

    document.querySelectorAll(".theme-toggle").forEach(btn => {
        btn.innerHTML = theme === "dark"
            ? '<i class="bi bi-sun-fill"></i>'
            : '<i class="bi bi-moon-stars-fill"></i>';
    });
}

function initTheme() {
    const saved = localStorage.getItem("medbook-theme") || "light";
    applyTheme(saved);

    document.querySelectorAll(".theme-toggle").forEach(btn => {
        btn.addEventListener("click", () => {
            const currentTheme = document.documentElement.dataset.theme;
            applyTheme(currentTheme === "dark" ? "light" : "dark");
        });
    });
}

document.addEventListener("DOMContentLoaded", initTheme);
