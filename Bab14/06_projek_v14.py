gred = "A"

match gred:
    case "A" | "B":
        status = "Cemerlang"
    case "C":
        status = "Baik"
    case "D" | "E":
        status = "Perlu bimbingan"
    case "F":
        status = "Gagal"
    case _:
        status = "Tiada data"

print("Gred:", gred)
print("Status:", status)
