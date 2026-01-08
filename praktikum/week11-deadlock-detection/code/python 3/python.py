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

