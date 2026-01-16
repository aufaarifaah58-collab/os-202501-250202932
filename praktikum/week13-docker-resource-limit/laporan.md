
# Laporan Praktikum Minggu 13
Topik: Docker - Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Aufaa Rufaah
- **NIM**   : 250202932
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Memahami cara membuat Dockerfile untuk aplikasi sederhana
2. Menjalankan container dengan dan tanpa pembatasan resource
3. Menganalisis dampak pembatasan resource terhadap performa aplikasi
4. Memahami pentingnya resource management dalam containerization

---

## Dasar Teori
Praktikum ini bertujuan untuk mempelajari mekanisme pembatasan resource (CPU dan memori) pada Docker container menggunakan cgroups (control groups) yang merupakan fitur kernel Linux untuk mengatur dan membatasi penggunaan resource oleh proses.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
   - Persiapan Lingkungan
   - Pastikan Docker terpasang dan berjalan.
Verifikasi: docker version
            docker ps

   - Membuat Aplikasi/Skrip Uji
   - Buat program sederhana di folder code/ (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).
   
   - Membuat Dockerfile
   - Tulis Dockerfile untuk menjalankan program uji.
   - Build image
   
   - Menjalankan Container Tanpa Limit
   - Menjalankan Container Dengan Limit Resource
   - Monitoring Sederhan

2. Perintah yang dijalankan.
   - docker version
   - docker ps
   - docker build -t week13-resource-limit .
   - docker run --rm week13-resource-limit
   - docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   - docker stats
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```python

import time
import sys
import psutil
import os

def cpu_intensive_task(duration=10):
    """Tugas intensif CPU - komputasi berulang"""
    print(f"[CPU TEST] Memulai komputasi intensif selama {duration} detik...")
    start_time = time.time()
    counter = 0
    
    while time.time() - start_time < duration:
        # Operasi matematika kompleks
        result = sum([i**2 for i in range(1000)])
        counter += 1
    
    print(f"[CPU TEST] Selesai! Iterasi: {counter:,}")
    return counter

def memory_intensive_task(max_mb=200, step_mb=50):
    """Tugas intensif memori - alokasi bertahap"""
    print(f"[MEMORY TEST] Mengalokasikan memori hingga {max_mb}MB...")
    data_list = []
    
    try:
        for mb in range(0, max_mb, step_mb):
            # Alokasi memori ~50MB per iterasi
            chunk = ' ' * (step_mb * 1024 * 1024)
            data_list.append(chunk)
            
            # Cek penggunaan memori saat ini
            process = psutil.Process(os.getpid())
            mem_info = process.memory_info()
            mem_mb = mem_info.rss / 1024 / 1024
            
            print(f"[MEMORY TEST] Teralokasi: {mb + step_mb}MB | RSS: {mem_mb:.2f}MB")
            time.sleep(1)
        
        print(f"[MEMORY TEST] Sukses mengalokasi {max_mb}MB!")
        
    except MemoryError:
        print(f"[MEMORY TEST] ERROR - Memori tidak cukup!")
        sys.exit(1)
    
    return len(data_list)

def display_system_info():
    """Tampilkan informasi sistem"""
    print("="*60)
    print("INFORMASI SISTEM & RESOURCE")
    print("="*60)
    
    # CPU info
    cpu_count = psutil.cpu_count()
    print(f"CPU Cores: {cpu_count}")
    
    # Memory info
    mem = psutil.virtual_memory()
    mem_total_mb = mem.total / 1024 / 1024
    mem_available_mb = mem.available / 1024 / 1024
    print(f"Total Memory: {mem_total_mb:.2f}MB")
    print(f"Available Memory: {mem_available_mb:.2f}MB")
    
    print("="*60)
    print()

def main():
    print("\n" + "="*60)
    print("DOCKER RESOURCE LIMIT TEST")
    print("="*60 + "\n")
    
    # Tampilkan info sistem
    display_system_info()
    
    # Test CPU
    print("\n[1] CPU INTENSIVE TEST")
    print("-"*60)
    start = time.time()
    iterations = cpu_intensive_task(duration=10)
    cpu_time = time.time() - start
    print(f"Waktu eksekusi: {cpu_time:.2f} detik")
    print(f"Iterasi per detik: {iterations/cpu_time:.2f}")
    
    # Jeda
    print("\nMenunggu 2 detik...\n")
    time.sleep(2)
    
    # Test Memory
    print("[2] MEMORY INTENSIVE TEST")
    print("-"*60)
    chunks = memory_intensive_task(max_mb=200, step_mb=50)
    print(f"Total chunks teralokasi: {chunks}")
    
    # Summary
    print("\n" + "="*60)
    print("TEST SELESAI")
    print("="*60)

if __name__ == "__main__":
    main()

# Gunakan Python slim image untuk ukuran lebih kecil
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir psutil

# Copy aplikasi ke container
COPY app.py .

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Jalankan aplikasi
CMD ["python", "app.py"]
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/docker%20build%20-t%20week13-resource-limit%20..png)
![Screenshot hasil](./screenshots/docker%20run%20--rm%20--cpus=0.5%20--memory=256m%20week13-resource-limit.png)
![Screenshot hasil](./screenshots/docker%20run%20--rm%20week13-resource-limit.png)

---

## Analisis
- Makna Hasil Percobaan

Percobaan ini menunjukkan bahwa Docker mampu mengatur dan membatasi penggunaan resource sistem seperti CPU dan memori pada setiap container. Saat container dijalankan tanpa limit, aplikasi dapat menggunakan resource secara maksimal sesuai kemampuan host, sehingga proses berjalan lebih cepat dan alokasi memori berhasil tanpa hambatan. Ketika limit CPU diterapkan, kecepatan proses komputasi menurun.  Hal ini terlihat dari waktu eksekusi yang lebih lama dan jumlah iterasi per detik yang berkurang. Kondisi ini membuktikan bahwa Docker benar-benar membatasi jatah waktu CPU yang dapat digunakan oleh container, sehingga mencegah satu container mendominasi penggunaan CPU. Pada limit memori, percobaan memperlihatkan bahwa container hanya dapat menggunakan memori sesuai batas yang ditentukan. Jika aplikasi mencoba mengalokasikan memori melebihi batas tersebut, maka proses dapat gagal atau container akan dihentikan oleh sistem melalui mekanisme Out of Memory (OOM) Killer. Hal ini menegaskan pentingnya pengaturan memori agar aplikasi tidak menyebabkan kehabisan memori pada sistem. Saat limit CPU dan memori diterapkan secara bersamaan, performa aplikasi menjadi paling rendah dibandingkan skenario lainnya. Hal ini menunjukkan bahwa pembatasan resource secara kombinasi sangat berpengaruh terhadap kinerja aplikasi, namun tetap menjaga stabilitas sistem secara keseluruhan. Secara keseluruhan, percobaan ini membuktikan bahwa mekanisme pembatasan resource pada Docker sangat penting untuk menjaga kestabilan sistem, memastikan pembagian resource yang adil, serta mencegah terjadinya gangguan antar container dalam lingkungan multi-container atau production.

- Hubungan dengan Teori Sistem Operasi
Kernel bertugas mengatur sumber daya dan eksekusi proses. Ketika deadlock terjadi, kernel tidak bisa menyelesaikan proses yang saling menunggu.

Pada percobaan Docker, pembatasan CPU dan memori dilakukan menggunakan cgroups, yaitu mekanisme yang bekerja langsung di tingkat kernel Linux. Artinya, kernel menentukan seberapa besar jatah CPU dan memori yang boleh digunakan oleh proses di dalam container. Ketika limit diterapkan, kernel akan membatasi akses resource sehingga proses tidak dapat melebihi batas yang ditentukan. Jika sebuah aplikasi di dalam container mencoba menggunakan CPU atau memori secara berlebihan, kernel akan melakukan tindakan pengendalian. Pada kasus pembatasan CPU, kernel akan melakukan throttling sehingga proses berjalan lebih lambat. Sedangkan pada pembatasan memori, jika penggunaan memori melebihi batas, kernel akan menghentikan proses melalui mekanisme Out of Memory (OOM) Killer.
Berbeda dengan deadlock, di mana proses saling menunggu resource sehingga kernel tidak dapat melanjutkan eksekusi proses, pada percobaan ini kernel masih memiliki kontrol penuh terhadap proses. Kernel dapat memaksa pembatasan atau menghentikan proses untuk menjaga kestabilan sistem. Hal ini menunjukkan bahwa manajemen resource yang baik oleh kernel dapat mencegah kondisi sistem menjadi tidak responsif. Dengan demikian, percobaan ini memperlihatkan secara nyata bagaimana teori manajemen proses dan resource pada Sistem Operasi diterapkan langsung dalam teknologi container seperti Docker.

- Perbedaan Hasil pada OS Linux dan Windows

Perbedaan hasil percobaan Docker Resource Limit pada sistem operasi Linux dan Windows terjadi karena perbedaan cara kernel mengelola sumber daya sistem. Pada Linux, Docker berjalan langsung di atas kernel Linux. Mekanisme pembatasan CPU dan memori menggunakan cgroups yang merupakan fitur asli kernel Linux. Karena itu, pembatasan resource pada container bersifat langsung, akurat, dan stabil. Ketika limit CPU atau memori diterapkan, kernel Linux segera mengatur atau menghentikan proses yang melanggar batas tersebut. Sementara itu, pada Windows, Docker tidak berjalan langsung di atas kernel Linux. Docker Desktop menggunakan virtualisasi (WSL2 atau Hyper-V) untuk menjalankan kernel Linux di dalam mesin virtual. Akibatnya, pembatasan resource container dipengaruhi oleh dua lapisan, yaitu:
- Pengaturan resource pada mesin virtual (WSL2/Hyper-V)
- Pembatasan resource pada container di dalam mesin virtual tersebut
Karena adanya lapisan virtualisasi tambahan, penggunaan CPU dan memori pada Windows dapat terasa kurang presisi dibandingkan Linux. Dalam beberapa kasus, monitoring resource juga menunjukkan nilai yang berbeda atau tidak sepenuhnya mencerminkan kondisi host Windows. Secara keseluruhan, Docker pada Linux memberikan hasil yang lebih konsisten dan efisien dalam pengelolaan resource, sedangkan pada Windows terdapat overhead tambahan akibat virtualisasi, meskipun secara fungsional pembatasan resource tetap berjalan.

---

## Kesimpulan 
Praktikum ini menunjukkan bahwa Docker mampu membatasi penggunaan CPU dan memori pada container secara efektif. Pembatasan CPU menyebabkan penurunan performa aplikasi, sedangkan pembatasan memori dapat menghentikan container jika penggunaan melebihi batas yang ditentukan. Pengaturan resource ini penting untuk menjaga kestabilan dan efisiensi sistem, terutama pada lingkungan multi-container dan production.

---


---

## Quiz
1.  Mengapa container perlu dibatasi CPU dan memori? 
   Container perlu dibatasi CPU dan memori untuk beberapa alasan penting:
- Isolasi Resource: Mencegah satu container mengonsumsi semua resource sistem dan mengganggu container lain (noisy neighbor problem)
- Stabilitas Sistem: Melindungi host system dari kehabisan resource yang dapat menyebabkan crash atau hang
- Predictability: Memastikan aplikasi berjalan dengan performa yang konsisten dan dapat diprediksi
- Cost Efficiency: Dalam environment cloud, resource limit membantu optimasi biaya dengan mengalokasikan resource sesuai kebutuhan
- Multi-tenancy: Memungkinkan multiple container berjalan bersamaan dengan fair resource allocation
- Prevent Resource Hogging: Mencegah memory leak atau infinite loop menghabiskan semua resource

2. Apa perbedaan VM dan container dalam konteks isolasi resource?
   VM: Menggunakan hypervisor untuk membuat isolasi penuh dengan virtual hardware. Setiap VM menjalankan OS lengkap, sehingga overhead lebih besar tetapi isolasi lebih kuat.
   Container: Menggunakan cgroups (control groups) untuk membatasi resource dan namespaces untuk isolasi process. Lebih ringan karena sharing kernel, tetapi isolasi tidak sekuat VM.

3. [Pertanyaan 3]  
   Dampak limit memori terhadap aplikasi yang boros memori:
Dampak Langsung:
- OOM Kill: Jika aplikasi mencoba mengalokasikan memori melebihi limit, kernel akan menghentikan container dengan OOM (Out of Memory) killer
- Performance Degradation: Aplikasi mungkin mengalami swap (jika diizinkan), yang sangat memperlambat performa
- Application Crash: Aplikasi dapat crash dengan error MemoryError atau equivalent

Dampak pada Behavior Aplikasi:
- Garbage Collection Pressure: Pada aplikasi dengan GC (Java, Python), GC akan lebih sering berjalan, mengurangi throughput
- Failed Operations: Operasi yang membutuhkan memory allocation (loading data, caching) akan gagal
- Degraded Functionality: Fitur tertentu mungkin tidak berfungsi atau dibatasi

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? mumet 
- Bagaimana cara Anda mengatasinya?  liburan

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
