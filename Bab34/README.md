# Bab 34 — MongoDB dengan Python

Folder ini mengandungi kod untuk Bab 34 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_connect.py` | Ping MongoDB |
| `02_insert.py` | `insert_many()` |
| `03_find.py` | `find()` |
| `04_query.py` | `$gte` dan sort |
| `05_update_delete.py` | Update dan delete |
| `06_apa_output.py` | Count dan find_one |
| `07_projek_v34.py` | Kelas CRUD |

## Prerequisites

- MongoDB berjalan pada `127.0.0.1:27017`
- `python -m pip install pymongo`

```powershell
python 01_connect.py
python 02_insert.py
python 03_find.py
```

## Nota

`_id` dijana secara automatik. Gunakan `{"_id": 0}` untuk menyembunyikannya.
Contoh ini tiada authentication; hanya untuk pembelajaran tempatan.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab34> python 07_projek_v34.py
=== LAPORAN PELAJAR ===
Siti Aminah - Diploma Teknologi Maklumat - 90.0
Aiman Hakim - Diploma Sains Komputer - 85.5
Raj Kumar - Diploma Multimedia - 78.5
Purata: 84.66666666666667
```
