import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [60, 70, 75, 85, 90]

plt.plot(x, y, marker="o")
plt.title("Markah Mengikut Ujian")
plt.xlabel("Ujian")
plt.ylabel("Markah")
plt.grid(True)
plt.savefig("fig_line.png", dpi=150)
plt.close()

print("fig_line.png disimpan.")
