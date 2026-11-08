# Bab 35 — Python Data Structures dan Algorithms

Folder ini mengandungi kod untuk Bab 35 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_stack.py` | Stack LIFO |
| `02_queue.py` | Queue FIFO |
| `03_linked_list.py` | Linked list |
| `04_binary_search.py` | Binary search |
| `05_sorting.py` | Bubble/selection/insertion |
| `06_apa_output.py` | Latihan stack |
| `07_projek_v35.py` | Carian dan peringkat |

## Cara jalankan

```powershell
cd Bab35
python 01_stack.py
```

Atau dari folder utama repo:

```powershell
python Bab35\01_stack.py
```

## Nota

Stack LIFO; queue FIFO. `deque.popleft()` cekap untuk queue. Binary search
memerlukan data tersusun. Gunakan `sorted()` untuk kerja sebenar.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab35> python 07_projek_v35.py
Carian Raj: {'nama': 'Raj', 'markah': 78.5}
Peringkat markah:
Siti - 90.0
Mei - 88.0
Aiman - 85.5
Raj - 78.5
```
