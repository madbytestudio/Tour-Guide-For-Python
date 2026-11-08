import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

gred = ["A", "B", "C", "D"]
bilangan = [12, 8, 5, 2]

plt.pie(bilangan, labels=gred, autopct="%1.0f%%")
plt.title("Taburan Gred")
plt.savefig("fig_pie.png", dpi=150)
plt.close()

print("fig_pie.png disimpan.")
