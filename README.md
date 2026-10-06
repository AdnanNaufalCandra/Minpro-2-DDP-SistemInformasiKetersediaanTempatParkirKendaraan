# Minpro-2-DDP-SistemInformasiKetersediaanTempatParkirKendaraan

Nama : Adnan Naufal Candra

NIM : 2609116034

*------------------------------------------------*

**FLOWCHART**
-------------------
<img width="4646" height="3870" alt="minpro ddp2" src="https://github.com/user-attachments/assets/75d88fba-42a8-4cda-b690-67d55ea37863" />


**KODE PROGRAM**
------------------
<img width="1920" height="1078" alt="mini_project 2 py - ddp ni bos - Visual Studio Code 06_10_2026 18 09 59" src="https://github.com/user-attachments/assets/84496312-6c28-49f5-8550-e004ab3bc29e" />
<img width="1920" height="1078" alt="mini_project 2 py - ddp ni bos - Visual Studio Code 06_10_2026 18 10 06" src="https://github.com/user-attachments/assets/428106a8-fb29-4f35-9929-0a132da644a5" />
<img width="1920" height="1078" alt="mini_project 2 py - ddp ni bos - Visual Studio Code 06_10_2026 18 10 32" src="https://github.com/user-attachments/assets/75f77bcf-4489-43f1-a81e-1fa8020441f2" />
<img width="1920" height="1078" alt="mini_project 2 py - ddp ni bos - Visual Studio Code 06_10_2026 18 10 41" src="https://github.com/user-attachments/assets/775d14e2-3271-4475-b39d-7a8158d21860" />

**Penjelasan Kode Program**

*1. List*

data_parkir menggunakan kode list untuk menyimpan info data parkiran mulai dari kode, lantai, dan status (terisi/kosong)

*2. Dictionary*

data_akun menggunakan kode dictionary untuk menyimpan username dan password admin/user

*3. Def*

def berfungsi sebagai mengelompok kan kode berdasarkan tugas/perannya masing masing dan def juga berfungsi saat ingin memanggil tugas itu lagi agar tidak mngetik ulang kode panjang, cukup panggil nama fungsinya

*4. Kumpulan def*

- tampilkan () : untuk mencetak daftar parkir yang isinya kode, lantai dan status

- kendaraan_masuk () & kendaraan_keluar () : mengubah status "kosong" menjadi "terisi", dan juga sebaliknya

- tambah_parkir(), ubah_parkir(), hapus_parkir() : untuk mengubah apapun yang ada di list data_parkir

*5. While True menu admin/user*

saat seseorang memasukan role admin dan password admin dengan benar, maka dia akan memiliki akses untuk menu admin yang isinya tampilkan daftar data parkir, menambah tempat parkir, mengubah tempat parkir, dan menghapus tempat parkir. dan orang itu bisa keluar dari menu admin dengan pilihan ke 5. dan kalau seseorang memasukan role user dan password user dengan benar, maka dia akan memiliki akses untuk menu user

*6. Login*

sistem meminta untuk memasukan username dan password lalu sistem akan cek jika memasukan username admin password admin maka akan ke menu admin dan jika memasukan username user password user maka akan ke menu user
