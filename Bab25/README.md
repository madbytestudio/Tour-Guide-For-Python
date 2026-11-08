# Bab 25 — Class Methods dan Magic Methods

Folder ini mengandungi kod untuk Bab 25 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_class_method.py` | `@classmethod` |
| `02_static_method.py` | `@staticmethod` |
| `03_str.py` | `__str__` |
| `04_repr_eq.py` | `__repr__`, `__eq__` |
| `05_len_add.py` | `__len__`, `__add__` |
| `06_apa_output.py` | Latihan `__str__` |
| `07_projek_v25.py` | Koleksi pelajar |

## Cara jalankan

```powershell
cd Bab25
python 01_class_method.py
```

Atau dari folder utama repo:

```powershell
python Bab25\01_class_method.py
```

## Nota

Class method menerima `cls`; static method tidak menerima `self` atau `cls`.
Magic methods membolehkan object berfungsi dengan `print()`, `len()`, `==`, dan
operator `+`.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab25> python 07_projek_v25.py
SenaraiPelajar dengan 2 pelajar
Bilangan: 2
Aiman (85.5)
Siti (90.0)
```
