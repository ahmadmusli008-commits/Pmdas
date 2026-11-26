
# Program Kalkulator

# Input
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

# Proses dan Output
print("\n===== HASIL KALKULATOR =====")
print("Penjumlahan :", a + b)
print("Pengurangan :", a - b)
print("Perkalian   :", a * b)

if b != 0:
    print("Pembagian   :", a / b)
    print("Bagi Bulat  :", a // b)
    print("Sisa Bagi   :", a % b)
else:
    print("Pembagian tidak bisa dilakukan dengan nol")

print("Pangkat     :", a ** b)
