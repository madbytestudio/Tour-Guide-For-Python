# Bab 29 — Try/Except dan Custom Exceptions

Folder ini mengandungi kod untuk Bab 29 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_try_except.py` | `ZeroDivisionError` |
| `02_multiple_except.py` | Dua jenis exception |
| `03_else_finally.py` | `else` dan `finally` |
| `04_raise.py` | `raise ValueError` |
| `05_custom_exception.py` | `MarkahTidakSah` |
| `06_apa_output.py` | Latihan try/except |
| `07_projek_v29.py` | Validasi data |

## Cara jalankan

```powershell
cd Bab29
python 01_try_except.py
```

Atau dari folder utama repo:

```powershell
python Bab29\01_try_except.py
```

## Nota

Tangkap exception spesifik. Elakkan `except:` kosong. `finally` sentiasa
dijalankan. Custom exception mesti mewarisi `Exception`.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab29> python 07_projek_v29.py
Sah: 85.5
Tidak sah: -10 - Markah mesti antara 0 dan 100
Tidak sah: 150 - Markah mesti antara 0 dan 100
Tidak sah: abc - Markah mesti nombor
Sah: 90.0
```
