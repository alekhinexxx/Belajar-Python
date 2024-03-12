def program_hitung():
    while True:
        try:
            angka1 = input("Masukan Angka 1 : ")
            angka2 = input("Masukan Angka 2 : ")
            jmlh = int(angka1) + int(angka2)
            print("Hasilnya adalah : ", jmlh)
        except ValueError:
            print("Input bukan angka. Silakan masukkan angka yang valid.")
            continue

        mengulang_program = input("Apakah Anda ingin mengulang perhitungan? (y/n): ").lower()
        if mengulang_program != 'y':
            print("Terima kasih telah menggunakan program kami.")
            break  # Keluar dari loop, menghentikan program.

# Memanggil fungsi untuk menjalankan program
program_hitung()
