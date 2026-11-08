# Bab 40 — Capstone: Testing, Packaging dan Deployment

Folder ini mengandungi kod untuk Bab 40 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `_app.py` | Model, sistem, storage |
| `_tests.py` | Empat test function |
| `01_test.py` | Jalankan semua test |
| `02_package.py` | Semak versi Python dan library |
| `03_apa_output.py` | Latihan ringkasan |
| `04_projek_v40.py` | Integrasi akhir |

## Cara jalankan

```powershell
cd Bab40
python 01_test.py
python 04_projek_v40.py
```

Atau dari folder utama repo:

```powershell
python Bab40\01_test.py
```

## Nota

Test menggunakan `assert` dan mencipta sistem sendiri supaya tidak bergantung
pada state test lain. Untuk projek besar, gunakan `pytest`, coverage, dan CI.
Jangan simpan credential atau data peribadi dalam repo.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab40> python 04_projek_v40.py
=== LAPORAN AKHIR ===
Siti Aminah - 90.0 - A - Lulus
Aiman Hakim - 85.5 - A - Lulus
Raj Kumar - 78.5 - B - Lulus
Purata: 84.66666666666667
uji_tambah: lulus
uji_cari: lulus
uji_purata: lulus
uji_padam: lulus
APLIKASI SIAP
```

Fail: `data_final.json`, `fig_projek_v40.png`.
