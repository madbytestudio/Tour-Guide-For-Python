# Bab 19 — Recursion, Generators dan Decorators

Folder ini mengandungi kod untuk Bab 19 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_recursion.py` | Factorial recursive |
| `02_recursion_ralat.py` | **Sengaja salah** — `RecursionError` |
| `03_generator.py` | `yield` dan `next()` |
| `04_generator_expr.py` | Generator expression |
| `05_decorator.py` | Decorator logging |
| `06_apa_output.py` | Latihan generator |
| `07_projek_v19.py` | Log dan laporan lazy |

## Cara jalankan

```powershell
cd Bab19
python 01_recursion.py
```

Atau dari folder utama repo:

```powershell
python Bab19\01_recursion.py
```

## Amaran

`02_recursion_ralat.py` memang menghasilkan `RecursionError` kerana tiada base
case. Jangan jalankan pada mesin yang kekurangan memori.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab19> python 07_projek_v19.py
[LOG] Menjalankan kira_purata
[LOG] Selesai kira_purata
Purata: 84.66666666666667
Aiman Hakim - 85.5
Siti Aminah - 90.0
Raj Kumar - 78.5
```
