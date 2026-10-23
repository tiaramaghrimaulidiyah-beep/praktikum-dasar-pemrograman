# Program kalkulator sederhana
print("=== Kalkulator Sederhana ===")
angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))
if operator == "+":
 hasil = angka1 + angka2
elif operator == "-":
 hasil = angka1 - angka2
elif operator == "*":
 hasil = angka1 * angka2
elif operator == "/":
 hasil = angka1 / angka2
else:
 hasil = "Operator tidak dikenali"
print("Hasil:", hasil)