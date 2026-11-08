# Bab 32 — NumPy dan Pandas

Folder ini mengandungi kod untuk Bab 32 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_numpy.py` | Array dan statistik |
| `02_series.py` | Pandas Series |
| `03_dataframe.py` | DataFrame |
| `04_pandas_csv.py` | `read_csv()` |
| `05_apa_output.py` | Latihan NumPy/Pandas |
| `06_projek_v32.py` | Sort dan groupby |
| `pelajar.csv` | Data contoh |

## Cara jalankan

```powershell
cd Bab32
python 01_numpy.py
```

Atau dari folder utama repo:

```powershell
python Bab32\01_numpy.py
```

## Nota

NumPy menyediakan array berangka; Pandas menyediakan Series dan DataFrame.
`read_csv()` membaca fail CSV. `sort_values()` dan `groupby()` meringkaskan data.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab32> python 06_projek_v32.py
...
Purata keseluruhan: 85.5
Markah tertinggi: 90.0
...
kursus
DIT    90.00
DMM    78.50
DSC    86.75
```
