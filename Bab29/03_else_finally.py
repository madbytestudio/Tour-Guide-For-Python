try:
    angka = int("10")
except ValueError:
    print("Ralat")
else:
    print("Berjaya:", angka)
finally:
    print("Selesai")
