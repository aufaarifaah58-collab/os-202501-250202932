
# Laporan Praktikum Minggu [2]
Topik: Arsitektur Sistem Operasi dan Kernel

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
System Call adalah mekanisme yang digunakan program untuk meminta layanan dari sistem operasi.
Program tidak bisa langsung mengakses perangkat keras (seperti disk, printer, atau memori) karena sistem operasi harus menjaga keamanan dan kestabilan sistem. Jadi, program akan meminta bantuan sistem operasi lewat system call.

Percobaan strace ls secara langsung dan mendemokrasikan mekanisme nya, mencatat 
setiap kali program juga nelakkukan transisinya dari mode ke kernel mode

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
Gunakan Linux (Ubuntu/WSL).
Pastikan perintah stracedan mansudah terinstal.
Konfigurasikan Git 

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tai

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Screenshot%202025-10-19%20194615.png)
![Screanshot diagram](./screenshots/Screenshot%202025-10-19%20202728.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
Percobaan ini dapat mengetahui bagaimana program strace ls berjalan dengan 
sistem operasi melalui systeam call.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
Berdasarkan hasil percobaan 
Percobaan dengan strace membuktikan bagaimana sistem operasi modern memisahkan ruang pengguna dan kernel, serta bagaimana kernel menjalankan fungsinya melalui system call sebagai perantara antara program dan sumber daya perangkat keras.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)? 

Linux lebih terbuka dan langsung dalam pelacakan system call dengan strace, sedangkan Windows memerlukan tools khusus dan tracing dilakukan melalui API level yang lebih tinggi atau tersembunyi.
hasil percobaan di Linux dan Windows akan sangat berbeda, baik dari segi sistem yang dipanggil, alat yang digunakan, hingga kemudahan tracing.
---

## Kesimpulan
System call adalah elemen kunci OS yang memungkinkan interaksi aman antara aplikasi dan kernel, mencegah program pengguna merusak sistem. Mekanismenya melibatkan mode transisi yang dikontrol untuk mematikan layanan inti, dengan fokus pada efisiensi, keamanan, dan isolasi.
--- 

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?

   System call (syscall) adalah mekanisme interface yang memungkinkan aplikasi di user space untuk meminta layanan dari kernel sistem operasi. Fungsi utamanya adalah menyediakan akses terkontrol dan aman ke sumber daya hardware serta layanan OS, sambil menjaga isolasi antara aplikasi dan komponen inti sistem

2. Penawaran 4 kategori system call yang umum digunakan

   -Pengelolaan Proses (Process Management)
   -Pengelolaan Berkas (File Management)
   -Pengelolaan Perangkat (Device Management)
   -Pengelolaan Informasi (Information Maintenance)

3. Mengapa panggilan sistem tidak bisa dipanggil langsung oleh pengguna program?

   Program pengguna tidak bisa memanggil System Call secara langsung karena System Call memerlukan hak istimewa penuh (Mode Kernel) untuk mengakses sumber daya penting. Program harus melalui prosedur resmi yang terkendali ketat untuk menjaga sistem agar tetap aman dan stabil.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
belum punya laptop
- Bagaimana cara Anda mengatasinya?  
beli, tp nabung dlu hehe
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
