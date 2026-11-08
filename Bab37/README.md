# Bab 37 — Capstone: Spesifikasi, Arkitektur dan Data Model

Folder ini mengandungi kod untuk Bab 37 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_model.py` | `@dataclass` Pelajar |
| `02_validation.py` | `__post_init__` |
| `03_apa_output.py` | Latihan dataclass |
| `04_projek_v37.py` | Rangka sistem |

## Cara jalankan

```powershell
cd Bab37
python 01_model.py
```

Atau dari folder utama repo:

```powershell
python Bab37\01_model.py
```

## Nota

Bab ini menetapkan spesifikasi dan data model. `@dataclass` mengurangkan
boilerplate; `__post_init__` digunakan untuk validation.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab37> python 04_projek_v37.py
Aiman Hakim - Diploma Sains Komputer - 85.5 - A
Siti Aminah - Diploma Teknologi Maklumat - 90.0 - A
```
