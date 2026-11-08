# Bab 27 — Inner Classes dan Refactor Projek

Folder ini mengandungi kod untuk Bab 27 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_inner.py` | Inner class |
| `02_inner_instance.py` | Inner instance |
| `03_refactor.py` | Dua class bekerjasama |
| `04_apa_output.py` | Latihan inner class |
| `05_projek_v27.py` | Sistem analisis |

## Cara jalankan

```powershell
cd Bab27
python 01_inner.py
```

Atau dari folder utama repo:

```powershell
python Bab27\01_inner.py
```

## Nota

Inner class diakses melalui class luar, contohnya `Luar.Dalam()`. Composition
bermaksud “has-a”; inheritance bermaksud “is-a”. Uji output sebelum dan selepas
refactor.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab27> python 05_projek_v27.py
=== LAPORAN PELAJAR ===
Aiman Hakim - 85.5 - A
Siti Aminah - 90.0 - A
Raj Kumar - 78.5 - B
Bilangan pelajar: 3
Purata kelas: 84.66666666666667
```
