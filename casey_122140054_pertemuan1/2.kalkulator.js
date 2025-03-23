// Fungsi untuk menyapa pengguna
function sapaNama(nama) {
    return `Halo, ${nama}! Selamat belajar JavaScript 😊`;
}

// Event handler untuk tombol sapa
document.getElementById("sapa-button").addEventListener("click", function() {
    const nama = document.getElementById("nama-input").value;
    if (nama.trim() === "") {
        document.getElementById("sapa-output").innerHTML = 
            `<p class="error">Silakan masukkan nama Anda terlebih dahulu!</p>`;
    } else {
        const pesan = sapaNama(nama);
        document.getElementById("sapa-output").innerHTML = 
            `<p class="success">${pesan}</p>`;
    }
});

// Fungsi untuk kalkulator dengan operasi tambahan
function hitungKalkulator(angka1, angka2, operasi) {
    let hasil = 0;
    switch (operasi) {
        case "tambah":
            hasil = angka1 + angka2;
            break;
        case "kurang":
            hasil = angka1 - angka2;
            break;
        case "kali":
            hasil = angka1 * angka2;
            break;
        case "bagi":
            if (angka2 === 0) {
                return "Error: Pembagian dengan nol tidak diperbolehkan";
            }
            hasil = angka1 / angka2;
            break;
        case "pangkat":
            hasil = Math.pow(angka1, angka2);
            break;
        case "akar":
            if (angka1 < 0) {
                return "Error: Tidak bisa mengambil akar kuadrat dari bilangan negatif";
            }
            hasil = Math.sqrt(angka1);
            break;
        case "modulus":
            if (angka2 === 0) {
                return "Error: Modulus dengan nol tidak diperbolehkan";
            }
            hasil = angka1 % angka2;
            break;
        default:
            return "Operasi tidak valid";
    }
    return hasil;
}

// Event handler untuk tombol operasi matematika
document.getElementById("btn-tambah").addEventListener("click", function() {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    
    if (isNaN(angka1) || isNaN(angka2)) {
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p class="error">Masukkan angka yang valid!</p>`;
    } else {
        const hasil = hitungKalkulator(angka1, angka2, "tambah");
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p class="success">Hasil: ${angka1} + ${angka2} = ${hasil}</p>`;
    }
});

document.getElementById("btn-kurang").addEventListener("click", function() {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    
    if (isNaN(angka1) || isNaN(angka2)) {
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p class="error">Masukkan angka yang valid!</p>`;
    } else {
        const hasil = hitungKalkulator(angka1, angka2, "kurang");
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p class="success">Hasil: ${angka1} - ${angka2} = ${hasil}</p>`;
    }
});

document.getElementById("btn-kali").addEventListener("click", function() {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    
    if (isNaN(angka1) || isNaN(angka2)) {
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p class="error">Masukkan angka yang valid!</p>`;
    } else {
        const hasil = hitungKalkulator(angka1, angka2, "kali");
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p class="success">Hasil: ${angka1} × ${angka2} = ${hasil}</p>`;
    }
});

document.getElementById("btn-bagi").addEventListener("click", function() {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    
    if (isNaN(angka1) || isNaN(angka2)) {
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p class="error">Masukkan angka yang valid!</p>`;
    } else {
        const hasil = hitungKalkulator(angka1, angka2, "bagi");
        if (typeof hasil === "string" && hasil.startsWith("Error")) {
            document.getElementById("hasil-kalkulator").innerHTML = 
                `<p class="error">${hasil}</p>`;
        } else {
            document.getElementById("hasil-kalkulator").innerHTML = 
                `<p class="success">Hasil: ${angka1} ÷ ${angka2} = ${hasil}</p>`;
        }
    }
});

// Event handler untuk operasi pangkat
document.getElementById("btn-pangkat").addEventListener("click", function() {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    
    if (isNaN(angka1) || isNaN(angka2)) {
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p class="error">Masukkan angka yang valid!</p>`;
    } else {
        const hasil = hitungKalkulator(angka1, angka2, "pangkat");
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p class="success">Hasil: ${angka1} ^ ${angka2} = ${hasil}</p>`;
    }
});

// Event handler untuk operasi akar kuadrat
document.getElementById("btn-akar").addEventListener("click", function() {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    
    if (isNaN(angka1)) {
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p class="error">Masukkan angka yang valid!</p>`;
    } else {
        const hasil = hitungKalkulator(angka1, 0, "akar");
        if (typeof hasil === "string" && hasil.startsWith("Error")) {
            document.getElementById("hasil-kalkulator").innerHTML = 
                `<p class="error">${hasil}</p>`;
        } else {
            document.getElementById("hasil-kalkulator").innerHTML = 
                `<p class="success">Hasil: √${angka1} = ${hasil}</p>`;
        }
    }
});

// Event handler untuk operasi modulus
document.getElementById("btn-modulus").addEventListener("click", function() {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    
    if (isNaN(angka1) || isNaN(angka2)) {
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p class="error">Masukkan angka yang valid!</p>`;
    } else {
        const hasil = hitungKalkulator(angka1, angka2, "modulus");
        if (typeof hasil === "string" && hasil.startsWith("Error")) {
            document.getElementById("hasil-kalkulator").innerHTML = 
                `<p class="error">${hasil}</p>`;
        } else {
            document.getElementById("hasil-kalkulator").innerHTML = 
                `<p class="success">Hasil: ${angka1} % ${angka2} = ${hasil}</p>`;
        }
    }
});