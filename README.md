# Tour Guide For Python — Kod Contoh

Kod contoh untuk buku **Tour Guide For Python: Dari Kosong ke Projek Sebenar**.

Repo ini disusun mengikut bab supaya pelajar boleh clone, buka folder bab,
dan copy-paste kod ke dalam projek sendiri.

## Keperluan

- Python **3.12.x** (disyorkan 3.12.10)
- Windows 10/11 (arahan buku ditulis untuk Windows)
- Visual Studio Code (disyorkan) + extension Python Microsoft

Semak versi Python:

```powershell
python --version
```

## Cara guna

Clone repo:

```powershell
git clone https://github.com/madbytestudio/Tour-Guide-For-Python.git
cd Tour-Guide-For-Python
```

Masuk ke folder bab dan jalankan fail:

```powershell
cd Bab01
python 01_hello.py
```

## Senarai bab

| Bab | Folder | Topik | Status |
|---:|---|---|---|
| 01 | [`Bab01`](Bab01/) | Pengenalan Python dan persediaan | Siap |
| 02 | [`Bab02`](Bab02/) | Sintaks, output dan comments | Siap |
| 03 | [`Bab03`](Bab03/) | Variables dan pengurusan nilai | Siap |
| ... | ... | ... | ... |
| 40 | `Bab40` | Capstone: testing, packaging, deployment | Akan datang |

## Struktur projek

```text
.
├── Bab01/
│   ├── 01_hello.py
│   ├── 02_sistem.py
│   ├── 03_versi.py
│   ├── 04_ralat_salah_eja.py   # sengaja salah — untuk latihan debugging
│   ├── 05_betulkan.py
│   ├── 06_output.py
│   └── README.md
├── Bab02/
│   ├── 01_statements.py
│   ├── 02_output.py
│   ├── 03_comments.py
│   ├── 04_indent_ralat.py      # sengaja salah — IndentationError
│   ├── 05_indent_betul.py
│   ├── 06_apa_output.py
│   ├── 07_banner_v2.py
│   └── README.md
├── Bab03/
│   ├── 01_variables.py
│   ├── 02_naming.py
│   ├── 03_nama_salah.py        # sengaja salah — SyntaxError
│   ├── 04_multiple.py
│   ├── 05_output.py
│   ├── 06_global.py
│   ├── 07_apa_output.py
│   ├── 08_banner_v3.py
│   └── README.md
├── projek/
│   └── README.md
├── requirements.txt
└── .gitignore
```

## Nota penting

- Fail `04_ralat_salah_eja.py` **sengaja** mengandungi ralat sintaks. Jangan
  betulkan terus jika anda sedang mengikuti bahagian **Spot the Bug**.
- Semua kod menggunakan standard library Python kecuali dinyatakan sebaliknya.
  Library tambahan akan dimasukkan dalam `requirements.txt` apabila bab
  berkaitan bermula.
- Kod dalam repo ini disusun untuk pembelajaran, bukan sebagai aplikasi
  production.

## Lesen

Belum ditetapkan. Sila hubungi pemilik repo sebelum mengedar semula.
