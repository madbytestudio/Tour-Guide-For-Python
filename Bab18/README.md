# Bab 18 — *args, **kwargs, Scope dan Lambda

Folder ini mengandungi kod untuk Bab 18 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_args.py` | `*args` |
| `02_kwargs.py` | `**kwargs` |
| `03_order.py` | Campuran parameter |
| `04_scope.py` | Local vs global |
| `05_global.py` | `global` |
| `06_lambda.py` | Lambda dan sort key |
| `07_apa_output.py` | Latihan args |
| `08_projek_v18.py` | Profil dan purata |

## Cara jalankan

```powershell
cd Bab18
python 01_args.py
```

Atau dari folder utama repo:

```powershell
python Bab18\01_args.py
```

## Nota

`*args` mengumpul argument positional ke dalam tuple; `**kwargs` mengumpul
argument bernama ke dalam dictionary. Elakkan `global` jika return value boleh
digunakan.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab18> python 08_projek_v18.py
nama: Aiman Hakim
kursus: Diploma Sains Komputer
semester: 3
Purata: 85.0
```
