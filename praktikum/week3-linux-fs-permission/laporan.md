
# Laporan Praktikum Minggu [3]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Aufaa Rifaah 
- **NIM**   : 250202932
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Pada minggu ini mahasiswa akan mempelajari tentang cara kerja operasis sistem (OS).
Dengan menggunakan chown dan chmod. Mahasiswa juga akan menganalisis perbedaan kedua nya
---


## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
  Hasil percobaan chmod menunjukkan bagaimana sistem operasi Linux mengontrol izin akses terhadap file dan direktori.
Dengan mengubah permission, pengguna atau administrator dapat mengatur tingkat keamanan dan membatasi siapa yang dapat melakukan tindakan tertentu terhadap file. Sedangkan Hasil percobaan chown menunjukkan bahwa sistem Linux mengizinkan pengalihan hak kepemilikan file untuk mengatur tanggung jawab dan keamanan.Perubahan kepemilikan ini penting agar hanya pengguna tertentu yang berwenang dapat mengubah, membaca, atau mengeksekusi file sesuai kebutuhan sistem.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS). 
  Dari hasil percobaan chown dan chmod, dapat disimpulkan bahwa perubahan kepemilikan dan hak akses file merupakan implementasi langsung dari konsep fungsi kernel, system call, dan arsitektur sistem operasi.Kernel bertugas mengatur dan melindungi file system melalui system call (chown() dan chmod()), sementara arsitektur OS memisahkan ruang pengguna dan kernel untuk menjaga keamanan serta stabilitas sistem. demikian, percobaan ini menunjukkan bagaimana teori manajemen file, keamanan, dan komunikasi antara user–kernel bekerja secara nyata di sistem Linux.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
  Hasil perintah chown dan chmod di Linux menunjukkan perubahan langsung pada kepemilikan dan izin file melalui mekanisme POSIX permission (rwx) yang sederhana dan efisien. Sedangkan di Windows, hasil serupa diatur menggunakan ACL (Access Control List) yang lebih kompleks dan fleksibel, dengan pengaturan melalui GUI atau perintah seperti icacls dan takeown. Perbedaan ini mencerminkan perbedaan arsitektur kernel dan sistem keamanan antara Linux (berbasis POSIX) dan Windows (berbasis NT Security Model).

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

1. Perintah chown berhasil mengubah kepemilikan file atau direktori.
2. Perintah chmod berhasil mengubah hak akses (permission) file.
---

## Quiz
1. Apa fungsi dari perintah chmod?
   Perintah chmod digunakan untuk mengatur hak akses file atau direktori di Linux. Dengan chmod, administrator dapat mengontrol tingkat akses pengguna terhadap sumber daya sistem, sehingga menjaga keamanan dan integritas sistem operasi.

2. Apa arti dari kode permission rwxr-xr--?
   Kode rwxr-xr-- adalah representasi hak akses (permission) pada sebuah file atau direktori di sistem Linux/Unix.

3. Jelaskan perbedaan antara chown dan chmod.
   Chown untuk mengatur siapa pemilik file/direktori sedangkan Chmod itu untuk mengatur apa yang bisa dilakukan oleh pemilik, grup, dan pengguna lain terhadap file/direktori

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
  blm punya laptop
- Bagaimana cara Anda mengatasinya? 
  beli bntr lg

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
