# Bab 7 — User Input, String Formatting dan None

Folder ini mengandungi kod untuk Bab 7 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan | Output |
|---|---|---|
| `01_input.py` | Input nama | Sapaan |
| `02_input_nombor.py` | Casting input kepada `int` | Umur dan tahun lahir |
| `03_input_float.py` | Casting input kepada `float` | Markah + 5 |
| `04_format_spec.py` | Format specifier | Markah, peratus, harga, alignment |
| `05_none.py` | Nilai `None` | `None`, `NoneType`, boolean |
| `06_none_check.py` | Semakan `is None` | `Belum diisi` |
| `07_apa_output.py` | Latihan format | Empat baris |
| `08_input_ralat.py` | **Sengaja salah** | `ValueError` |
| `09_projek_v7.py` | Laporan daripada input | Laporan pelajar |

Fail `.in` mengandungi input automatik untuk contoh yang memerlukan `input()`.

## Cara jalankan

```powershell
cd Bab07
python 01_input.py
```

Atau dari folder utama repo:

```powershell
python Bab07\01_input.py
```

## Amaran

`08_input_ralat.py` memang menghasilkan `ValueError` apabila input bukan nombor.
Pengendalian input tidak sah secara menyeluruh akan diajar dalam Bab 29
(`try...except`).

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab07> python 09_projek_v7.py
Masukkan nama pelajar:
Masukkan kursus:
Masukkan semester:
Masukkan markah:
===================================
SISTEM ANALISIS KEPUTUSAN PELAJAR
===================================
Nama     : Aiman Hakim
Kursus   : Diploma Sains Komputer
Semester : 3
Markah   : 85.50
Status   : Lulus
```
