
# Program Kasir Sederhana

# Input
nama = input("Nama barang: ")
harga = int(input("Harga satuan: "))
jumlah = int(input("Jumlah beli: "))
persen = float(input("Diskon (%): "))

# Proses
total = harga * jumlah
diskon = total * persen / 100
bayar = total - diskon

# Output
print("\n===== STRUK PEMBELIAN =====")
print(f"Nama Barang : {nama}")
print(f"Jumlah Beli : {jumlah}")
print(f"Total       : Rp{total:,.0f}")
print(f"Diskon      : Rp{diskon:,.0f}")
print(f"Bayar       : Rp{bayar:,.0f}")

# Program Konversi Suhu

# Input
celsius = float(input("Masukkan suhu Celsius: "))

# Proses
fahrenheit = celsius * 9 / 5 + 32
reamur = celsius * 4 / 5
kelvin = celsius + 273.15

# Output
print("\n===== HASIL KONVERSI SUHU =====")
print(f"Celsius    : {celsius} C")
print(f"Fahrenheit : {fahrenheit} F")
print(f"Reamur     : {reamur} R")
print(f"Kelvin     : {kelvin} K")


 