# Bab 5 — Strings dan Pemprosesan Teks

Folder ini mengandungi kod untuk Bab 5 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan | Output |
|---|---|---|
| `01_strings.py` | Cipta string, indeks, `len()` | Aksara dan panjang |
| `02_slicing.py` | Slicing positif, negatif, step | Potongan string |
| `03_modify.py` | `upper()`, `lower()`, `strip()`, `replace()` | Teks yang diubah |
| `04_concat.py` | Gabung string dengan `+` | Nama penuh |
| `05_format.py` | f-string dan `.format()` | Teks diformat |
| `06_escape.py` | `\n`, `\t`, `\"`, `\\` | Output berbilang baris |
| `07_methods.py` | `count()`, `find()`, `startswith()` | Carian dan semakan |
| `08_apa_output.py` | Latihan slicing | Empat baris output |
| `09_projek_v5.py` | Bersih dan format data pelajar | Laporan pelajar |

## Cara jalankan

```powershell
cd Bab05
python 01_strings.py
```

Atau dari folder utama repo:

```powershell
python Bab05\01_strings.py
```

## Nota

String ialah immutable. Method string mengembalikan string baharu; ia tidak
mengubah string asal. Jika anda mahu menyimpan hasilnya, assign semula:

```python
nama = nama.strip().title()
```

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab05> python 09_projek_v5.py
===================================
SISTEM ANALISIS KEPUTUSAN PELAJAR
===================================
Nama   : Aiman Hakim
Kursus : Diploma Sains Komputer
Bilangan aksara nama: 11
```
