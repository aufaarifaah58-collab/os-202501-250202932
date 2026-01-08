
# Laporan Praktikum Minggu 11
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Aufaa Rifaah 
- **NIM**   : 250202932 
- **Kelas** : 1IKRB

---

## Tujuan 
1. Membuat program sederhana untuk mendeteksi deadlock.
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.
4. Memberikan interpretasi hasil uji secara logis dan sistematis.
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---


## Dasar Teori
Deteksi Deadlock dalam Sistem Operasi
Deadlock adalah kondisi ketika dua atau lebih proses saling menunggu sumber daya yang sedang dipegang oleh proses lain, sehingga tidak ada satu pun proses yang dapat melanjutkan eksekusinya. Berbeda dengan pencegahan (deadlock prevention) dan penghindaran (deadlock avoidance) yang berusaha mencegah deadlock sebelum terjadi, deteksi deadlock bertujuan untuk menemukan deadlock yang sudah terjadi, kemudian melakukan tindakan pemulihan. Pendekatan deteksi deadlock digunakan pada sistem operasi yang mengizinkan terjadinya deadlock karena alasan efisiensi. Sistem ini tidak membatasi secara ketat penggunaan sumber daya, tetapi secara berkala menjalankan algoritma untuk mengecek apakah deadlock sedang terjadi

---
  
## Langkah Praktikum
1. Menyiapkan Dataset 
 
 Gunakan dataset sederhana yang berisi:
 - Daftar proses
 - Menentukan apakah sistem berada dalam kondisi deadlock.
 - Resource Request / Need

2. Implementasi Algoritma Deteksi Deadlock

 Program minimal harus:
 - Membaca data proses dan resource.
 - Menentukan apakah sistem berada dalam kondisi deadlock.
 - Menampilkan proses mana saja yang terlibat deadlock

3. Eksekusi & Validasi

 - Jalankan program dengan dataset uji.
 - Validasi hasil deteksi dengan analisis manual/logis.
 - Simpan hasil eksekusi dalam bentuk screenshot.
   
4. Analisis Hasil

 - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).
 - Jelaskan mengapa deadlock terjadi atau tidak terjadi.
 - Kaitkan hasil dengan teori deadlock (empat kondisi).   

5. Commit & Push

git add .
git commit -m "Minggu 11 - Deadlock Detection"
git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
``` python
# Dataset
processes = ["P1", "P2", "P3"]

allocation = {
    "P1": "R1",
    "P2": "R2",
    "P3": "R3"
}

request = {
    "P1": "R2",
    "P2": "R3",
    "P3": "R1"
}

# Membuat resource -> proses yang memegangnya
resource_owner = {}
for p, r in allocation.items():
    resource_owner[r] = p

# Membuat graph ketergantungan proses
graph = {}
for p in processes:
    req_res = request[p]
    if req_res in resource_owner:
        graph[p] = resource_owner[req_res]

# Deteksi siklus (deadlock)
visited = set()
stack = set()
deadlock_processes = set()

def detect_cycle(p):
    if p in stack:
        deadlock_processes.update(stack)
        return True
    if p in visited:
        return False

    visited.add(p)
    stack.add(p)

    if p in graph:
        if detect_cycle(graph[p]):
            return True

    stack.remove(p)
    return False

for p in processes:
    detect_cycle(p)

# Output
print("Hasil Deteksi Deadlock:")
for p in processes:
    status = "Deadlock" if p in deadlock_processes else "Tidak Deadlock"
    print(f"{p}: {status}")


```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/kode%20ss%20python.png)
![Screenshot hasil](./screenshots/hasil%20python%203.png)

---

## Analisis
 - Makna Hasil Percobaan
Hasil percobaan menunjukkan bahwa P1, P2, dan P3 mengalami deadlock. Artinya, semua proses saling menunggu resource yang sedang dipegang proses lain sehingga tidak ada proses yang bisa berjalan. Hal ini terjadi karena keempat kondisi deadlock terpenuhi: mutual exclusion, hold and wait, no preemption, dan circular wait.
 
 - Hubungan dengan Teori Sistem Operasi
Kernel bertugas mengatur sumber daya dan eksekusi proses. Ketika deadlock terjadi, kernel tidak bisa menyelesaikan proses yang saling menunggu.
System call adalah cara proses meminta atau melepaskan resource. Jika permintaan menyebabkan siklus menunggu, proses akan terblokir.
Scheduler tidak bisa menjalankan proses yang macet, tapi proses lain tetap bisa menggunakan CPU.
 
 - Perbedaan di OS Berbeda
Di Linux, deadlock bisa dipantau dengan perintah seperti ps atau top.
Di Windows, deadlock bisa terjadi di thread tertentu dan monitoring dilakukan lewat Task Manager atau Resource Monitor.
Konsep deadlock sama di semua OS, tapi cara mendeteksi dan menanganinya bisa berbeda karena struktur kernel dan manajemen resource berbeda.

---

## Kesimpulan
Percobaan berhasil mendeteksi deadlock pada P1, P2, dan P3 yang saling menunggu resource. Deadlock terjadi karena empat kondisi perlu terpenuhi: mutual exclusion, hold and wait, no preemption, dan circular wait. Algoritma deteksi membantu mengetahui proses yang macet sehingga sistem bisa mengambil tindakan pemulihan.

---

## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection?
   Deadlock Prevention
Strategi ini mencegah deadlock dengan memastikan salah satu dari empat kondisi perlu (mutual exclusion, hold and wait, no preemption, circular wait) tidak pernah terjadi, misalnya melalui pengurutan sumber daya untuk hindari circular wait. Pendekatan ini statis dan sering mengakibatkan utilisasi sumber daya rendah karena pembatasan ketat.

   Deadlock Avoidance
Pendekatan ini dinamis, memungkinkan alokasi sumber daya hanya jika sistem tetap dalam "safe state" menggunakan algoritma seperti Banker's Algorithm atau Resource-Allocation Graph. Sistem memprediksi permintaan masa depan proses untuk hindari keadaan tidak aman tanpa memblokir kemungkinan deadlock sepenuhnya.

   Deadlock Detection
Strategi ini membiarkan deadlock terjadi, lalu mendeteksinya secara periodik melalui graf alokasi sumber daya atau algoritma khusus, diikuti recovery seperti terminasi proses atau preemption. Metode ini fleksibel tapi memerlukan overhead komputasi tinggi untuk deteksi dan pemulihan.
​
2. [Pertanyaan 2]  
 Deadlock prevention dan avoidance memang dapat mencegah deadlock, tetapi kedua pendekatan tersebut sering membatasi sistem secara ketat atau membutuhkan informasi lengkap tentang kebutuhan sumber daya proses, yang dalam praktiknya tidak selalu tersedia. Akibatnya, pemanfaatan sumber daya menjadi kurang efisien dan kinerja sistem bisa menurun. Dalam sistem operasi modern, terutama yang bersifat umum dan multitasking, deadlock sering dianggap kejadian yang jarang tetapi mungkin terjadi. Oleh karena itu, sistem lebih memilih mengizinkan deadlock terjadi agar penggunaan sumber daya tetap fleksibel, lalu mendeteksinya ketika benar-benar muncul. Dengan deteksi deadlock, sistem dapat mengetahui proses mana yang saling menunggu dan mengambil tindakan pemulihan seperti menghentikan proses tertentu atau melakukan preemption sumber daya. Selain itu, deteksi deadlock penting karena tidak semua deadlock dapat diprediksi. Banyak aplikasi memiliki pola permintaan sumber daya yang dinamis dan sulit diperkirakan di awal. Tanpa mekanisme deteksi, sistem bisa mengalami hang permanen, di mana beberapa proses berhenti selamanya tanpa diketahui penyebabnya.
 Dengan demikian, deteksi deadlock diperlukan untuk menjaga keandalan dan kestabilan sistem operasi, memastikan sistem tetap dapat pulih dari kondisi macet, serta memberikan keseimbangan antara efisiensi penggunaan sumber daya dan keselamatan sistem.

3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
 Deteksi deadlock memberikan fleksibilitas dan efisiensi penggunaan sumber daya, tetapi memiliki risiko gangguan sistem dan biaya komputasi tambahan karena deadlock ditangani setelah terjadi. Pendekatan ini paling sesuai untuk sistem yang mengutamakan kinerja dan memiliki kemungkinan deadlock yang relatif rendah.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
  banyak tugas 
- Bagaimana cara Anda mengatasinya?  
  ngerjain 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
