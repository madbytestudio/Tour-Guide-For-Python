import os

with open("sementara.txt", "w", encoding="utf-8") as fail:
    fail.write("Fail sementara")

print("Sebelum:", os.path.exists("sementara.txt"))
os.remove("sementara.txt")
print("Selepas:", os.path.exists("sementara.txt"))
