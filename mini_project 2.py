from prettytable import PrettyTable

data_parkir = [["A1", "lantai 1", "kosong"], ["A2", "lantai 1", "terisi"], ["A3", "lantai 1", "terisi"], ["A4", "lantai 1", "terisi"], ["A5", "lantai 1", "kosong"],
["B1", "lantai 2", "terisi"], ["B2", "lantai 2", "kosong"], ["B3", "lantai 2", "terisi"], ["B4", "lantai 2", "kosong"], ["B5", "lantai 2", "terisi"]]

data_akun = {"admin": {"password": "admin123", "role": "admin"},
"user": {"password": "user123", "role": "user"}}

def tampilkan () :
    print ("Daftar semua tempat parkir")
    if data_parkir == [] :
        print ("belum ada data tempat parkir")
    else :
        tabel = PrettyTable()
        tabel.field_names = ["kode", "lokasi", "status"]

        for data in data_parkir :
            tabel.add_row ([data[0], data[1], data[2]])
        print (tabel)

def kendaraan_masuk () :
    tanya = input ("selamat datang, apakah anda mau parkir di dalam? (y/n) :")

    if tanya == "y" :
        print ("tempat parkir yang kosong ada di :")
        ada_kosong = False

        for data in data_parkir :
            if data [2] == "kosong" :
                print ("-", data [0], "(" + data [1] + ")")
                ada_kosong = True

        if ada_kosong :
            pilih_tempat = input ("pilih kode parkir (contoh : B4) :")
            ditemukan = False

            for data in data_parkir :
                if data [0] == pilih_tempat and data [2] == "kosong" :
                    data [2] = "terisi"
                    ditemukan = True
                    print ("selamat datang, silahkan masuk :) kendaraan di arahkan ke  " + pilih_tempat)
            if not ditemukan :
                print ("gagal, anda salah memasukan kode")
        else :
            print ("maaf, tempat parkir sudah penuh")

    elif tanya == "n" :
        print ("baiklah, terimakasih dan hati hati di jalan")
    else :
        print ("pilihan tidak tersedia.")

def kendaraan_keluar () :
    keluar = input ("masukan kode parkir kendaraan yang mau keluar (contoh : A1) :")
    ditemukan = False

    for data in data_parkir :
        if data [0] == keluar and data [2] == "terisi" :
            data [2] = "kosong"
            ditemukan = True
            print ("terimakasih, hati hati di jalan")

    if not ditemukan :
        print ("gagal, kode salah atau tempatnya memang kosong")

def tambah_parkir () :
    print ("menambah tempat parkir baru")
    kode = input ("masukan kode parkir (contoh : A6) :")
    lantai = input ("masukan lantai parkiran (lantai 1 atau lantai 2) :")

    sudah_ada = False
    for data in data_parkir :
        if data [0] == kode :
            sudah_ada = True

    if kode == "" :
        print ("gagal, kode parkir tidak boleh kosong")
    elif sudah_ada :
        print ("gagal, kode parkir sudah ada")
    elif lantai != "lantai 1" and lantai != "lantai 2" :
        print ("gagal, lantai harus berupa 'lantai 1' atau 'lantai 2'")
    else : 
        data_parkir.append ([kode, lantai, "kosong"])
        print ("tempat parkir berhasil ditambahkan")

def ubah_parkir () :
    print ("mengubah data tempat parkir")
    tampilkan ()
    kode = input ("masukan kode parkir yang mau diubah :")
    lantai_baru = input ("masukan lantai baru (contoh : 1) :")
    status_baru = input ("masukan status baru (kosong/terisi) :")
    ditemukan = False

    if not lantai_baru :
        print ("gagal, lantai harus berupa angka")
    elif status_baru != "kosong" and status_baru != "terisi" :
        print ("gagal, status harus kosong atau terisi")
    else :
        for data in data_parkir :
            if data [0] == kode :
                data [1] = "lantai " + lantai_baru
                data [2] = status_baru
                ditemukan = True
                print ("berhasil, data tempat parkir " + kode + " berhasil diubah")

        if not ditemukan :
            print ("gagal, kode parkir tidak ditemukan")

def hapus_parkir () :
    print ("menghapus data tempat parkir")
    tampilkan ()
    hapus = input ("masukan kode parkir yang mau dihapus :")
    ditemukan = False

    for data in data_parkir :
        if data [0] == hapus :
            data_parkir.remove (data)
            ditemukan = True
            print ("berhasil, tempat parkir " + hapus + " dihapus dari daftar")
            break

    if not ditemukan :
        print ("gagal, kode parkir tidak ditemukan")

def menu_admin () :
    while True :
        print ("MENU ADMIN")
        print ("1. tampilkan daftar seluruh tempat parkir")
        print ("2. tambah tempat parkir baru")
        print ("3. ubah data tempat parkir")
        print ("4. hapus tempat parkir")
        print ("5. keluar dari menu admin")

        pilihan = input ("masukan pilihan anda (1-5) :")
        if pilihan == "1" :
            tampilkan ()
        elif pilihan == "2" :
            tambah_parkir ()
        elif pilihan == "3" :
            ubah_parkir ()
        elif pilihan == "4" :
            hapus_parkir ()
        elif pilihan == "5" :
            print ("berhasil keluar dari menu admin")
            break
        else :
            print ("gagal, pilihan tidak tersedia")

def menu_user () :
    while True :
        print ("MENU USER")
        print ("1. tampilkan daftar seluruh tempat parkir")
        print ("2. kendaraan masuk")
        print ("3. kendaraan keluar")
        print ("4. keluar dari menu user")

        pilihan = input ("masukan pilihan anda (1-4) :")
        if pilihan == "1" :
            tampilkan ()
        elif pilihan == "2" :
            kendaraan_masuk ()
        elif pilihan == "3" :
            kendaraan_keluar ()
        elif pilihan == "4" :
            print ("berhasil keluar dari menu user")
            break
        else :
            print ("gagal, pilihan tidak tersedia")

while True :
    print ("selamat datang di sistem parkir")
    print ("1. login sebagai admin / user")
    print ("2. keluar program")

    pilihan = input ("masukan pilihan anda (1/2) :")
    if pilihan == "1" :
        username = input ("masukan username :")
        password = input ("masukan password :")
        if username in data_akun and data_akun [username] ["password"] == password :
            print ("login berhasil, selamat datang " + username)
            role = data_akun [username] ["role"]

            if role == "admin" :
                menu_admin ()
            elif role == "user" :
                menu_user ()
        else:
            print ("username atau password anda salah")

    elif pilihan == "2" :
        print ("program parkir dimatikan")
        break

    else :
        print ("gagal, pilihan tidak tersedia")