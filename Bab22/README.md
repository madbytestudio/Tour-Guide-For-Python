# Bab 22 — JSON dan Regular Expressions

Folder ini mengandungi kod untuk Bab 22 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_json.py` | `dumps()` dan `loads()` |
| `02_json_types.py` | Pemetaan jenis |
| `03_regex.py` | search/findall/sub/split |
| `04_regex_patterns.py` | Validasi kod dan emel |
| `05_apa_output.py` | Latihan JSON/regex |
| `06_projek_v22.py` | JSON pelajar dan validasi |

## Cara jalankan

```powershell
cd Bab22
python 01_json.py
```

Atau dari folder utama repo:

```powershell
python Bab22\01_json.py
```

## Nota

`json.dumps()` menghasilkan string JSON; `json.loads()` menukar string kepada
Python. Regex menggunakan raw string `r"..."`. `re.match()` bermula di awal
string; `re.search()` mencari di mana-mana.

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab22> python 06_projek_v22.py
[
  {
    "nama": "Aiman Hakim",
    "kod_kursus": "DSC-2026",
    "markah": 85.5
  },
  ...
]
Aiman Hakim - DSC-2026 - Sah: True
Siti Aminah - DIT-2026 - Sah: True
Raj Kumar - dm-26 - Sah: False
```
