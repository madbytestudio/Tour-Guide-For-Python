import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

nama = ["Aiman", "Siti", "Raj"]
markah = [85.5, 90.0, 78.5]

plt.bar(nama, markah)
plt.title("Markah Pelajar")
plt.xlabel("Pelajar")
plt.ylabel("Markah")
plt.savefig("fig_projek_bar.png", dpi=150)
plt.close()

plt.pie(markah, labels=nama, autopct="%1.0f%%")
plt.title("Peratus Sumbangan Markah")
plt.savefig("fig_projek_pie.png", dpi=150)
plt.close()

print("Dua figura projek disimpan.")
