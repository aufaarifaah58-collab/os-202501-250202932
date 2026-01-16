
# Laporan Praktikum Minggu 12
Topik:  Virtualisasi Menggunakan Virtual Machine

---

## Identitas
- **Nama**  : Aufaa Rifah ( 250202932) 
              Azid MIrza Maulana (250202933)

- **Kelas** : 1IKRB

---

## Tujuan
1. Tuliskan tujuan praktikum minggu ini.  
2. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).
3. Membuat dan menjalankan sistem operasi guest di dalam VM.
4. Mengatur konfigurasi resource VM (CPU, RAM, storage).
5. Menjelaskan mekanisme proteksi OS melalui virtualisasi.
6. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
Virtualisasi Sistem Operasi Menggunakan Virtual Machine (VM)
Virtualisasi sistem operasi adalah teknologi yang memungkinkan satu komputer fisik menjalankan lebih dari satu sistem operasi secara bersamaan. Teknologi ini bekerja dengan cara menciptakan lingkungan virtual yang menyerupai komputer fisik, yang disebut Virtual Machine (VM). Dengan virtualisasi, sistem operasi tidak berjalan langsung di atas perangkat keras, melainkan di atas lapisan perantara.

---

## Langkah Praktikum
1. Instalasi Virtual Machine
- Instal VirtualBox atau VMware pada komputer host.
- Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

2. Pembuatan OS Guest
- Buat VM baru dan pilih OS guest (misal: Ubuntu Linux).
- Atur resource awal:
CPU: 1–2 core
RAM: 2–4 GB
Storage: ≥ 20 GB

3. Instalasi Sistem Operasi
- Jalankan proses instalasi OS guest sampai selesai.
- Pastikan OS guest dapat login dan berjalan normal.

4. Konfigurasi Resource
- Ubah konfigurasi CPU dan RAM.
- Amati perbedaan performa sebelum dan sesudah perubahan resource.

5. Analisis Proteksi OS
- Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.
- Kaitkan dengan konsep sandboxing dan hardening OS.

6. Dokumentasi
- Ambil screenshot setiap tahap penting.
- Simpan di folder screenshots/.

7. Commit 

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
![Screenshot hasil](./screenshots/week12%20(3).jpeg)
![Screenshot hasil](./screenshots/week12.jpeg)
![Screenshot hasil](./screenshots/week12%20(2).jpeg)
![Screenshot hasil](./screenshots/week%2012..jpeg)
![Screenshot hasil](./screenshots/week12%20(5).jpeg)
![Screenshot hasil](./screenshots/week12%20(4).jpeg)


---


## Analisis
- Jelaskan makna hasil percobaan.  
  Hasil percobaan menunjukkan bagaimana pengaturan resource pada VM memengaruhi kinerja sistem operasi guest. Saat CPU atau RAM ditingkatkan, OS guest berjalan lebih lancar, program dapat dijalankan lebih cepat, dan respons sistem lebih baik. Sebaliknya, jika resource dikurangi, OS guest menjadi lambat dan terkadang tidak stabil. Hal ini sesuai dengan teori kernel dan system call, karena kernel guest OS mengatur eksekusi program dan penggunaan resource. Namun, semua permintaan hardware tetap melalui hypervisor, sehingga host OS tetap aman dan stabil. Selain itu, percobaan ini menunjukkan prinsip isolasi sistem: meskipun guest OS mengalami error atau crash, host OS tetap berfungsi normal. VM bekerja seperti sandbox, menjaga agar aktivitas di guest OS tidak memengaruhi host OS.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
  Fungsi Kernel
Kernel pada guest OS bertugas mengatur semua sumber daya seperti CPU, memori, dan perangkat I/O. Saat resource VM ditingkatkan, kernel dapat mengalokasikan lebih banyak CPU dan RAM ke proses, sehingga performa OS guest meningkat. Sebaliknya, jika resource terbatas, kernel harus membagi resource secara ketat, sehingga sistem menjadi lambat.

  System Call
Semua permintaan akses perangkat keras dari guest OS dilakukan melalui system call. Di VM, system call ini tidak langsung ke hardware fisik, tetapi diteruskan oleh hypervisor ke host OS. Hal ini menjelaskan mengapa guest OS bisa berjalan aman tanpa memengaruhi host OS, sekaligus tetap dapat menggunakan CPU, memori, dan storage.

  Arsitektur OS
Hasil percobaan menunjukkan konsep layered architecture dalam OS. Guest OS berjalan di atas hypervisor yang menjadi lapisan perantara antara hardware dan sistem operasi. Dengan cara ini, guest OS seolah-olah memiliki komputer sendiri, tetapi tetap dibatasi dan diatur oleh host OS melalui hypervisor, sehingga terjadi isolasi sistem.
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
  VM berjalan di Linux cenderung lebih cepat dan responsif karena manajemen resource kernel Linux lebih efisien. Di Windows, VM bisa sedikit lebih lambat karena overhead virtualisasi lebih tinggi. Namun, isolasi sistem tetap terjaga, sehingga crash di guest OS tidak memengaruhi host OS di kedua lingkungan.
---

## Kesimpulan
Virtual Machine memungkinkan satu komputer menjalankan beberapa sistem operasi secara aman dan terisolasi. Kinerja guest OS dipengaruhi oleh alokasi CPU, RAM, dan storage; semakin besar resource, semakin lancar sistem berjalan. Hypervisor mengatur akses guest OS ke hardware host tanpa mengganggu host OS. Linux sebagai host biasanya membuat VM lebih responsif dibanding Windows, tetapi isolasi sistem tetap terjaga di kedua OS.

---

## Quiz
1. Apa perbedaan antara host OS dan guest OS?
   Host OS adalah sistem operasi utama yang terpasang langsung di komputer fisik, sedangkan Guest OS adalah sistem operasi yang dijalankan di dalam Virtual Machine (VM) dan menggunakan resource host OS melalui hypervisor. Guest OS berjalan terisolasi sehingga gangguan pada guest tidak memengaruhi host.

2. Apa peran hypervisor dalam virtualisasi?
   Hypervisor adalah perangkat lunak yang mengatur Virtual Machine dengan membagi resource komputer, menjaga isolasi antara guest OS dan host OS, serta meneruskan akses hardware sehingga guest OS dapat berjalan seolah-olah di komputer sendiri. Hypervisor memungkinkan satu komputer menjalankan beberapa sistem operasi sekaligus.

3. Mengapa virtualisasi meningkatkan keamanan sistem?
   Virtualisasi meningkatkan keamanan karena setiap Virtual Machine berjalan terisolasi dari host OS dan VM lain, sehingga gangguan pada guest OS tidak memengaruhi sistem utama. Guest OS dijalankan di lingkungan terbatas (sandbox) dan hanya menggunakan resource yang dialokasikan, sehingga akses ke data host dapat dikontrol dengan aman.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  menabung
- Bagaimana cara Anda mengatasinya?  sabar

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
