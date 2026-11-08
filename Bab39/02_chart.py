import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

nama = ["Aiman", "Siti", "Raj"]
markah = [85.5, 90.0, 78.5]

plt.bar(nama, markah)
plt.title("Markah Pelajar")
plt.xlabel("Pelajar")
plt.ylabel("Markah")
plt.savefig("fig_chart.png", dpi=150)
plt.close()

print("fig_chart.png disimpan.")
