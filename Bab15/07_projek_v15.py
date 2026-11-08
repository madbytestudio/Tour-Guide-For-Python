while True:
    print("=== MENU ===")
    print("1. Papar banner")
    print("2. Papar versi")
    print("3. Keluar")
    print("Pilihan:")
    pilihan = input()

    match pilihan:
        case "1":
            print("SISTEM ANALISIS KEPUTUSAN PELAJAR")
        case "2":
            print("Versi 0.15")
        case "3":
            print("Keluar daripada sistem.")
            break
        case _:
            print("Pilihan tidak sah.")
