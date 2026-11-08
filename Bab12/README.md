# Bab 12 — Arrays, Range dan Iterators

Folder ini mengandungi kod untuk Bab 12 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_arrays.py` | List sebagai array |
| `02_range.py` | `range()` dengan satu, dua, tiga argumen |
| `03_iterators.py` | `iter()` dan `next()` |
| `04_apa_output.py` | Latihan range |
| `05_iter_ralat.py` | **Sengaja salah** untuk `StopIteration` |
| `06_projek_v12.py` | Laporan bernombor |

## Cara jalankan

```powershell
cd Bab12
python 01_arrays.py
```

Atau dari folder utama repo:

```powershell
python Bab12\01_arrays.py
```

## Amaran

`05_iter_ralat.py` memang menghasilkan `StopIteration` kerana `next()` dipanggil
melebihi bilangan item. Loop `for` menangkap ralat ini secara automatik.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab12> python 06_projek_v12.py
Pelajar 1: Aiman (85.5)
Pelajar 2: Siti (90.0)
Pelajar 3: Raj (78.5)
```
