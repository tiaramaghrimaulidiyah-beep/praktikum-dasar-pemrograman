harga_satuan = float(input("Masukkan harga satuan barang: "))
jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
persen_diskon = float(input("Masukkan persentase diskon (contoh: 10 untuk 10%): "))
subtotal = harga_satuan * jumlah_barang
nominal_diskon = subtotal * (persen_diskon / 100)
total_bayar = subtotal - nominal_diskon
print(f"Subtotal        : Rp {subtotal:,.2f}")
print(f"Nominal Diskon : Rp {nominal_diskon:,.2f}")
print(f"Total Bayar    : Rp {total_bayar:,.2f}")