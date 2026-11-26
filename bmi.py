
# Program Menghitung BMI

# Input
berat = float(input("Berat badan (kg): "))
tinggi = float(input("Tinggi badan (cm): "))

# Proses
bmi = berat / (tinggi / 100) ** 2

# Output
print("\n===== HASIL PERHITUNGAN BMI =====")
print(f"Berat badan : {berat} kg")
print(f"Tinggi badan: {tinggi} cm")
print(f"BMI kamu    : {bmi:.2f}")
