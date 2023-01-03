print('***** Kredit Keaktifan Mahasiswa *****')
print('(Student Activities Credit)')
while True:
    pilihan = input('1. Menambahkan Kegiatan\n2. Menampilkan Jumlah Poin\n3. Keluar\n Silahkan masukan pilihan anda: ')
    if pilihan in ('1','2,','3','4'):
        if pilihan == '1':
            a = input(str('Nama kegiatan: '))
            b = input(str('Tanggal Kegiatan: '))
            print('Pilihan Kategori kegiatan:\n- PRESTASI\n - ORGANISASI\n - Kepanitiaan\n - Rekognisi\n')
            c = input(str('Masukan Kategori Kegiatan: '))
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