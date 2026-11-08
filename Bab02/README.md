# Bab 2 — Sintaks, Output dan Comments

Folder ini mengandungi kod untuk Bab 2 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan | Output |
|---|---|---|
| `01_statements.py` | Statement, baris kosong, cetakan berbilang baris | Empat baris teks |
| `02_output.py` | Teks, nombor, baris kosong, `sep`, `end` | Pelbagai bentuk output |
| `03_comments.py` | Comment dan triple-quoted string | `Hello` dan `Selesai` |
| `04_indent_ralat.py` | **Sengaja salah** untuk latihan Spot the Bug | `IndentationError` |
| `05_indent_betul.py` | Versi betul untuk `04_indent_ralat.py` | Dua baris teks |
| `06_apa_output.py` | Latihan “Apa Output Dia?” | Empat baris output |
| `07_banner_v2.py` | Milestone banner sistem v0.2 | Banner dengan pemisah `|` |

## Cara jalankan

```powershell
cd Bab02
python 01_statements.py
```

Atau dari folder utama repo:

```powershell
python Bab02\01_statements.py
```

## Amaran

`04_indent_ralat.py` memang menghasilkan `IndentationError`. Ia digunakan untuk
mengajar cara membaca ralat indentation. Jangan betulkan fail itu sehingga anda
selesai mencuba latihan dalam buku.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab02> python 07_banner_v2.py
===================================
SISTEM ANALISIS KEPUTUSAN PELAJAR
Versi 0.2
===================================
Modul | Laporan Keputusan
Status | Sedia digunakan
```

Lokasi folder pada komputer anda mungkin berbeza. Yang penting, fail `.py`
berada dalam folder yang sama semasa anda menjalankan `python`.
