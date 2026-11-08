# Bab 26 — Inheritance, Polymorphism dan Encapsulation

Folder ini mengandungi kod untuk Bab 26 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_inheritance.py` | `super().__init__` |
| `02_override.py` | Method override |
| `03_polymorphism.py` | Loop object berbeza |
| `04_encapsulation.py` | Private attribute + getter/setter |
| `05_apa_output.py` | Latihan inheritance |
| `06_projek_v26.py` | Hierarki pelajar |

## Cara jalankan

```powershell
cd Bab26
python 01_inheritance.py
```

Atau dari folder utama repo:

```powershell
python Bab26\01_inheritance.py
```

## Nota

`super().__init__` memanggil constructor induk. `__markah` bukan private
sepenuhnya; Python hanya melakukan name mangling. Gunakan getter/setter untuk
akses terkawal.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab26> python 06_projek_v26.py
Aiman Hakim - 85.5 - A
Siti Aminah - 90.0 - A - Biasiswa: Yayasan Pendidikan
```
