# Data asal daripada teks (contohnya borang atau fail CSV).
nama_pelajar = "Aiman"
kursus = "Diploma Sains Komputer"
semester_teks = "3"
markah_teks = "85.5"

# Tukar teks kepada nombor yang boleh diproses.
semester = int(semester_teks)
markah = float(markah_teks)

print("Nama:", nama_pelajar)
print("Kursus:", kursus)
print("Semester:", semester)
print("Markah:", markah)
print("Jenis semester:", type(semester))
print("Jenis markah:", type(markah))
