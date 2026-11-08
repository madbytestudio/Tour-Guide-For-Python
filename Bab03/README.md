# Bab 3 — Variables dan Pengurusan Nilai

Folder ini mengandungi kod untuk Bab 3 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan | Output |
|---|---|---|
| `01_variables.py` | Cipta variable dan semak `type()` | Nilai dan jenis data |
| `02_naming.py` | Nama deskriptif dan sensitiviti huruf | `Nama` dan `nama` berbeza |
| `03_nama_salah.py` | **Sengaja salah** untuk latihan Spot the Bug | `SyntaxError` |
| `04_multiple.py` | Multiple assignment | Tiga nilai, kemudian `0` tiga kali |
| `05_output.py` | Output dengan label dan `sep` | Profil ringkas |
| `06_global.py` | Variable global pada aras fail | Nama sistem dan versi |
| `07_apa_output.py` | Latihan “Apa Output Dia?” | `20` dan `5` |
| `08_banner_v3.py` | Milestone banner v0.3 | Data pelajar pertama |

## Cara jalankan

```powershell
cd Bab03
python 01_variables.py
```

Atau dari folder utama repo:

```powershell
python Bab03\01_variables.py
```

## Amaran

`03_nama_salah.py` memang menghasilkan `SyntaxError` kerana nama variable bermula
dengan nombor. Ia digunakan untuk mengajar cara membaca ralat nama variable.
Jangan betulkan fail itu sehingga anda selesai mencuba latihan dalam buku.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab03> python 08_banner_v3.py
===================================
SISTEM ANALISIS KEPUTUSAN PELAJAR
Versi: 0.3
===================================
Nama : Aiman
Kursus : Diploma Sains Komputer
Semester : 3
Markah : 85.5
```

Lokasi folder pada komputer anda mungkin berbeza. Yang penting, fail `.py`
berada dalam folder yang sama semasa anda menjalankan `python`.
