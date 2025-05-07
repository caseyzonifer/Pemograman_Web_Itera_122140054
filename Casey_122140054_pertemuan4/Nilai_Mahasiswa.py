# Program Pengelolaan Data Nilai Mahasiswa
# ========================================

# Data mahasiswa (nama, nim, nilai_uts, nilai_uas, nilai_tugas)
mahasiswa = [
    {"nama": "Budi Santoso", "nim": "12214001", "nilai_uts": 85, "nilai_uas": 90, "nilai_tugas": 78},
    {"nama": "Anisa Rahma", "nim": "12214002", "nilai_uts": 75, "nilai_uas": 65, "nilai_tugas": 80},
    {"nama": "Dian Purnama", "nim": "12214003", "nilai_uts": 90, "nilai_uas": 85, "nilai_tugas": 95},
    {"nama": "Eko Prasetyo", "nim": "12214004", "nilai_uts": 60, "nilai_uas": 65, "nilai_tugas": 70},
    {"nama": "Fitri Handayani", "nim": "12214005", "nilai_uts": 45, "nilai_uas": 50, "nilai_tugas": 55}
]

# Menghitung nilai akhir dan menentukan grade untuk setiap mahasiswa
for mhs in mahasiswa:
    # Hitung nilai akhir: 30% UTS + 40% UAS + 30% Tugas
    nilai_akhir = (0.3 * mhs["nilai_uts"]) + (0.4 * mhs["nilai_uas"]) + (0.3 * mhs["nilai_tugas"])
    mhs["nilai_akhir"] = nilai_akhir
    
    # Tentukan grade berdasarkan nilai akhir
    if nilai_akhir >= 80:
        mhs["grade"] = "A"
        mhs["emoji"] = "🌟"
    elif nilai_akhir >= 70:
        mhs["grade"] = "B"
        mhs["emoji"] = "✨"
    elif nilai_akhir >= 60:
        mhs["grade"] = "C"
        mhs["emoji"] = "👍"
    elif nilai_akhir >= 50:
        mhs["grade"] = "D"
        mhs["emoji"] = "⚠️"
    else:
        mhs["grade"] = "E"
        mhs["emoji"] = "❌"

# Tampilkan header program
print("\n" + "="*80)
print(" "*25 + "📊 DATA NILAI MAHASISWA 📊")
print("="*80)

# Header tabel
print(f"| {'NO':^4} | {'NAMA':^20} | {'NIM':^10} | {'UTS':^5} | {'UAS':^5} | {'TUGAS':^5} | {'AKHIR':^8} | {'GRADE':^10} |")
print("-"*80)

# Isi tabel - data mahasiswa
for i, mhs in enumerate(mahasiswa, 1):
    print(f"| {i:^4} | {mhs['nama']:<20} | {mhs['nim']:^10} | {mhs['nilai_uts']:^5} | {mhs['nilai_uas']:^5} | {mhs['nilai_tugas']:^5} | {mhs['nilai_akhir']:^8.2f} | {mhs['grade']} {mhs['emoji']:^6} |")

print("-"*80)

# Mencari mahasiswa dengan nilai tertinggi dan terendah
nilai_tertinggi = max(mahasiswa, key=lambda x: x["nilai_akhir"])
nilai_terendah = min(mahasiswa, key=lambda x: x["nilai_akhir"])

# Informasi nilai tertinggi dan terendah
print("\n" + "="*80)
print(" "*25 + "📈 STATISTIK NILAI 📈")
print("="*80)
print(f"▶ Mahasiswa dengan nilai tertinggi: {nilai_tertinggi['nama']} ({nilai_tertinggi['nilai_akhir']:.2f})")
print(f"▶ Mahasiswa dengan nilai terendah: {nilai_terendah['nama']} ({nilai_terendah['nilai_akhir']:.2f})")

# Legenda grade
print("\n" + "="*80)
print(" "*30 + "📝 LEGENDA 📝")
print("="*80)
print("🌟 A (≥ 80)   : Sangat Baik")
print("✨ B (70-79)  : Baik")
print("👍 C (60-69)  : Cukup")
print("⚠️ D (50-59)  : Kurang")
print("❌ E (< 50)   : Sangat Kurang")
print("="*80)

# Informasi rumus perhitungan
print("\n" + "="*80)
print(" "*25 + "🧮 RUMUS PERHITUNGAN 🧮")
print("="*80)
print("Nilai Akhir = (30% × UTS) + (40% × UAS) + (30% × Tugas)")
print("="*80)