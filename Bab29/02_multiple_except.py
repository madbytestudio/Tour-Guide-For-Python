def tukar(nilai):
    try:
        angka = int(nilai)
        print(10 / angka)
    except ValueError:
        print("Bukan nombor yang sah.")
    except ZeroDivisionError:
        print("Tidak boleh bahagi dengan sifar.")

tukar("abc")
tukar("0")
tukar("5")
