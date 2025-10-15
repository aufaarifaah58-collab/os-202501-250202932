
#Laporan Praktikum Minggu 1
Topik: "Arsitektur Sistem Operasi dan Kernel"

---
## Identitas
- **Nama**  : Aufaa Rifaah 
- **NIM**   : 250202932
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  

> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Pada minggu ini mahasiswa akan mempelajari tentang sistem opearasi seperti bagaimana cara OS bekerja, interaksi antar user, karnel, aplikasi dan hardware bekerja.

---

## Langkah Praktikum
1. - Pastikan telah menginstal Linux (Ubuntu/WSL)
   - Pastikan Git telah di konfigurasi
   
   git config --global user.name "Nama Anda"
   git config --global user.email "email@contoh.com"

2. Ekperimen dasar yang di jalankan pada terminal

uname -a
whoami
lsmod | head
dmesg | head

3. Membuat Diagram Arsitektur

- Buat diagram yang menghubungan antara User → System Call → Kernel →   hardware.
- Gunakan draw.io atau Mermaid.
  Simpan hasilnya di:
  
  praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png

4. Penulisan laporan

- Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam laporan.md.
- Tambahkan screenshot hasil terminal ke folder screenshots/.

5. Commit & push

git add .
git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
git push origin main

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
![Screenshot hasil](./screenshots/linux%20-1.png)

---

## Analisis
- Jelaskan makna hasil percobaan.

uname -a Perintah ini digunakan untuk mencetak semua informasi sistem (kernel). uname adalah singkatan dari "Unix name". -a adalah opsi untuk "all"

whoami Perintah ini digunakan untuk mencetak nama pengguna yang saat ini Anda gunakan (ID pengguna yang efektif). 

lsmod | head Perintah ini digunakan untuk menampilkan daftar modul kernel yang saat ini dimuat, tetapi hanya menampilkan beberapa baris pertama

(pipa/pipe) mengarahkan output dari perintah di sebelah kirinya (lsmod) sebagai input untuk perintah di sebelah kanannya (head)

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  

System call adalah cara utama untuk mengakses fungsi kernel dari aplikasi, sehingga bergantung pada desain arsitektur OS. Misalnya, di monolithic kernel, system call lebih cepat karena semuanya terintegrasi.
Secara keseluruhan, arsitektur OS menentukan bagaimana fungsi kernel dan system call diimplementasikan, yang memengaruhi performa dan keamanan sistem.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)? 

Linux ideal untuk lingkungan IIoT yang membutuhkan efisiensi dan keamanan tinggi, seperti di edge devices, sementara Windows lebih cocok untuk aplikasi komersial yang memerlukan ekosistem lengkap. 

---

## Kesimpulan
Sistem operasi adalah perangkat lunak dasar yang berfungsi sebagai penghubung antara pengguna, aplikasi, dan hardware. OS bertanggung jawab atas pengelolaan sumber daya seperti memori, prosesor, penyimpanan, dan perangkat input/output, sehingga memastikan efisiensi, keamanan, dan stabilitas sistem. Contohnya termasuk Windows, Linux, dan macOS, yang menyediakan interface pengguna (seperti GUI) dan mengatur eksekusi program.

Kernel, sebagai inti atau "jantung" dari sistem operasi, memainkan peran krusial dalam menangani operasi tingkat rendah. sedangkan
System call adalah mekanisme penting yang menghubungkan program aplikasi (di ruang pengguna) dengan kernel (di ruang kernel)
---

## Quiz
1. Sebutkan 3 fungsi utama sistem operasi  
   **Manajemen proses, Menejemen memori, Manajemen perengkat**  

2. Jelaskan perbedaan antara kernel mode dan user mode.

   **Karnel mode memiliki akses penuh ke sumber daya sistem dan hardware yang di gunakan pada sistem operasi inti. Sedangkan user mode memiliki akses terbatas yang di gunakan pada aplikasi biasa**  

3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.

   **Contoh OS dengan arsitektur monolithic: Linux, BSD, Solaris, DOS. Contoh OS dengan arsitektur microkernel: QNX, Minix, Mach (seperti pada GNU/Hurd dan macOS).**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Membuat 500 kata
- Bagaimana cara Anda mengatasinya?  
Search dan membuat kata sendiri
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
