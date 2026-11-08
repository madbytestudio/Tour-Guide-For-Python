# Bab 10 — Sets

Folder ini mengandungi kod untuk Bab 10 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_sets.py` | Cipta set dan buang duplicate |
| `02_access.py` | Membership dan loop |
| `03_add.py` | `add()` dan `update()` |
| `04_remove.py` | `remove()`, `discard()`, `pop()`, `clear()` |
| `05_join.py` | Union, intersection, difference |
| `06_frozenset.py` | Frozenset immutable |
| `07_methods.py` | `issubset()`, `issuperset()`, `isdisjoint()` |
| `08_apa_output.py` | Latihan set |
| `09_projek_v10.py` | Kursus unik |

## Cara jalankan

```powershell
cd Bab10
python 01_sets.py
```

Atau dari folder utama repo:

```powershell
python Bab10\01_sets.py
```

## Nota

Set tidak mempunyai index dan tidak menjamin urutan. Gunakan `sorted(set)`
apabila anda perlu memaparkan item dalam urutan yang stabil. `{}` ialah
dictionary kosong; gunakan `set()` untuk set kosong.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab10> python 09_projek_v10.py
Senarai asal: ['Python', 'SQL', 'Python', 'HTML', 'SQL', 'CSS']
Bilangan asal: 6
Kursus unik: ['CSS', 'HTML', 'Python', 'SQL']
Bilangan unik: 4
Kursus wajib: ['Python', 'SQL']
Semua wajib ada: True
```
