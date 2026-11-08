# Bab 11 — Dictionaries

Folder ini mengandungi kod untuk Bab 11 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_dict.py` | Cipta dictionary |
| `02_access.py` | `[]`, `get()`, keys/values |
| `03_change.py` | Ubah nilai dan `update()` |
| `04_add.py` | Tambah key |
| `05_remove.py` | `pop()`, `popitem()`, `del`, `clear()` |
| `06_loop.py` | Loop keys/values/items |
| `07_copy.py` | Copy vs reference |
| `08_nested.py` | Nested dictionary |
| `09_methods.py` | `get()`, `setdefault()` |
| `10_apa_output.py` | Latihan dictionary |
| `11_projek_v11.py` | List of dictionaries |

## Cara jalankan

```powershell
cd Bab11
python 01_dict.py
```

Atau dari folder utama repo:

```powershell
python Bab11\01_dict.py
```

## Nota

`[]` menghasilkan `KeyError` jika key tiada; `get()` mengembalikan `None` atau
nilai lalai. Assignment `b = a` tidak menyalin dictionary; gunakan `a.copy()`.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab11> python 11_projek_v11.py
===================================
SISTEM ANALISIS KEPUTUSAN PELAJAR
===================================
Bilangan pelajar: 3

Nama   : Aiman Hakim
Kursus : Diploma Sains Komputer
Markah : 85.5
---
Nama   : Siti Aminah
Kursus : Diploma Teknologi Maklumat
Markah : 90.0
---
Nama   : Raj Kumar
Kursus : Diploma Multimedia
Markah : 78.5
---
```
