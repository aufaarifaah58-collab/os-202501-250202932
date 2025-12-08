
# Laporan Praktikum Minggu [7]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Aufaa Rifaah (250202932) Dokumentasi
              Azid Mirza Maulana (250202933) Analisis
              Rafid Raihan Yuda Permana (250202962) Ketua dan Implementasi          
- **NIM**   : 
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Mengidentifikasi empat kondisi penyebab kebuntuan (mutual exclusion, hold and wait, no preemption, circuklar wait).
2. Menjelaskan mekanisme sinkronisasi menggunakan semaphore atau monitor.
3. Menganalisis dan memberikan solusi untuk kasus kebuntuan.
4. Berkolaborasi dalam waktu untuk menyusun laporan analisis.
5. menyajikan hasil studi kasus secara sistematis.

---

## Dasar Teori
- Sinkronisasi proses adalah mekanisme pengaturan jalannya beberapa proses yang berjalan secara bersamaan dalam sistem operasi agar tidak terjadi konflik dalam mengakses sumber daya atau data bersama. Sinkronisasi penting untuk menghindari inkonsistensi data yang dapat terjadi karena proses-proses tersebut dapat mengakses dan memodifikasi data secara bersamaan. Mekanisme ini menjamin bahwa proses yang bersaing untuk mengakses ke sumber daya bersama dapat melakukannya secara berurutan dan terkontrol, sehingga menghindari masalah seperti kondisi ras dan ketidakkonsistenan data.
- Masalah deadlock adalah kondisi dimana beberapa proses saling menunggu satu sama lain untuk melepaskan sumber daya yang dibutuhkan, sehingga tidak ada proses yang dapat melanjutkan eksekusinya. Deadlock terjadi bila empat kondisi utama terpenuhi sekaligus, yakni: mutualclusion (satu sumber daya hanya bisa digunakan satu proses pada suatu waktu), hold and wait (proses menahan satu sumber daya sambil menunggu sumber daya lain), no preemption (sumber daya tidak bisa diambil paksa dari proses yang memilikinya), dancircular wait (terdapat siklus menunggu sumber daya antar proses). Pemahaman dan penanganan deadlock memerlukan pengenalan kondisi ini serta penggunaan teknik sinkronisasi seperti semaphore dan monitor untuk mencegah atau mengatasi kebuntuan.

---

## Langkah Praktikum
1.  Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)

- Implementasikan versi sederhana dari masalah Dining Philosophers tanpa mekanisme pencegahan deadlock.
Contoh pseudocode:
while true:
  think()
  pick_left_fork()
  pick_right_fork()
  eat()
  put_left_fork()
  put_right_fork()

- Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).
- Identifikasi kapan dan mengapa kebuntuan terjadi.

2. Eksperimen 2 – Versi Tetap (Menggunakan Semaphore / Monitor)

*Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
-Menggunakan semaphore (mutex) untuk mengontrol akses.
-Membatasi jumlah filosof yang dapat dimakan secara bersamaan (maks 4).
-pengaturan urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).
*Analisis hasil modifikasi dan buktikan bahwa kebuntuan telah dihindari.

3. Eksperimen 3 – Analisis Kebuntuan
Menjelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut menyelesaikan pada versi fixed.
Sajikan hasil analisis dalam tabel seperti contoh berikut:

Kondisi Deadlock	Terjadi di Versi Deadlock	Solusi di Versi Fixed
Pengecualian Bersama	Ya (satu garpu hanya satu proses)	Gunakan semaphore untuk mengontrol akses
Tahan dan Tunggu	Ya	Hindari proses menahan lebih dari satu sumber daya
Tidak Ada Pendahuluan	Ya	Tidak ada mekanisme pelepasan paksa
Menunggu Melingkar	Ya	Ubah urutan pengambilan sumber day


4. Eksperimen 4 – Dokumentasi

Simpan semua diagram, simulasi tangkapan layar, dan hasil diskusi di:
praktikum/week7-concurrency-deadlock/screenshots/
Tuliskan laporan kelompok di laporan.md(format IMRaD singkat: Pendahuluan, Metode, Hasil, Analisis, Diskusi ).

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
![Screenshot hasil](./praktikumweek7-concurrency-deadlockscreenshots/)

---

## Analisis
- Eksperimen pertama, 5 filsuf dapat mencapai deadlock permanen saat semua mengambil garpu kiri bersamaan lalu menunggu garpu kanan, memenuhi 4 kondisi Coffman secara penuh. Simulasi alur mengilustrasikan circular wait (P0→F1→P1→F2→...→P4→F0), menyebabkan sistem terkunci total tanpa kemajuan. Hasil ini membuktikan bahaya race condition dan urutan pengambilan sumber daya yang simetris dalam sistem konkuren.​
-ekperimen kedua Modifikasi dengan semaphore room=4 dan asimetri P4 mematahkan circular wait karena selalu ada minimal 1 garpu bebas, memungkinkan progres kontinu. Simulasi menunjukkan 4 filsuf makan bergantian sementara 1 menunggu, menghindari kebuntuan sambil mempertahankan paralelisme maksimal. Teknik ini menjamin liveness (tidak ada starvation) melalui fairness semaphore FIFO.​

---

## Kesimpulan
Eksperimen Sinkronisasi & Deadlock
Eksperimen Dining Philosophers membuktikan bahwa implementasi tanpa sinkronisasi menyebabkan deadlock permanen melalui circular wait saat semua filsuf mengambil garpu kiri bersamaan, memenuhi 4 kondisi. Modifikasi dengan semaphore room=4 dan asimetri berhasil mematahkan circular wait, menjamin progres kontinu karena selalu ada minimal 1 garpu bebas.​

1. Pencegahan > Deteksi: Mengontrol akses sumber daya (semaphore) lebih efisien daripada recovery deadlock.​
2. Kondisi Kritis: Sinkronisasi esensial untuk hindari race condition di sistem konkuren seperti multi-threading dan database locks.​
3. Praktik Industri: Teknik ini diterapkan di Linux mutex, Java synchronized, dan Web3 smart contract concurrency.

---

## Quiz
1. Sebutkan empat kondisi utama penyebab deadlock.
- Mutual Exclusion (Eksklusi Saling)
Sumber daya tidak dapat digunakan secara bersama; hanya satu proses yang boleh menggunakannya pada satu waktu.

- Hold and Wait
Proses sudah memegang satu sumber daya dan menunggu sumber daya lain yang sedang digunakan proses lain.

- No Preemption
Sumber daya yang sedang digunakan tidak dapat diambil paksa; hanya bisa dilepas secara sukarela oleh proses yang memegangnya.

- Circular Wait
Terdapat rangkaian proses yang saling menunggu secara melingkar, misalnya P1 menunggu sumber daya yang dipegang P2, P2 menunggu yang dipegang P3, dan seterusnya hingga kembali ke P1.
Jika keempat kondisi ini terjadi bersamaan, maka deadlock dapat muncul.

2. Mengapa sinkronisasi diperlukan dalam sistem operasi?
  Sinkronisasi diperlukan dalam sistem operasi untuk memastikan bahwa proses dan thread yang berjalan bersama-samadapat mengakses sumber daya secara aman, konsisten, dan teratur. Alasan utamanya adalah:

-  Mencegah kondisi balapan (race conditions)
Tanpa sinkronisasi, dua atau lebih proses dapat mengakses dan mengubah data bersama secara bersamaan sehingga hasil akhirnya menjadi tidak terduga.

-  Menjaga konsistensi data
 Ketika beberapa proses membaca/menulis ke data yang sama, mekanisme sinkronisasi (seperti mutex, semaphore) membuat operasi tersebut terjadi secara atomik sehingga data tidak korup.

-  Mengatur akses ke sumber daya bersama
 Sumber daya seperti file, printer, atau variabel global tidak boleh digunakan sembarangan oleh banyak proses sekaligus. Sinkronisasi mencegah konflik.

-  Menghindari deadlock dan starvation
 Dengan aturan sinkronisasi yang tepat, sistem dapat mencegah situasi proses saling menunggu tanpa akhir atau ada proses yang tidak pernah mendapat giliran.

-  Koordinasi antar-proses atau antar-thread
 Beberapa proses perlu bekerja dalam urutan tertentu (misalnya producer-consumer). Sinkronisasi membantu memastikan urutan eksekusi tersebut benar. sinkronisasi diperlukan untuk keamanan, konsistensi, dan ketertiban dalam eksekusi proses yang paralel atau bersamaan.

3. Jelaskan perbedaan antara semaphore dan monitor.
 Semaphore dan monitor merupakan mekanisme sinkronisasi untuk mengelola akses sumber daya bersama dalam pemrograman konkuren, tetapi semaphore berupa variabel integer non-negatif yang dimodifikasi melalui operasi wait() dan signal(), sedangkan monitor adalah tipe data abstrak tingkat tinggi yang mengenkapsulasi variabel bersama dan prosedur aksesnya. Semaphore bersifat low-level dan fleksibel untuk mengontrol jumlah akses simultan ke sumber daya, sementara monitor memastikan hanya satu proses yang dieksekusi di dalamnya pada satu waktu, sehingga lebih aman dari kesalahan seperti race condition.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
  hujan mulu pak
- Bagaimana cara Anda mengatasinya? 
  beli jas ujan
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
