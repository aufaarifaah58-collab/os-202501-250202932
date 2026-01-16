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
