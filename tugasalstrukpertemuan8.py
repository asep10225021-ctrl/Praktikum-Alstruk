# =====================================================
# TUGAS PERTEMUAN 8 — IMPLEMENTASI STRUKTUR DATA
# =====================================================

print("=" * 55)
print("      IMPLEMENTASI STRUKTUR DATA — PERTEMUAN 8")
print("=" * 55)

# =====================================================
# 1. ARRAY — Menyimpan & Mengelola Sekumpulan Data
# =====================================================
print("\n📌 1. IMPLEMENTASI ARRAY")
print("-" * 40)

# Menggunakan list Python sebagai array
data_siswa = ["Andi", "Budi", "Citra", "Dedi", "Eka"]

print("Data awal:", data_siswa)
print("Jumlah data:", len(data_siswa))
print("Data indeks ke-2:", data_siswa[2])

# Menambah data
data_siswa.append("Fajar")
print("Setelah ditambah:", data_siswa)

# Menghapus data
data_siswa.remove("Budi")
print("Setelah dihapus:", data_siswa)

# Mengakses data dengan perulangan
print("Semua data:")
for i, nama in enumerate(data_siswa):
    print(f"   Indeks {i}: {nama}")

# =====================================================
# 2. LINKED LIST — Konsep Node & Pointer
# =====================================================
print("\n📌 2. IMPLEMENTASI LINKED LIST")
print("-" * 40)

# Kelas Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer ke node berikutnya

# Kelas Linked List
class LinkedList:
    def __init__(self):
        self.head = None  # Node pertama

    def tambah_di_akhir(self, data):
        node_baru = Node(data)
        if self.head is None:
            self.head = node_baru
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node_baru

    def tampilkan(self):
        temp = self.head
        hasil = ""
        while temp:
            hasil += str(temp.data) + " -> "
            temp = temp.next
        hasil += "None"
        print("Isi Linked List:", hasil)

# Penggunaan Linked List
ll = LinkedList()
ll.tambah_di_akhir(10)
ll.tambah_di_akhir(20)
ll.tambah_di_akhir(30)
ll.tambah_di_akhir(40)
ll.tampilkan()

# =====================================================
# 3. TUPLE — Data Bersifat Tetap (Immutable)
# =====================================================
print("\n📌 3. IMPLEMENTASI TUPLE")
print("-" * 40)

# Membuat tuple
data_prodi = ("TKJ", "RPL", "TKR", "MM")
print("Data Prodi:", data_prodi)
print("Jumlah elemen:", len(data_prodi))
print("Elemen ke-2:", data_prodi[1])

# Mencoba mengakses data (TIDAK BISA diubah)
print("\n⚠️ Tuple bersifat TETAP — tidak bisa diubah isinya")
print("Contoh: data_prodi[0] = 'Baru' → akan ERROR!")

# Menggunakan tuple dalam perulangan
print("Daftar Program Keahlian:")
for prodi in data_prodi:
    print(f"   - {prodi}")

print("\n" + "=" * 55)
print("✅ PROGRAM SELESAI DIJALANKAN")
print("=" * 55)