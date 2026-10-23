def hitung_subtotal(harga, jumlah):
    return harga * jumlah

def hitung_diskon(subtotal):
    if subtotal >= 100000:
        return subtotal * 0.10
    else:
        return 0

def tampilkan_struk(nama_barang, subtotal, diskon): 
    total_akhir = subtotal - diskon

    print("-==== STRUK PEMBELIAN =====")
    print("Nama barang:", nama_barang) 
    print(f"Subtotal : Rp{subtotal:,.0f}")
    print(f"Diskon : Rp{diskon:,.0f}")
    print(f"Total akhir : Rp{total_akhir:,.0f}")

harga = 25000 
jumlah = -5
subtotal = hitung_subtotal(harga, jumlah)
diskon = hitung_diskon(subtotal)
tampilkan_struk("Buku", subtotal, diskon)