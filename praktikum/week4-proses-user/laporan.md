
# Laporan Praktikum Minggu [4]
Topik: "Arsitektur Sistem Operasi dan Kernel"

---

## Identitas
- **Nama**  : Aufaa Rifaah  
- **NIM**   : 250202932
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Mahasiswa pada minggu ini akan mempelajari tentang identitas user,monitoring proses, dan control proses.
Eksperimen ini akan menunjukan bagaimana cara linux mengelola,mengendalikan dan menganalisis perintah
yang di berikan oleh pengguna.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan. 
  1.Setup Environment
  Gunakan Linux (Ubuntu/WSL).
  Pastikan Anda sudah login sebagai user non-root. 

  2.Jalankan Identitas User
  3.Monitoring proses
  4.Control proses

2. Perintah yang dijalankan.  
   - whoami
   - id
   - groups
   - sudo adduser praktikan
   - sudo passwd praktikan
   - ps aux | head -10
   - top -n 1
   - sleep 1000 &
   - ps aux | grep sleep
   - kill <PID>
   - pstree -p | head -20
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
![Screenshot hasil](./praktikumweek4-proses-userscreenshotstop.png/Screenshot%202025-11-10%20184822.png)
![Screenshot hasil](./praktikumweek4-proses-userscreenshotstop.png/Screenshot%202025-11-10%20184952.png)
![Screenshot hasil](./praktikumweek4-proses-userscreenshotstop.png/Screenshot%202025-11-10%20185108.png)
![Screenshot hasil](./praktikumweek4-proses-userscreenshotstop.png/Screenshot%202025-11-11%20085946.png)
---

## Analisis
- Jelaskan makna hasil percobaan.  
  Eksierimen ini menunjukan bagaimana Linux bekerja untuk mengelola identitas pengguna (user) dan proses sistem. pengguna dapat dikenali melalui UID, GID, dan grup yang menentukan hak akses. Proses sistem dapat di monitor, dikendalikan, dan dianalisis melalui perintah seprti ps, top, kill, dan pstree. Dengan meemahami struktur proses dan hak pengguna, kita dapat megelola sistem secara efesien dan aman.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
  Hasil dari perintah ps, top, dan kill menunjukkan implementasi nyata dari teori kernel dan system call dalam arsitektur sistem operasi. Ketiga perintah tersebut bekerja di ruang pengguna dan berinteraksi dengan kernel melalui system call untuk mengakses, menampilkan, dan mengontrol proses yang sedang berjalan.

- Apa perbedaan hasi di lingkungan OS berbeda (Linux vs Windows)?  
  Pada sistem Linux, perintah ps, top, dan kill berinteraksi langsung dengan kernel melalui system call POSIX untuk membaca, memantau, dan mengontrol proses. Sedangkan pada Windows, fungsi serupa dijalankan melalui Task Manager, tasklist, atau taskkill, yang berkomunikasi dengan kernel menggunakan Windows API. Perbedaan ini mencerminkan perbedaan arsitektur kernel: Linux menggunakan model monolitik yang transparan dengan /proc, sementara Windows menggunakan kernel hibrida dengan lapisan API yang lebih terabstraksi.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Hierarki prosess menunjukan proses sistem yang di kendalikan oleh systemd dengan proses induk.
2. Proses sistem dapat di monitor, dikendalikan, dan dianalisis melalui perintah seperti ps, top, kill dan pstree.
3. Eksperimen ini menunjukan bagaimana linux bekerja untuk mengelola identitas pengguna dan proses sistem
---

## Quiz
1. Apa fungsi dari proses init atau systemd dalam sistem Linux?
   Proses systemd berfungsi sebagai proses pertama (PID 1) yang menginisialisasi sistem, menjalankan layanan utama, serta menjadi induk dari seluruh proses lain dalam sistem Linux.

2. Apa perbedaan antara kill dan killall?
   kill menghentikan proses berdasarkan PID,
sedangkan killall menghentikan proses berdasarkan nama program

3. Mengapa user root memiliki hak istimewa di sistem Linux?

   Karena User root memiliki hak istimewa karena bertanggung jawab atas pengelolaan penuh sistem operasi, termasuk pengaturan file sistem, manajemen pengguna, dan layanan penting. Hak ini dibatasi untuk menjaga keamanan dan stabilitas sistem agar tidak disalahgunakan oleh pengguna biasa.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
- belum punya laptop pak
- Bagaimana cara Anda mengatasinya?  
- beli ini lagi otw laptop nya

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
