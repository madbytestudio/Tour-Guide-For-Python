gred = "B"

match gred:
    case "A" | "B":
        print("Cemerlang")
    case "C":
        print("Sederhana")
    case "D" | "E":
        print("Perlu bimbingan")
    case _:
        print("Gagal atau tiada data")
