print('***** Kredit Keaktifan Mahasiswa *****')
print('(Student Activities Credit)')

print('1. Menambahkan Kegiatan')
print('2. Menampilkan Jumlah Poin')
print('3. Keluar')

user = input('Silahkan masukan pilihan anda: ')
if user == 1:
    a = Input('Nama kegiatan: ')
    b = Input('Tanggal Kegiatan: ')
    print('Pilihan Kategori kegiatan:\n- PRESTASI\n - ORGANISASI\n - Kepanitiaan\n - Rekognisi\n')
    c = input('Masukan Kategori Kegiatan: ')
    if input == ORGANISASI:
        print("Kegiatan berhasil di tambahkan")
    elif input == Kepanitiaan:
        print("Kegiatan berhasil di tambahkan")
    elif input == PRESTASI:
        print("Kegiatan berhasil di tambahkan")
    elif input == Rekognisi:
        print("Kegiatan berhasil di tambahkan")
elif input == 2:
    print("Nama kegiatan                   Tanggal                      Kategori                             Poin")
    print("1.", a , b , c, )


elif input == 3:
    print("Sistem berhenti...")
