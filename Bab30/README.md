# Bab 30 — Debugging dan Testing

Folder ini mengandungi kod untuk Bab 30 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_print_debug.py` | Print debugging |
| `02_assert.py` | Assert lulus |
| `03_test_ringkas.py` | Test function |
| `04_bug.py` | **Sengaja salah** — `AssertionError` |
| `05_apa_output.py` | Latihan assert |
| `06_projek_v30.py` | Test projek |

## Cara jalankan

```powershell
cd Bab30
python 01_print_debug.py
```

Atau dari folder utama repo:

```powershell
python Bab30\01_print_debug.py
```

## Amaran

`04_bug.py` memang gagal dengan `AssertionError` kerana formula purata salah.
Ia digunakan untuk mengajar cara test menangkap pepijat.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab30> python 06_projek_v30.py
Uji purata: lulus
Uji gred: lulus
Semua ujian selesai
```
