# Minpro_2_DDP
 
Nama : Jihan Shafira Rahmah  
NIM : 2509116073  
Kelas : B'25  

Flowchart :
<img width="1077" height="604" alt="Screenshot 2025-09-28 194919" src="https://github.com/user-attachments/assets/0ef0165c-20a4-47e6-9dbc-88e766cac4b2" />  

Output dan Penjelasan Alur Program:  
- Pengguna sebagai mahasiswa  
<img width="583" height="131" alt="Screenshot 2025-09-28 204549" src="https://github.com/user-attachments/assets/3d9d1a0f-e1ea-4ef6-84f0-8999c90df400" />
Pada saat aplikasi dijalankan, pengguna akan diminta untuk memasukkan username dan password sebagai langkah awal untuk mengakses sistem. Jika pengguna memasukkan kombinasi username dan password yang benar, maka akan muncul pesan "Login berhasil" dan pengguna dapat melanjutkan ke menu utama. 

- menu mahasiswa  
<img width="179" height="82" alt="menu mahasiswa (1)" src="https://github.com/user-attachments/assets/7856f5b9-d314-4e10-9745-005dde045bfb" />

Setelah login, pengguna akan melihat Menu Mahasiswa yang terdiri dari empat opsi: Tambah Kegiatan (1), Hapus Kegiatan (2), Lihat Semua Kegiatan (3), dan Keluar (4).  
- Jika pengguna memilih menu 1:
<img width="227" height="132" alt="pil 1 (1)" src="https://github.com/user-attachments/assets/7c9f08aa-374e-4c2a-a92a-344d4f37b464" />

Jika pengguna memilih opsi Tambah Kegiatan (menu 1), sistem akan meminta input berupa judul kegiatan, tanggal kegiatan, dan lokasi kegiatan. Setelah data diisi lengkap, sistem akan menampilkan pesan “Kegiatan berhasil ditambahkan”  
- Jika pengguna memilih menu  2:
<img width="699" height="219" alt="Screenshot 2025-09-28 210250" src="https://github.com/user-attachments/assets/ece4a737-1703-4421-a64b-7d1687dbe6d7" />
Pada menu Hapus Kegiatan (2), pengguna memasukkan judul kegiatan yang ingin dihapus. Jika ditemukan, sistem akan menghapusnya dan menampilkan pesan “Kegiatan berhasil dihapus.”

- Jika pengguna memilih menu 3:
<img width="600" height="162" alt="Screenshot 2025-09-28 210741" src="https://github.com/user-attachments/assets/a02f8b08-3c4f-4c17-8d7b-b895a91e7d7b" />
Sistem akan menampilkan semua kegiatan.

- Jika pengguna memilih menu 4:
  
<img width="361" height="198" alt="Screenshot 2025-09-28 210957" src="https://github.com/user-attachments/assets/bfab9b0f-ee01-4a11-8953-6881b29c845f" />  

Pengguna akan keluar dari menu mahasiswa  

- Menu Admin
<img width="319" height="152" alt="Screenshot 2025-09-28 211305" src="https://github.com/user-attachments/assets/26d28cd5-0867-4538-a1d3-0e2f049ca578" />

Menu Admin menyediakan tiga pilihan: Lihat Data Kegiatan (1), Lihat Akun Pengguna (2), dan Keluar (3). Pengguna memilih angka sesuai menu.  
- Jika pengguna memilih menu 1:
<img width="597" height="220" alt="Screenshot 2025-09-28 211527" src="https://github.com/user-attachments/assets/5b5db579-224c-4ada-a2fb-6ec6d64c0b0f" />
Sistem akan menampilkan data kegiatan sosial.

- Jika pengguna memilih menu 2:
<img width="744" height="124" alt="Screenshot 2025-09-28 211720" src="https://github.com/user-attachments/assets/9d5c4b4b-83e9-40b4-a8b6-5923781228b1" />
Sistem akan menampilkan Data akun pengguna yang terdaftar.

- Jika pengguna memilih menu 3:

<img width="310" height="57" alt="Screenshot 2025-09-28 211923" src="https://github.com/user-attachments/assets/44636c09-c3c5-4ace-8dff-b6ca3bfa2095" />

Pengguna akan keluar dari menu admin.  

Error Handling:  
- KeyboardInterrupt
<img width="409" height="54" alt="Screenshot 2025-09-28 212343" src="https://github.com/user-attachments/assets/458d3a66-c342-4680-b74f-8948f4dfcd66" />

Jika pengguna menekan CTRL+C saat input username, sistem menampilkan pesan “Harap tidak menekan tombol CTRL+C.” sebagai peringatan agar proses login tidak terganggu  

- Exception as e
<img width="396" height="68" alt="Screenshot 2025-09-28 213102" src="https://github.com/user-attachments/assets/de42f387-824d-4dc3-82b8-ef7f537a4d19" />

Jika pengguna menekan CTRL+Z saat memasukkan username, sistem akan menampilkan pesan "Harap tidak menekan tombol CTRL+Z." sebagai peringatan untuk mencegah penghentian program secara paksa
 
  






  


