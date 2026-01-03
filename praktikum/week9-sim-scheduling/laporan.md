
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan C

---

## Identitas
- **Nama**  : Aufaa Rifaah  
- **NIM**   : 250202932
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
1.Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
2.Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
3.Menyajikan output simulasi dalam bentuk tabel atau grafik.
4.Menjelaskan hasil simulasi secara tertulis.
5.Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
Penjadwalan CPU adalah mekanisme sistem operasi untuk mengatur urutan proses yang akan dijalankan oleh prosesor. Karena CPU tidak dapat menjalankan semua proses secara bersamaan, diperlukan algoritma penjadwalan agar penggunaan CPU menjadi efisien. First Come First Served (FCFS) menjalankan proses berdasarkan urutan kedatangan, sehingga mudah diterapkan tetapi dapat menyebabkan waktu tunggu lama jika proses awal memiliki waktu eksekusi panjang. Shortest Job First (SJF) menjalankan proses dengan waktu eksekusi paling singkat terlebih dahulu sehingga dapat meminimalkan rata-rata waktu tunggu, namun membutuhkan informasi waktu eksekusi proses. Simulasi sederhana FCFS dan SJF digunakan untuk memahami cara kerja, perbedaan hasil, serta kelebihan dan kekurangan kedua algoritma tersebut.

---

## Langkah Praktikum
1. Menyiapkan Dataset

2. Implementasi Algoritma
Program harus:
- Menghitung waiting time dan turnaround time.
- Mendukung minimal 1 algoritma (FCFS atau SJF non-preemptive).
- Menampilkan hasil dalam tabel.

3. Eksekusi & Validasi
- jalankan program menggunakan dataset uji.
- Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.
- Simpan hasil eksekusi (screenshot).

4. Analisis
- Jelaskan alur program.
- Bandingkan hasil simulasi dengan perhitungan manual.
- Jelaskan kelebihan dan keterbatasan simulasi.
---

## Kode / Perintah

```python
# Data proses: (Process, Arrival Time, Burst Time)
processes = [
    ("P1", 0, 6),
    ("P2", 1, 8),
    ("P3", 2, 7),
    ("P4", 3, 3)
]

current_time = 0
result = []

for process, arrival, burst in processes:
    # Jika CPU menganggur
    if current_time < arrival:
        current_time = arrival

    waiting_time = current_time - arrival
    turnaround_time = waiting_time + burst

    result.append((process, waiting_time, turnaround_time))
    current_time += burst

# Menampilkan hasil
print("Process | Waiting Time | Turnaround Time")
for r in result:
    print(f"{r[0]}      | {r[1]}           | {r[2]}")

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/code%20week%209.png)
![Screenshot hasil](./screenshots/hasil%20week%209.png)




---

## Analisis
  Makna Hasil Percobaan

Hasil percobaan simulasi penjadwalan CPU menunjukkan bagaimana proses dieksekusi berdasarkan aturan algoritma yang digunakan. Pada algoritma FCFS, proses dijalankan sesuai urutan kedatangan sehingga proses yang datang lebih awal akan menunggu lebih lama jika proses sebelumnya memiliki burst time besar. Hal ini menjelaskan mengapa waktu tunggu dan turnaround time bisa menjadi tinggi pada kondisi tertentu. Hasil ini sesuai dengan teori bahwa algoritma sederhana belum tentu efisien untuk semua kondisi beban kerja.

Hubungan dengan Teori Sistem Operasi

Dalam teori sistem operasi, penjadwalan CPU merupakan bagian dari fungsi kernel, khususnya dalam manajemen proses. Kernel bertugas memilih proses yang siap dijalankan dan mengalokasikan CPU. Proses pemilihan ini dilakukan melalui system call, misalnya saat proses berpindah dari status ready ke running. Arsitektur sistem operasi memungkinkan kernel bekerja sebagai pengendali utama yang mengatur eksekusi proses, sementara simulasi yang dilakukan merepresentasikan cara kerja kernel tersebut dalam bentuk yang lebih sederhana.

Perbedaan Hasil pada Linux dan Windows

Perbedaan hasil antara lingkungan Linux dan Windows umumnya tidak terletak pada konsep dasar penjadwalan, tetapi pada implementasinya. Linux menggunakan penjadwalan yang lebih fleksibel dan dinamis sehingga respons sistem cenderung lebih baik untuk banyak proses. Windows juga memiliki scheduler sendiri yang dioptimalkan untuk sistem desktop dan interaktif. Oleh karena itu, meskipun simulasi FCFS memberikan hasil yang sama secara teori, hasil nyata di Linux dan Windows dapat berbeda karena perbedaan kebijakan scheduler, manajemen thread, dan prioritas proses.

---

## Kesimpulan
 hasil praktikum simulasi penjadwalan CPU menggunakan algoritma FCFS, dapat disimpulkan bahwa algoritma ini mudah diimplementasikan karena hanya menjalankan proses berdasarkan urutan kedatangan. Hasil simulasi menunjukkan bahwa proses dengan waktu eksekusi yang panjang dapat menyebabkan proses lain menunggu lebih lama, sehingga rata-rata waktu tunggu menjadi cukup besar. Melalui simulasi ini, dapat dipahami bahwa meskipun FCFS sederhana dan adil dalam urutan, algoritma ini kurang efisien untuk sistem dengan banyak proses dan variasi waktu eksekusi.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling? 
   Simulasi diperlukan untuk menguji algoritma *scheduling* karena memungkinkan pengujian dilakukan tanpa mengganggu sistem operasi yang sebenarnya. Dengan simulasi, perilaku algoritma dapat diamati secara terkontrol, seperti urutan eksekusi proses dan waktu tunggu. Selain itu, simulasi memudahkan perbandingan antar algoritma dalam kondisi yang sama sehingga hasilnya lebih mudah dianalisis dan dipahami.

2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
   Perbedaan hasil antara simulasi dan perhitungan manual pada dataset besar terletak pada keakuratan, efisiensi, dan potensi kesalahan. Pada dataset besar, perhitungan manual sangat sulit dilakukan karena membutuhkan banyak langkah dan waktu, sehingga risiko kesalahan hitung menjadi tinggi. Sebaliknya, simulasi mampu memproses data dalam jumlah besar secara cepat dan konsisten, sehingga hasil yang diperoleh lebih akurat dan stabil. Selain itu, simulasi memungkinkan pengolahan metrik seperti waktu tunggu rata-rata dan turnaround time secara otomatis, yang pada perhitungan manual sering kali disederhanakan atau tidak lengkap karena keterbatasan waktu dan kompleksitas.

3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan
   Algoritma FCFS (First Come First Served) lebih mudah diimplementasikan dibandingkan SJF (Shortest Job First). FCFS hanya membutuhkan urutan kedatangan proses tanpa perhitungan tambahan, sehingga logikanya sederhana dan mudah diprogram. Sementara itu, SJF memerlukan proses pemilihan berdasarkan waktu eksekusi terpendek, sehingga membutuhkan perhitungan dan pengurutan tambahan yang membuat implementasinya lebih kompleks.

---

## Refleksi Diri
- Apa bagian yang paling menantang minggu ini?
  nabung  
- Bagaimana cara Anda mengatasinya?  
  sabar

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
