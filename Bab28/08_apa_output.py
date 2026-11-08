with open("data_contoh.txt", "r", encoding="utf-8") as fail:
    baris = fail.readlines()

print(len(baris))
print(baris[0].strip())
print(baris[-1].strip())
