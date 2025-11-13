
# Laporan Praktikum Minggu [5]
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
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
1. Memahami konsep proses dan urutan eksekusi proses.
2. Menghitung rata-rata
---

## Langkah Praktikum
1. Siapkan Data Proses 
2. Eksperimen 1 – FCFS (First Come First Served)
- Urutkan proses berdasarkan Arrival Time.
- Hitung nilai berikut untuk tiap proses:

Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
Turnaround Time (TAT) = WT + Burst Time

Hitung rata-rata Waiting Time dan Turnaround Time.
Buat Gantt Chart sederhana:
| P1 | P2 | P3 | P4 |
0    6    14   21   24
3. Eksperimen 2 – SJF (Shortest Job First)

- Urutkan proses berdasarkan Burst Time terpendek (dengan memperhatikan waktu kedatangan).
- Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.
  
4. Eksperimen 3 – Visualisasi Spreadsheet (Opsional)

- Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
Gunakan formula dasar penjumlahan/subtraksi.
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
![Screenshot hasil](./praktikumweek5-scheduling-fcfs-sjfscreenshots/Screenshot%202025-11-13%20132922.png)

---

## Analisis
- jelaskan makna hasil percobaan.
    Hasil percobaan menunjukkan pengaruh urutan dan lama proses terhadap performa CPU.SJF biasanya memberikan hasil terbaik dalam rata-rata waktu tunggu dan turnaround, tapi kurang adil sedangkan FCFS lebih mudah dan adil, namun kurang efisien jika ada variasi lama proses.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
    Kernel adalah pengatur utama proses di CPU sementara System call adalah cara program berkomunikasi dengan kernel.Arsitektur OS memastikan setiap lapisan bekerja sama agar proses bisa dijalankan sesuai algoritma.Hasil percobaan menunjukkan bagaimana cara kerja kernel memengaruhi efisiensi sistem.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
    Hasil percobaan FCFS dan SJF bisa berbeda di Linux dan Windows karena cara kernel kedua sistem mengatur CPU berbeda. Linux lebih efisien dan adil dalam multitasking, sedangkan Windows lebih menekankan respons cepat dan prioritas pengguna.
---

## Kesimpulan
   1. Kesimpulan FCFS adalah proses dijalankan berdasarkan urutan kedatangan. Proses yang datang lebih dulu akan dikerjakan lebih dulu, tanpa melihat lama waktu prosesnya. Akibatnya, jika ada proses yang sangat panjang di awal, proses lain harus menunggu lama (waktu tunggu besar). FCFS mudah diterapkan tetapi kurang efisien untuk sistem multitasking.
   2. SJF adalah proses yang memiliki waktu eksekusi paling singkat dijalankan lebih dulu. Algoritma ini menghasilkan waktu tunggu dan waktu selesai rata-rata yang lebih kecil dibanding FCFS, sehingga lebih efisien. Namun, proses dengan waktu eksekusi panjang bisa tertunda terus (starvation) jika banyak proses pendek yang datang.
   

---

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?
   FCFS menekankan urutan kedatangan, sedangkan SJF menekankan kecepatan proses.FCFS lebih sederhana tapi lambat, sedangkan SJF lebih efisien tapi kurang adil.

2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?
   SJF menghasilkan rata-rata waktu tunggu minimum karena selalu mengeksekusi proses dengan waktu paling singkat terlebih dahulu, sehingga proses-proses kecil cepat selesai dan tidak memperlama antrian proses lain.

3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?
   Kelemahan utama SJF di sistem interaktif adalah sulit memperkirakan lama proses dan risiko penundaan proses panjang (starvation), sehingga respons sistem bisa menjadi lambat atau tidak stabil untuk pengguna.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
  mumet 
- Bagaimana cara Anda mengatasinya?  
  nginpo

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
