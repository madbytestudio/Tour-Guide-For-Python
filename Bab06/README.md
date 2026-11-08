# Bab 6 — Booleans dan Operators

Folder ini mengandungi kod untuk Bab 6 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan | Output |
|---|---|---|
| `01_booleans.py` | Boolean dan `bool()` | `True`/`False` |
| `02_arithmetic.py` | Tujuh operator arithmetic | Nombor |
| `03_assignment.py` | Assignment operators | Nilai `x` berubah |
| `04_comparison.py` | Comparison operators | Boolean |
| `05_logical.py` | `and`, `or`, `not` | Boolean |
| `06_identity_membership.py` | `is`, `in` | Boolean |
| `07_ternary.py` | Conditional expression | `Dewasa`, `Lulus` |
| `08_bitwise.py` | Bitwise operators | Integer |
| `09_precedence.py` | Precedence dan kurungan | Integer/boolean |
| `10_apa_output.py` | Latihan operator | Lima baris |
| `11_projek_v6.py` | Analisis markah pelajar | Jumlah, purata, peratus |

## Cara jalankan

```powershell
cd Bab06
python 01_booleans.py
```

Atau dari folder utama repo:

```powershell
python Bab06\01_booleans.py
```

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab06> python 11_projek_v6.py
Nama: Aiman
Jumlah: 255
Purata: 85.0
Peratus: 85.0
Lulus: True
```

## Nota

`is` menyemak identity objek, bukan kesamaan nilai. Gunakan `==` untuk
membandingkan nilai, dan gunakan `is` terutamanya dengan `None`.
