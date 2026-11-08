# Bab 20 — Modules, PIP dan Virtual Environment

Folder ini mengandungi kod untuk Bab 20 buku **Tour Guide For Python**.

## Fail

| Fail | Tujuan |
|---|---|
| `01_module.py` | `math` dan `random` |
| `_my_module.py` | Helper module |
| `02_own_module.py` | Import module sendiri |
| `03_import_ralat.py` | **Sengaja salah** — `NameError` |
| `04_import_betul.py` | Import lengkap |
| `05_venv.py` | Semak prefix venv |
| `_projek_modul.py` | Module analisis projek |
| `06_projek_v20.py` | Import fungsi analisis |

## Cara jalankan

```powershell
cd Bab20
python 01_module.py
```

Atau dari folder utama repo:

```powershell
python Bab20\01_module.py
```

## PIP dan venv

```powershell
python -m pip --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python 05_venv.py
deactivate
```

Jika PowerShell menghalang activation, jalankan:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Output yang dijangka

```text
PS E:\TourGuidePython\Bab20> python 06_projek_v20.py
Purata: 84.66666666666667
Gred: A
```
