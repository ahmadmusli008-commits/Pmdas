
# Program Konversi Waktu

# Input
detik = int(input("Jumlah detik: "))

# Proses
jam = detik // 3600
sisa = detik % 3600
menit = sisa // 60
detik_akhir = sisa % 60

# Output
print("\n===== HASIL KONVERSI WAKTU =====")
print(f"{jam} jam {menit} menit {detik_akhir} detik")
