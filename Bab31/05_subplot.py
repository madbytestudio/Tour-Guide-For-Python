import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

nama = ["Aiman", "Siti", "Raj"]
markah = [85.5, 90.0, 78.5]

fig, (atas, bawah) = plt.subplots(1, 2, figsize=(10, 4))

atas.bar(nama, markah)
atas.set_title("Markah")

bawah.pie(markah, labels=nama, autopct="%1.0f%%")
bawah.set_title("Peratus")

plt.tight_layout()
plt.savefig("fig_subplot.png", dpi=150)
plt.close()

print("fig_subplot.png disimpan.")
