
# Laporan Praktikum Minggu 10
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)


---

## Identitas
- **Nama**  : Aufaa Rifaah  
- **NIM**   : 250202932
- **Kelas** : 1IKRB

---

## Tujuan
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.



---

## Dasar Teori
Pengantar Manajemen Memori Virtual
Manajemen memori virtual memungkinkan sistem operasi mengelola memori fisik (RAM) dan sekunder (disk) sebagai satu kesatuan. Memori dibagi menjadi halaman (page) tetap ukuran, yang dipetakan ke frame di RAM atau disimpan di disk. Ini mendukung program besar tanpa memori fisik cukup, dengan isolasi proses dan efisiensi.

Mekanisme Page Fault dan Page Replacement
Page Fault terjadi saat program mengakses halaman yang tidak di RAM, memicu pemuatan dari disk. Jika RAM penuh, page replacement mengganti halaman lama dengan yang baru. Algoritma menentukan halaman yang diganti untuk meminimalkan fault, meningkatkan performa.

Algoritma FIFO (First-In First-Out)
Mengganti halaman tertua (pertama masuk). Mudah diimplementasikan dengan antrian, tapi tidak mempertimbangkan frekuensi akses, rentan terhadap anomaly Belady (fault meningkat dengan frame tambahan).

Algoritma LRU (Least Recently Used)
Mengganti halaman paling lama tidak diakses. Asumsi: halaman baru-baru ini digunakan lebih mungkin diakses lagi. Lebih akurat daripada FIFO, tapi overhead lebih tinggi (tracking akses).

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```python

reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3

def fifo(reference_string, frame_size):
    frames = []
    page_fault = 0

    print("=== FIFO ===")
    for page in reference_string:
        if page in frames:
            print(f"Page {page} -> HIT | Frame: {frames}")
        else:
            page_fault += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            print(f"Page {page} -> FAULT | Frame: {frames}")

    print("Total Page Fault FIFO:", page_fault)
    return page_fault

def lru(reference_string, frame_size):
    frames = []
    page_fault = 0

    print("\n=== LRU ===")
    for page in reference_string:
        if page in frames:
            frames.remove(page)
            frames.append(page)
            print(f"Page {page} -> HIT | Frame: {frames}")
        else:
            page_fault += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            print(f"Page {page} -> FAULT | Frame: {frames}")

    print("Total Page Fault LRU:", page_fault)
    return page_fault

fifo_fault = fifo(reference_string, frame_size)
lru_fault = lru(reference_string, frame_size)

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/week%2010%20(2).png)
![Screenshot hasil](./screenshots/week%2010%20(3).png)
![Screenshot hasil](./screenshots/week%2010.png)
---

## Analisis
-  Makna Hasil Percobaan

Hasil percobaan menunjukkan bahwa algoritma LRU menghasilkan jumlah page fault lebih sedikit dibanding FIFO. Hal ini membuktikan bahwa cara sistem operasi memilih halaman yang akan diganti sangat berpengaruh terhadap kinerja memori. FIFO hanya melihat urutan masuk halaman, sehingga halaman yang masih sering digunakan bisa terbuang. Sebaliknya, LRU mempertahankan halaman yang baru saja dipakai sehingga akses memori menjadi lebih efisien.

- Kaitan dengan Teori Sistem Operasi

Pada teori sistem operasi, kernel bertanggung jawab mengelola memori melalui mekanisme memory management. Saat terjadi page fault, kernel akan menjalankan system call untuk mengambil halaman dari penyimpanan sekunder (disk) ke memori utama (RAM). Proses ini membutuhkan waktu yang lebih lama dibanding akses RAM biasa. Dalam arsitektur sistem operasi, proses berjalan di user mode, sedangkan penggantian halaman dilakukan di kernel mode. Algoritma FIFO dan LRU merupakan bagian dari kebijakan (policy) kernel dalam menentukan halaman mana yang diganti. Karena LRU lebih sesuai dengan pola akses program (locality of reference), kernel dapat mengurangi jumlah page fault dan meningkatkan performa sistem secara keseluruhan.

- Perbedaan Hasil pada OS Linux dan Windows

Secara konsep, hasil logika FIFO dan LRU akan sama baik di Linux maupun Windows karena algoritmanya identik. Namun, hasil kinerja nyata dapat berbeda karena perbedaan implementasi kernel. Pada Linux, manajemen memori cenderung lebih transparan dan agresif dalam caching, serta menggunakan pendekatan yang mendekati LRU. Hal ini membuat Linux sering menghasilkan performa yang stabil pada sistem multitasking. Pada Windows, algoritma penggantian halaman juga kompleks dan adaptif, tetapi kebijakan manajemen memorinya berbeda dengan Linux. Windows lebih banyak mengoptimalkan untuk aplikasi interaktif, sehingga pola page fault dapat terlihat berbeda saat diuji pada beban kerja tertentu.  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
Berikut **kesimpulan praktikum** yang singkat, jelas, dan cocok langsung dimasukkan ke laporan:

---

## Kesimpulan

Berdasarkan hasil praktikum simulasi algoritma penggantian halaman FIFO dan LRU, dapat disimpulkan bahwa algoritma LRU menghasilkan jumlah *page fault* yang lebih sedikit dibandingkan FIFO. Hal ini menunjukkan bahwa pemilihan halaman berdasarkan riwayat penggunaan lebih efektif dibandingkan hanya berdasarkan urutan kedatangan. Algoritma FIFO memiliki implementasi yang sederhana, tetapi kurang efisien karena dapat mengganti halaman yang masih sering digunakan. Sebaliknya, LRU lebih sesuai dengan pola akses program sehingga mampu meningkatkan kinerja manajemen memori. Percobaan ini membuktikan bahwa kebijakan pengelolaan memori pada kernel sistem operasi sangat berpengaruh terhadap performa sistem, khususnya dalam mengurangi *page fault* dan meningkatkan efisiensi penggunaan memori utama.

---

## Quiz
1. Apa perbedaan utama FIFO dan LRU?
IFO (First In First Out)
FIFO mengganti data yang paling dulu masuk ke memori, tanpa memperhatikan apakah data tersebut masih sering digunakan atau tidak. Selama data itu masuk paling awal, maka ia akan dikeluarkan lebih dulu. Akibatnya, FIFO bisa saja menghapus data yang sebenarnya masih sering dipakai, sehingga kinerjanya kurang efisien dalam beberapa kondisi.

LRU (Least Recently Used)
LRU mengganti data yang paling lama tidak digunakan. Algoritma ini memperhatikan pola pemakaian, sehingga data yang sering diakses akan dipertahankan lebih lama di memori. Karena menyesuaikan dengan perilaku penggunaan, LRU umumnya memberikan performa yang lebih baik, meskipun implementasinya lebih kompleks dibanding FIFO.

2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly? 
   Pada FIFO, halaman yang masuk paling awal akan dikeluarkan lebih dulu, meskipun halaman itu masih sering dipakai. Ketika jumlah frame ditambah, urutan masuk halaman bisa berubah sehingga halaman yang “seharusnya berguna” justru terbuang lebih cepat. Akibatnya, sistem malah mengalami lebih banyak page fault walaupun kapasitas memori diperbesar. Dengan kata lain, FIFO tidak memiliki sifat stack (stack property). Artinya, himpunan halaman pada memori dengan jumlah frame kecil tidak selalu menjadi subset dari memori dengan frame lebih besar. Inilah yang menyebabkan penambahan frame justru bisa memperburuk kinerja. Sebaliknya, algoritma seperti LRU tidak mengalami Belady’s Anomaly karena halaman yang dipertahankan selalu berdasarkan pola penggunaan, sehingga penambahan frame tidak meningkatkan jumlah page fault.  

3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
   LRU menyimpan halaman yang baru saja digunakan dan mengganti halaman yang paling lama tidak diakses. Hal ini sesuai dengan prinsip locality of reference, yaitu program cenderung mengakses halaman yang sama berulang kali dalam waktu berdekatan. Karena itu, LRU lebih jarang membuang halaman yang masih dibutuhkan, sehingga jumlah page fault lebih kecil. Sebaliknya, FIFO tidak memperhatikan apakah suatu halaman masih sering dipakai atau tidak. Halaman yang masuk lebih awal akan dikeluarkan lebih dulu, walaupun sebenarnya masih aktif digunakan. Akibatnya, FIFO bisa sering mengganti halaman penting dan menyebabkan page fault lebih banyak. Selain itu, LRU memiliki sifat stack, artinya penambahan jumlah frame tidak akan meningkatkan jumlah page fault. FIFO tidak memiliki sifat ini, sehingga kinerjanya bisa tidak stabil.


    

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  gabut
- Bagaimana cara Anda mengatasinya?  cari inpo

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
