# Bab 31 — Matplotlib dan Visualisasi Data

Folder ini mengandungi kod untuk Bab 31 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_line.py` | Carta garis |
| `02_bar.py` | Carta bar |
| `03_pie.py` | Carta pai |
| `04_hist.py` | Histogram |
| `05_subplot.py` | Dua carta |
| `06_apa_output.py` | Latihan data |
| `07_projek_v31.py` | Dua carta projek |

## Cara jalankan

```powershell
cd Bab31
python 01_line.py
```

Atau dari folder utama repo:

```powershell
python Bab31\01_line.py
```

## Nota

Skrip menggunakan backend `Agg` supaya carta disimpan ke fail tanpa membuka
tetingkap GUI. Setiap figura disimpan dengan `savefig()` dan ditutup dengan
`close()`.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab31> python 07_projek_v31.py
Dua figura projek disimpan.
```

Fail: `fig_projek_bar.png`, `fig_projek_pie.png`.
