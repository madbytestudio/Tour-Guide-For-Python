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
| 04 | [`Bab04`](Bab04/) | Data types, numbers dan casting | Siap |
| 05 | [`Bab05`](Bab05/) | Strings dan pemprosesan teks | Siap |
| 06 | [`Bab06`](Bab06/) | Booleans dan operators | Siap |
| 07 | [`Bab07`](Bab07/) | User input, string formatting dan None | Siap |
| 08 | [`Bab08`](Bab08/) | Lists | Siap |
| 09 | [`Bab09`](Bab09/) | Tuples | Siap |
| 10 | [`Bab10`](Bab10/) | Sets | Siap |
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
├── Bab04/
│   ├── 01_types.py
│   ├── 02_numbers.py
│   ├── 03_casting.py
│   ├── 04_cast_error.py        # sengaja salah — ValueError
│   ├── 05_cast_betul.py
│   ├── 06_apa_output.py
│   ├── 07_projek_v4.py
│   └── README.md
├── Bab05/
│   ├── 01_strings.py
│   ├── 02_slicing.py
│   ├── 03_modify.py
│   ├── 04_concat.py
│   ├── 05_format.py
│   ├── 06_escape.py
│   ├── 07_methods.py
│   ├── 08_apa_output.py
│   ├── 09_projek_v5.py
│   └── README.md
├── Bab06/
│   ├── 01_booleans.py
│   ├── 02_arithmetic.py
│   ├── 03_assignment.py
│   ├── 04_comparison.py
│   ├── 05_logical.py
│   ├── 06_identity_membership.py
│   ├── 07_ternary.py
│   ├── 08_bitwise.py
│   ├── 09_precedence.py
│   ├── 10_apa_output.py
│   ├── 11_projek_v6.py
│   └── README.md
├── Bab07/
│   ├── 01_input.py
│   ├── 02_input_nombor.py
│   ├── 03_input_float.py
│   ├── 04_format_spec.py
│   ├── 05_none.py
│   ├── 06_none_check.py
│   ├── 07_apa_output.py
│   ├── 08_input_ralat.py       # sengaja salah — ValueError
│   ├── 09_projek_v7.py
│   └── README.md
├── Bab08/
│   ├── 01_lists.py
│   ├── 02_access.py
│   ├── 03_change.py
│   ├── 04_add.py
│   ├── 05_remove.py
│   ├── 06_loop.py
│   ├── 07_comprehension.py
│   ├── 08_sort.py
│   ├── 09_copy.py
│   ├── 10_join.py
│   ├── 11_apa_output.py
│   ├── 12_projek_v8.py
│   └── README.md
├── Bab09/
│   ├── 01_tuples.py
│   ├── 02_access.py
│   ├── 03_update.py
│   ├── 04_unpack.py
│   ├── 05_loop.py
│   ├── 06_join.py
│   ├── 07_methods.py
│   ├── 08_apa_output.py
│   ├── 09_projek_v9.py
│   └── README.md
├── Bab10/
│   ├── 01_sets.py
│   ├── 02_access.py
│   ├── 03_add.py
│   ├── 04_remove.py
│   ├── 05_join.py
│   ├── 06_frozenset.py
│   ├── 07_methods.py
│   ├── 08_apa_output.py
│   ├── 09_projek_v10.py
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
