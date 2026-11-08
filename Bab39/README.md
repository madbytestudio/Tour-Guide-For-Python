# Bab 39 — Capstone: Visualisasi, CLI dan Persistence

Folder ini mengandungi kod untuk Bab 39 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `_app.py` | Model, sistem, storage |
| `01_persistence.py` | JSON save/load |
| `02_chart.py` | Carta bar |
| `03_cli.py` | CLI laporan |
| `04_apa_output.py` | Latihan JSON |
| `05_projek_v39.py` | Integrasi penuh |

## Cara jalankan

```powershell
cd Bab39
python 03_cli.py
python 03_cli.py carta
```

Atau dari folder utama repo:

```powershell
python Bab39\03_cli.py
```

## Nota

`argparse` mengendalikan command. JSON menyimpan data; Matplotlib menghasilkan
carta. Jika `data_pelajar.json` tiada, CLI menggunakan data contoh.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab39> python 05_projek_v39.py
=== LAPORAN ===
Siti Aminah - Diploma Teknologi Maklumat - 90.0 - A - Lulus
...
Purata: 84.66666666666667
Carta projek disimpan.
```
