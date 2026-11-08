# Bab 1 — Pengenalan Python dan Persediaan Persekitaran

Folder ini mengandungi kod untuk Bab 1 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan | Output |
|---|---|---|
| `01_hello.py` | Program pertama: dua baris `print()` | `Hello, World!` dan salam |
| `02_sistem.py` | Banner Sistem Analisis Keputusan Pelajar | Banner versi 0.1 |
| `03_versi.py` | Semak interpreter, platform dan lokasi Python | Versi Python 3.12.x |
| `04_ralat_salah_eja.py` | **Sengaja salah** untuk latihan Spot the Bug | `SyntaxError` |
| `05_betulkan.py` | Versi betul untuk `04_ralat_salah_eja.py` | `Hello, World!` |
| `06_output.py` | Latihan “Apa Output Dia?” | Empat baris, satu kosong |

## Cara jalankan

```powershell
cd Bab01
python 01_hello.py
```

Atau dari folder utama repo:

```powershell
python Bab01\01_hello.py
```

## Amaran

`04_ralat_salah_eja.py` memang tidak boleh dijalankan. Ia digunakan untuk
mengajar cara membaca `SyntaxError`. Jangan betulkan fail itu sehingga anda
selesai mencuba latihan dalam buku.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab01> python 01_hello.py
Hello, World!
Selamat datang ke Tour Guide For Python.
```

Lokasi folder pada komputer anda mungkin berbeza. Yang penting, fail `.py`
berada dalam folder yang sama semasa anda menjalankan `python`.
