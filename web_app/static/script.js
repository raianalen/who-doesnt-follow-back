// =====================
// COPY
// =====================
function copiar() {
    let texto = "";
    document.querySelectorAll(".user").forEach(el => {
        texto += el.innerText + "\n";
    });

    navigator.clipboard.writeText(texto);
    alert("Copied!");
}

// =====================
// DOWNLOAD
// =====================
function descargar() {
    let texto = "";
    document.querySelectorAll(".user").forEach(el => {
        texto += el.innerText + "\n";
    });

    const blob = new Blob([texto], { type: "text/plain" });
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "not_follow_back.txt";
    a.click();

    window.URL.revokeObjectURL(url);
}

// =====================
// FILE INPUT FEEDBACK
// =====================
const followersInput = document.querySelector('input[name="followers"]');
const followingInput = document.querySelector('input[name="following"]');

if (followersInput) {
    followersInput.addEventListener("change", function () {
        const count = this.files.length;

        if (count === 1) {
            document.getElementById("followers-text").innerText = "1 file selected";
        } else if (count > 1) {
            document.getElementById("followers-text").innerText = count + " files selected";
        } else {
            document.getElementById("followers-text").innerText = "Select Followers";
        }
    });
}

if (followingInput) {
    followingInput.addEventListener("change", function () {
        if (this.files.length > 0) {
            document.getElementById("following-text").innerText = "1 file selected";
        } else {
            document.getElementById("following-text").innerText = "Select Following";
        }
    });
}

// =====================
// FORM SUBMIT + VALIDACIÓN + SPINNER
// =====================
const form = document.querySelector("form");

if (form) {
    form.addEventListener("submit", function (e) {

        const followers = document.querySelector('input[name="followers"]').files.length;
        const following = document.querySelector('input[name="following"]').files.length;

        if (followers === 0 || following === 0) {
            e.preventDefault();
            alert("Please select both followers and following files.");
            return;
        }

        // spinner
        document.getElementById("spinner").classList.remove("hidden");

        // botón
        const btn = document.getElementById("analyze-btn");
        btn.disabled = true;
        btn.innerText = "Analyzing...";
    });
}

function abrirModal() {
    document.getElementById("modal").classList.remove("hidden");
    document.body.style.overflow = "hidden";
}

function cerrarModal(e) {
    if (!e || e.target.id === "modal") {
        document.getElementById("modal").classList.add("hidden");
        document.body.style.overflow = "auto";
    }
}

function setLang(lang) {
    document.getElementById("content-en").classList.add("hidden");
    document.getElementById("content-es").classList.add("hidden");

    document.getElementById("content-" + lang).classList.remove("hidden");
}