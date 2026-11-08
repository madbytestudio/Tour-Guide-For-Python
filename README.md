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
| 20 | [`Bab20`](Bab20/) | Modules, PIP dan virtual environment | Siap |
| 21 | [`Bab21`](Bab21/) | Dates dan math | Siap |
| 22 | [`Bab22`](Bab22/) | JSON dan regex | Siap |
| 23 | [`Bab23`](Bab23/) | OOP dan classes/objects | Siap |
| 24 | [`Bab24`](Bab24/) | init, self, properties dan methods | Siap |
| 25 | [`Bab25`](Bab25/) | Class methods dan magic methods | Siap |
| 26 | [`Bab26`](Bab26/) | Inheritance, polymorphism dan encapsulation | Siap |
| 27 | [`Bab27`](Bab27/) | Inner classes dan refactor projek | Siap |
| 28 | [`Bab28`](Bab28/) | File handling dan CSV | Siap |
| 29 | [`Bab29`](Bab29/) | Try/except dan custom exceptions | Siap |
| 30 | [`Bab30`](Bab30/) | Debugging dan testing | Siap |
| 31 | [`Bab31`](Bab31/) | Matplotlib dan visualisasi data | Siap |
| 32 | [`Bab32`](Bab32/) | NumPy dan Pandas | Siap |
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
├── Bab20/
│   ├── 01_module.py
│   ├── _my_module.py
│   ├── 02_own_module.py
│   ├── 03_import_ralat.py      # sengaja salah — NameError
│   ├── 04_import_betul.py
│   ├── 05_venv.py
│   ├── _projek_modul.py
│   ├── 06_projek_v20.py
│   └── README.md
├── Bab21/
│   ├── 01_datetime.py
│   ├── 02_timedelta.py
│   ├── 03_math.py
│   ├── 04_round.py
│   ├── 05_apa_output.py
│   ├── 06_projek_v21.py
│   └── README.md
├── Bab22/
│   ├── 01_json.py
│   ├── 02_json_types.py
│   ├── 03_regex.py
│   ├── 04_regex_patterns.py
│   ├── 05_apa_output.py
│   ├── 06_projek_v22.py
│   └── README.md
├── Bab23/
│   ├── 01_class.py
│   ├── 02_object.py
│   ├── 03_class_attr.py
│   ├── 04_method.py
│   ├── 05_isinstance.py
│   ├── 06_apa_output.py
│   ├── 07_projek_v23.py
│   └── README.md
├── Bab24/
│   ├── 01_init.py
│   ├── 02_self.py
│   ├── 03_properties.py
│   ├── 04_methods.py
│   ├── 05_default.py
│   ├── 06_apa_output.py
│   ├── 07_projek_v24.py
│   └── README.md
├── Bab25/
│   ├── 01_class_method.py
│   ├── 02_static_method.py
│   ├── 03_str.py
│   ├── 04_repr_eq.py
│   ├── 05_len_add.py
│   ├── 06_apa_output.py
│   ├── 07_projek_v25.py
│   └── README.md
├── Bab26/
│   ├── 01_inheritance.py
│   ├── 02_override.py
│   ├── 03_polymorphism.py
│   ├── 04_encapsulation.py
│   ├── 05_apa_output.py
│   ├── 06_projek_v26.py
│   └── README.md
├── Bab27/
│   ├── 01_inner.py
│   ├── 02_inner_instance.py
│   ├── 03_refactor.py
│   ├── 04_apa_output.py
│   ├── 05_projek_v27.py
│   └── README.md
├── Bab28/
│   ├── 01_write.py
│   ├── 02_read.py
│   ├── 03_read_lines.py
│   ├── 04_append.py
│   ├── 05_csv_write.py
│   ├── 06_csv_read.py
│   ├── 07_delete.py
│   ├── 08_apa_output.py
│   ├── 09_projek_v28.py
│   ├── data_contoh.txt
│   ├── pelajar.csv
│   └── README.md
├── Bab29/
│   ├── 01_try_except.py
│   ├── 02_multiple_except.py
│   ├── 03_else_finally.py
│   ├── 04_raise.py
│   ├── 05_custom_exception.py
│   ├── 06_apa_output.py
│   ├── 07_projek_v29.py
│   └── README.md
├── Bab30/
│   ├── 01_print_debug.py
│   ├── 02_assert.py
│   ├── 03_test_ringkas.py
│   ├── 04_bug.py             # sengaja salah — AssertionError
│   ├── 05_apa_output.py
│   ├── 06_projek_v30.py
│   └── README.md
├── Bab31/
│   ├── 01_line.py
│   ├── 02_bar.py
│   ├── 03_pie.py
│   ├── 04_hist.py
│   ├── 05_subplot.py
│   ├── 06_apa_output.py
│   ├── 07_projek_v31.py
│   └── README.md
├── Bab32/
│   ├── 01_numpy.py
│   ├── 02_series.py
│   ├── 03_dataframe.py
│   ├── 04_pandas_csv.py
│   ├── 05_apa_output.py
│   ├── 06_projek_v32.py
│   ├── pelajar.csv
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
