# Bab 4 — Data Types, Numbers dan Casting

Folder ini mengandungi kod untuk Bab 4 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan | Output |
|---|---|---|
| `01_types.py` | Lima jenis asas dan `type()` | `str`, `int`, `float`, `bool`, `NoneType` |
| `02_numbers.py` | Integer, float, complex | Nilai dan `.real`/`.imag` |
| `03_casting.py` | Casting asas | Nombor, teks, boolean |
| `04_cast_error.py` | **Sengaja salah** untuk Spot the Bug | `ValueError` |
| `05_cast_betul.py` | Casting yang sah | `123` dan jenis `int` |
| `06_apa_output.py` | Latihan “Apa Output Dia?” | `5`, `2.5`, `10` |
| `07_projek_v4.py` | Tukar data pelajar daripada teks | Data dengan jenis betul |

## Cara jalankan

```powershell
cd Bab04
python 01_types.py
```

Atau dari folder utama repo:

```powershell
python Bab04\01_types.py
```

## Amaran

`04_cast_error.py` memang menghasilkan `ValueError` kerana `"abc"` bukan nombor.
Ia digunakan untuk mengajar cara membaca ralat casting.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab04> python 07_projek_v4.py
Nama: Aiman
Kursus: Diploma Sains Komputer
Semester: 3
Markah: 85.5
Jenis semester: <class 'int'>
Jenis markah: <class 'float'>
```
