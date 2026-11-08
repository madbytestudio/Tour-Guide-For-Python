import csv

with open("pelajar_baru.csv", "w", newline="", encoding="utf-8") as fail:
    penulis = csv.writer(fail)
    penulis.writerow(["nama", "kursus", "markah"])
    penulis.writerow(["Aiman", "DSC", 85.5])
    penulis.writerow(["Siti", "DIT", 90.0])

print("Fail pelajar_baru.csv ditulis.")
