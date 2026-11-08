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
| 11 | [`Bab11`](Bab11/) | Dictionaries | Siap |
| 12 | [`Bab12`](Bab12/) | Arrays, range dan iterators | Siap |
| 13 | [`Bab13`](Bab13/) | If, elif dan else | Siap |
| 14 | [`Bab14`](Bab14/) | Match | Siap |
| 15 | [`Bab15`](Bab15/) | While loops | Siap |
| 16 | [`Bab16`](Bab16/) | For loops | Siap |
| 17 | [`Bab17`](Bab17/) | Functions dan arguments | Siap |
| 18 | [`Bab18`](Bab18/) | args, kwargs, scope dan lambda | Siap |
| 19 | [`Bab19`](Bab19/) | Recursion, generators dan decorators | Siap |
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
├── Bab11/
│   ├── 01_dict.py
│   ├── 02_access.py
│   ├── 03_change.py
│   ├── 04_add.py
│   ├── 05_remove.py
│   ├── 06_loop.py
│   ├── 07_copy.py
│   ├── 08_nested.py
│   ├── 09_methods.py
│   ├── 10_apa_output.py
│   ├── 11_projek_v11.py
│   └── README.md
├── Bab12/
│   ├── 01_arrays.py
│   ├── 02_range.py
│   ├── 03_iterators.py
│   ├── 04_apa_output.py
│   ├── 05_iter_ralat.py       # sengaja salah — StopIteration
│   ├── 06_projek_v12.py
│   └── README.md
├── Bab13/
│   ├── 01_if.py
│   ├── 02_if_else.py
│   ├── 03_elif.py
│   ├── 04_shorthand.py
│   ├── 05_logical.py
│   ├── 06_nested.py
│   ├── 07_pass.py
│   ├── 08_apa_output.py
│   ├── 09_projek_v13.py
│   └── README.md
├── Bab14/
│   ├── 01_match.py
│   ├── 02_default.py
│   ├── 03_combine.py
│   ├── 04_menu.py
│   ├── 05_apa_output.py
│   ├── 06_projek_v14.py
│   └── README.md
├── Bab15/
│   ├── 01_while.py
│   ├── 02_break.py
│   ├── 03_continue.py
│   ├── 04_else.py
│   ├── 05_input_loop.py
│   ├── 06_apa_output.py
│   ├── 07_projek_v15.py
│   └── README.md
├── Bab16/
│   ├── 01_for_list.py
│   ├── 02_range.py
│   ├── 03_break_continue.py
│   ├── 04_else.py
│   ├── 05_nested.py
│   ├── 06_apa_output.py
│   ├── 07_projek_v16.py
│   └── README.md
├── Bab17/
│   ├── 01_function.py
│   ├── 02_arguments.py
│   ├── 03_return.py
│   ├── 04_default.py
│   ├── 05_keyword.py
│   ├── 06_no_return.py
│   ├── 07_apa_output.py
│   ├── 08_projek_v17.py
│   └── README.md
├── Bab18/
│   ├── 01_args.py
│   ├── 02_kwargs.py
│   ├── 03_order.py
│   ├── 04_scope.py
│   ├── 05_global.py
│   ├── 06_lambda.py
│   ├── 07_apa_output.py
│   ├── 08_projek_v18.py
│   └── README.md
├── Bab19/
│   ├── 01_recursion.py
│   ├── 02_recursion_ralat.py   # sengaja salah — RecursionError
│   ├── 03_generator.py
│   ├── 04_generator_expr.py
│   ├── 05_decorator.py
│   ├── 06_apa_output.py
│   ├── 07_projek_v19.py
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
