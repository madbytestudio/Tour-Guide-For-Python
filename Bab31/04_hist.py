import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

markah = [55, 60, 65, 70, 70, 75, 80, 85, 85, 90, 95, 100]

plt.hist(markah, bins=5)
plt.title("Taburan Markah")
plt.xlabel("Julat Markah")
plt.ylabel("Bilangan Pelajar")
plt.savefig("fig_hist.png", dpi=150)
plt.close()

print("fig_hist.png disimpan.")
