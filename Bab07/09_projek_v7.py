print("Masukkan nama pelajar:")
nama_mentah = input()

print("Masukkan kursus:")
kursus_mentah = input()

print("Masukkan semester:")
semester_teks = input()

print("Masukkan markah:")
markah_teks = input()

nama = nama_mentah.strip().title()
kursus = kursus_mentah.strip().title()
semester = int(semester_teks)
markah = float(markah_teks)
status = "Lulus" if markah >= 60 else "Gagal"

print("===================================")
print("SISTEM ANALISIS KEPUTUSAN PELAJAR")
print("===================================")
print(f"Nama     : {nama}")
print(f"Kursus   : {kursus}")
print(f"Semester : {semester}")
print(f"Markah   : {markah:.2f}")
print(f"Status   : {status}")
