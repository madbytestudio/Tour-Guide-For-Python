import csv

with open("pelajar.csv", "r", newline="", encoding="utf-8") as fail:
    pembaca = csv.reader(fail)
    for baris in pembaca:
        print(baris)
