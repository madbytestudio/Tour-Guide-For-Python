try:
    nilai = int("12")
    print(nilai * 2)
except ValueError:
    print("Ralat")
finally:
    print("Selesai")
