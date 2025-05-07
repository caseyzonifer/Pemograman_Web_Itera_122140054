// Mengambil referensi form
const form = document.getElementById('myForm');

// Mengambil referensi input
const namaInput = document.getElementById('nama');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');

// Mengambil referensi pesan error
const namaError = document.getElementById('namaError');
const emailError = document.getElementById('emailError');
const passwordError = document.getElementById('passwordError');

// Mengambil referensi pesan sukses
const successMessage = document.getElementById('successMessage');

// Validasi nama
function validateNama(nama) {
    // Kriteria: Nama harus lebih dari 3 karakter
    if (nama.length <= 3) {
        namaError.style.display = 'block';
        return false;
    } else {
        namaError.style.display = 'none';
        return true;
    }
}

// Validasi email
function validateEmail(email) {
    // Kriteria: Email harus valid menggunakan regex
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        emailError.style.display = 'block';
        return false;
    } else {
        emailError.style.display = 'none';
        return true;
    }
}

// Validasi password
function validatePassword(password) {
    // Kriteria: Password harus minimal 8 karakter
    if (password.length < 8) {
        passwordError.style.display = 'block';
        return false;
    } else {
        passwordError.style.display = 'none';
        return true;
    }
}

// Fungsi validasi form secara keseluruhan
function validateForm() {
    // Mendapatkan nilai input
    const nama = namaInput.value.trim();
    const email = emailInput.value.trim();
    const password = passwordInput.value;
    
    // Melakukan validasi untuk setiap input
    const isNamaValid = validateNama(nama);
    const isEmailValid = validateEmail(email);
    const isPasswordValid = validatePassword(password);
    
    // Mengembalikan true jika semua validasi sukses
    return isNamaValid && isEmailValid && isPasswordValid;
}

// Event listener untuk validasi real-time pada input nama
namaInput.addEventListener('input', function() {
    validateNama(this.value.trim());
});

// Event listener untuk validasi real-time pada input email
emailInput.addEventListener('input', function() {
    validateEmail(this.value.trim());
});

// Event listener untuk validasi real-time pada input password
passwordInput.addEventListener('input', function() {
    validatePassword(this.value);
});

// Event listener untuk validasi saat form dikirim
form.addEventListener('submit', function(event) {
    // Mencegah form dikirim secara default
    event.preventDefault();
    
    // Validasi form
    const isValid = validateForm();
    
    // Jika valid, tampilkan pesan sukses
    if (isValid) {
        successMessage.style.display = 'block';
        
        // Optional: Reset form setelah valid
        // form.reset();
        
        // Optional: Sembunyikan pesan sukses setelah 3 detik
        setTimeout(function() {
            successMessage.style.display = 'none';
        }, 3000);
    } else {
        successMessage.style.display = 'none';
    }
});