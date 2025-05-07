# Program Penghitung BMI (Body Mass Index)
# =======================================

print("="*50)
print("🏋️ KALKULATOR BMI (BODY MASS INDEX) 🏋️")
print("="*50)
print("Program ini akan menghitung BMI dan menentukan kategori berat badan Anda")
print("-"*50)

# Input dari pengguna
try:
    berat = float(input("Masukkan berat badan Anda (kg): "))
    tinggi = float(input("Masukkan tinggi badan Anda (m): "))
    
    # Validasi input
    if berat <= 0 or tinggi <= 0:
        print("\n❌ Error: Berat dan tinggi harus bernilai positif!")
    else:
        # Hitung BMI
        bmi = berat / (tinggi * tinggi)
        
        # Tentukan kategori BMI
        if bmi < 18.5:
            kategori = "Berat badan kurang"
            simbol = "⚠️"
            saran = "Perbanyak asupan nutrisi dan konsultasikan dengan dokter"
        elif bmi < 25:
            kategori = "Berat badan normal"
            simbol = "✅"
            saran = "Pertahankan pola makan dan aktivitas fisik yang seimbang"
        elif bmi < 30:
            kategori = "Berat badan berlebih"
            simbol = "⚠️"
            saran = "Mulai perhatikan pola makan dan tingkatkan aktivitas fisik"
        else:
            kategori = "Obesitas"
            simbol = "⛔"
            saran = "Konsultasikan dengan dokter untuk program penurunan berat badan"
        
        # Tampilkan hasil
        print("\n" + "="*50)
        print(f"📊 Hasil Perhitungan BMI 📊")
        print("-"*50)
        print(f"Berat Badan: {berat} kg")
        print(f"Tinggi Badan: {tinggi} m")
        print(f"BMI Anda: {bmi:.2f}")
        print(f"Kategori: {simbol} {kategori}")
        print(f"Saran: {saran}")
        print("="*50)
        
        # Tampilkan skala BMI sederhana
        print("\n📏 SKALA BMI:")
        print("    <18.5    18.5-24.9    25-29.9    ≥30")
        print("     ↓          ↓           ↓         ↓")
        print("  Kurang     Normal     Berlebih   Obesitas")
        
        # Visualisasi sederhana posisi BMI pada skala
        posisi = min(55, max(0, int((bmi / 40) * 55)))
        skala = " " * posisi + "▼"
        print("\n" + skala)
        print("="*55)

except ValueError:
    print("\n❌ Error: Masukkan angka yang valid untuk berat dan tinggi!")

print("\nTerima kasih telah menggunakan kalkulator BMI!")