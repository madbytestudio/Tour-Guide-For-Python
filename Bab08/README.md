# Bab 8 — Lists

Folder ini mengandungi kod untuk Bab 8 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_lists.py` | Cipta list dan semak `type()` |
| `02_access.py` | Index, slice, membership, `count()`, `index()` |
| `03_change.py` | Ubah item dan slice |
| `04_add.py` | `append()`, `insert()`, `extend()` |
| `05_remove.py` | `remove()`, `pop()`, `del`, `clear()` |
| `06_loop.py` | Loop melalui list |
| `07_comprehension.py` | List comprehension |
| `08_sort.py` | `sort()` dan `reverse()` |
| `09_copy.py` | Copy vs reference |
| `10_join.py` | Gabung dengan `+` dan `extend()` |
| `11_apa_output.py` | Latihan mutasi |
| `12_projek_v8.py` | Senarai pelajar |

## Cara jalankan

```powershell
cd Bab08
python 01_lists.py
```

Atau dari folder utama repo:

```powershell
python Bab08\01_lists.py
```

## Nota

`for` loop dan list comprehension diperkenalkan sebagai pratonton. Penjelasan
penuh akan dibuat dalam Bab 16. Assignment `b = a` tidak menyalin list; gunakan
`a.copy()` untuk salinan bebas.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab08> python 12_projek_v8.py
===================================
SISTEM ANALISIS KEPUTUSAN PELAJAR
===================================
Bilangan pelajar: 3

Pelajar 1: Aiman Hakim | Diploma Sains Komputer | 85.5
Pelajar 2: Siti Aminah | Diploma Teknologi Maklumat | 90.0
Pelajar 3: Raj Kumar | Diploma Multimedia | 78.5
```
