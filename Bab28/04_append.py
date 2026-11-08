with open("catatan.txt", "a", encoding="utf-8") as fail:
    fail.write("Baris ketiga\n")

with open("catatan.txt", "r", encoding="utf-8") as fail:
    print(fail.read())
