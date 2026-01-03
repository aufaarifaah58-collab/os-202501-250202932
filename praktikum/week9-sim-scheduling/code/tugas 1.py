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
