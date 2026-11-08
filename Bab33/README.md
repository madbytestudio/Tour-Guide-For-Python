# Bab 33 — MySQL dengan Python

Folder ini mengandungi kod untuk Bab 33 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_create_table.py` | Cipta jadual |
| `02_insert.py` | Masukkan data |
| `03_select.py` | Baca data |
| `04_where.py` | Tapis data |
| `05_update_delete.py` | Kemas kini dan padam |
| `06_apa_output.py` | `COUNT` dan `AVG` |
| `07_projek_v33.py` | CRUD projek |

## Prerequisites

- MariaDB/MySQL berjalan pada `127.0.0.1:3307`
- Database `tour_guide`
- User `tourguide` / `tourguide123` (contoh tempatan)

```powershell
python -m pip install mysql-connector-python
python 01_create_table.py
python 02_insert.py
python 03_select.py
```

## Nota

Gunakan parameterized query `%s` untuk mengelakkan SQL injection. `commit()`
diperlukan selepas INSERT/UPDATE/DELETE. Jangan simpan credential sebenar
dalam repo.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab33> python 07_projek_v33.py
=== LAPORAN PELAJAR ===
Siti Aminah - Diploma Teknologi Maklumat - 90.0
Aiman Hakim - Diploma Sains Komputer - 85.5
Raj Kumar - Diploma Multimedia - 78.5
```
