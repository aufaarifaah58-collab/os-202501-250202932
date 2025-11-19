
# Laporan Praktikum Minggu [6]
Topik: "Arsitektur Sistem Operasi dan Kernel"

---

## Identitas
- **Nama**  : Aufaa Rifaah
- **NIM**   : 250202932
- **Kelas** : 1IKRB

---

## Tujuan
 tujuan praktikum minggu ini.    
1. Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.
3. Membandingkan performa algoritma RR dan Priority.
4. Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori
 Pada minggu ini mahasiswa akan melakukan simulasi perhitungan manual untuk menghitung waiting time dan turnaround time, serta menganalisis efek perbedaan time quantum dan prioritas terhadap performa CPU scheduling.



---

## Langkah Praktikum
1. Siapkan Data Proses  
2. Eksperimen 1 – Round Robin (RR)
    - Gunakan time quantum (q) = 3.
    - Hitung waiting time dan turnaround time untuk tiap proses.
    - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet)
    - Catat sisa burst time tiap putaran.
3.  Eksperimen 2 – Priority Scheduling (Non-Preemptive)
    - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).
    - Lakukan perhitungan manual untuk:
    WT[i] = waktu mulai eksekusi - Arrival[i]
    TAT[i] = WT[i] + Burst[i]
    - Buat tabel perbandingan hasil RR dan Priority.
4. Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)
    - Ubah quantum menjadi 2 dan 5.
    - Amati perubahan nilai rata-rata waiting time dan turnaround time.
    - Buat tabel perbandingan efek quantum.


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
![Screenshot hasil](./praktikumweek6-scheduling-rr-priorityscreenshots/Round%20Robin.png)
[Screenshot hasil](./praktikumweek6-scheduling-rr-priorityscreenshots/Priority%20Scheduling.png)
[Screenshot hasil](./praktikumweek6-scheduling-rr-priorityscreenshots/Tabel%20Perbandingan%20Efek%20Time%20Quantum.png)


---

## Analisis
- Jelaskan makna hasil percobaan. 
  Pada algoritma Round Robin, semua proses mendapatkan giliran secara adil karena dijalankan secara bergantian. Hasil percobaan menunjukkan bahwa ukuran time quantum sangat mempengaruhi kinerja: jika terlalu kecil, proses terlalu sering berganti sehingga sistem menjadi sibuk melakukan context switching; jika terlalu besar, proses menunggu lebih lama sehingga terasa seperti FCFS. Round Robin cocok digunakan pada sistem yang membutuhkan respon cepat, seperti komputer yang digunakan banyak aplikasi secara bersamaan.Pada Priority Scheduling, proses dengan prioritas lebih tinggi dikerjakan lebih dulu. Ini membuat pekerjaan yang penting dapat selesai lebih cepat. Namun, proses dengan prioritas rendah dapat menunggu terlalu lama, bahkan bisa tidak pernah dijalankan jika selalu ada proses berprioritas tinggi yang masuk. Kondisi ini disebut starvation. Algoritma ini cocok untuk situasi di mana proses tertentu harus benar-benar diutamakan. Secara umum, Round Robin menekankan keadilan dan kecepatan respon, sedangkan Priority Scheduling menekankan pentingnya proses, tetapi dengan risiko ketidakadilan bagi proses prioritas rendah.

---

## Kesimpulan
Pada praktikum Round Robin, proses mendapatkan giliran eksekusi secara merata dan hasilnya menunjukkan bahwa ukuran time quantum sangat mempengaruhi kinerja: quantum kecil membuat sistem lebih responsif tetapi sering melakukan pergantian proses, sedangkan quantum besar membuat proses berjalan lebih lama seperti FCFS. Pada Priority Scheduling, proses dengan prioritas tinggi selalu dijalankan lebih dulu sehingga tugas penting selesai lebih cepat, namun proses berprioritas rendah bisa menunggu terlalu lama dan berpotensi mengalami starvation jika prioritas tidak dinaikkan.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling? 
   Round Robin mengutamakan keadilan waktu proses untuk semua, sedangkan Priority Scheduling mengutamakan proses berdasarkan tingkat prioritasnya. Pemilihan algoritma bergantung pada kebutuhan sistem dan karakteristik beban kerja yang dijalankan.

2. Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?
   Jika time quantum terlalu kecil, jumlah context switch akan meningkat karena proses sering di-preempt untuk memberi kesempatan pada proses lain. Hal ini menyebabkan overhead CPU yang besar dari perpindahan konteks proses, sehingga performa sistem menurun walaupun responsif terhadap proses pendek meningkat. Sementara jika time quantum terlalu besar, Round Robin cenderung berperilaku seperti algoritma First Come First Served (FCFS) yang berarti proses yang panjang dapat mendominasi CPU, dan respons time untuk proses lain menjadi tinggi. Ini mengurangi fairness dan membuat sistem kurang responsif.

3. Mengapa algoritma Priority dapat menyebabkan starvation?
   Algoritma Priority dapat menyebabkan starvation karena proses dengan prioritas rendah dapat terus-menerus tertunda eksekusinya jika selalu ada proses dengan prioritas lebih tinggi yang datang atau sudah ada dalam antrian. Dengan kata lain, proses berprioritas rendah bisa menunggu tanpa batas waktu untuk mendapatkan CPU karena sumber daya selalu dialokasikan ke proses prioritas tinggi terlebih dahulu. Hal ini terjadi karena sistem penjadwalan tidak adil bagi proses prioritas rendah yang akhirnya "terlupakan" dalam antrian.​Starvation ini umumnya muncul pada algoritma priority scheduling yang bersifat preemptive, di mana proses berprioritas tinggi bisa memaksa keluar proses yang sedang berjalan dengan prioritas rendah. Solusi yang biasa digunakan untuk mengatasi masalah starvation adalah teknik aging, yaitu secara bertahap meningkatkan prioritas proses yang sudah lama menunggu dalam antrian sehingga akhirnya proses tersebut mendapatkan kesempatan eksekusi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
  pengen beli tiramisu matcha
- Bagaimana cara Anda mengatasinya?  
  pergi ke bandung karna beli nya di sana tapi jauh

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
