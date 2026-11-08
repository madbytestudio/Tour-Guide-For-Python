# Bab 24 — __init__, self, Properties dan Methods

Folder ini mengandungi kod untuk Bab 24 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_init.py` | `__init__` |
| `02_self.py` | `self` |
| `03_properties.py` | Ubah/tambah/padam attribute |
| `04_methods.py` | Method mengira |
| `05_default.py` | Default parameter |
| `06_apa_output.py` | Rujukan object |
| `07_projek_v24.py` | Class Pelajar lengkap |

## Cara jalankan

```powershell
cd Bab24
python 01_init.py
```

Atau dari folder utama repo:

```powershell
python Bab24\01_init.py
```

## Nota

`__init__` dijalankan automatik semasa object dicipta. `self` merujuk kepada
object semasa. `p2 = p1` tidak menyalin object; kedua-duanya merujuk object yang
sama.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab24> python 07_projek_v24.py
Nama   : Aiman Hakim
Kursus : Diploma Sains Komputer
Markah : 85.5
Gred   : A
---
Nama   : Siti Aminah
Kursus : Diploma Teknologi Maklumat
Markah : 90.0
Gred   : A
```
