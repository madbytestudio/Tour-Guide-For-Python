# Bab 28 — File Handling dan CSV

Folder ini mengandungi kod untuk Bab 28 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_write.py` | Tulis teks |
| `02_read.py` | Baca seluruh fail |
| `03_read_lines.py` | Baca baris |
| `04_append.py` | Tambah baris |
| `05_csv_write.py` | Tulis CSV |
| `06_csv_read.py` | Baca CSV |
| `07_delete.py` | Padam fail |
| `08_apa_output.py` | Latihan readlines |
| `09_projek_v28.py` | CSV pelajar |
| `data_contoh.txt` | Data contoh |
| `pelajar.csv` | Data CSV contoh |

## Cara jalankan

```powershell
cd Bab28
python 01_write.py
```

Atau dari folder utama repo:

```powershell
python Bab28\01_write.py
```

## Nota

Mod `w` menimpa fail; mod `a` menambah. Gunakan `encoding="utf-8"` dan
`newline=""` untuk CSV. `os.remove()` memadam fail tanpa pengesahan.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab28> python 09_projek_v28.py
Aiman Hakim - Diploma Sains Komputer - 85.5
Siti Aminah - Diploma Teknologi Maklumat - 90.0
Raj Kumar - Diploma Multimedia - 78.5
```
