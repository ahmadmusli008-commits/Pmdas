
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
