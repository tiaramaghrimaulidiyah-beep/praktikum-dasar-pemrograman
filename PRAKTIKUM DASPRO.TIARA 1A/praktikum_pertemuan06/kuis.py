bank_soal = [
    ["Ibu kota Indonesia?", "Bandung", "Jakarta", "Surabaya", "Medan", "B"],
    ["2 + 2 * 3 = ?", "12", "8", "10", "6", "B"],
    ["Tipe data teks disebut?", "int", "float", "str", "bool", "C"],
]

skor = 0

for nomor, soal in enumerate(bank_soal):
    teks, opsi_a, opsi_b, opsi_c, opsi_d, kunci = soal
    print(f"\nSoal {nomor + 1}: {teks}")
    print(f"A. {opsi_a}    B. {opsi_b}    C. {opsi_c}    D. {opsi_d}")
    
    jawaban = input("Jawaban Anda (A/B/C/D): ").strip().upper()
    
    if jawaban == kunci:
        print("Benar!")
        skor += 1
    else:
        print(f"Salah! Kunci jawaban yang benar adalah {kunci}")

print(f"jumlah soal: {len(bank_soal)}")
print(f"jawaban benar:{skor}")
print(f"Skor akhir anda: {skor} dari {len(bank_soal)} soal.")