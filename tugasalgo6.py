# Program Penentuan Nilai Akhir Mahasiswa
print("=" * 50)
print("      PROGRAM PENENTUAN NILAI AKHIR")
print("=" * 50)

# Input data
nama = input("Masukkan Nama Mahasiswa : ")
nim = input("Masukkan NIM            : ")
skor = float(input("Masukkan Nilai Akhir    : "))

# Validasi input
if skor < 0 or skor > 100:
    print("\n❌ Error: Nilai harus berada di antara 0 - 100")
else:
    # Proses penentuan nilai & status (menggunakan struktur percabangan)
    if skor >= 85:
        huruf = "A"
        status = "Lulus dengan predikat Sangat Baik ✅"
    elif skor >= 75:
        huruf = "B"
        status = "Lulus dengan predikat Baik ✅"
    elif skor >= 60:
        huruf = "C"
        status = "Lulus dengan predikat Cukup ✅"
    elif skor >= 50:
        huruf = "D"
        status = "Belum Lulus - Silakan ikuti Remedial ⚠️"
    else:
        huruf = "E"
        status = "Belum Lulus ❌"
    
    # Menampilkan hasil
    print("\n" + "-" * 50)
    print(f"Nama Mahasiswa : {nama}")
    print(f"NIM            : {nim}")
    print(f"Skor Akhir     : {skor:.1f}")
    print(f"Nilai Huruf    : {huruf}")
    print(f"Status         : {status}")
    print("-" * 50)

print("\nTerima Kasih!")