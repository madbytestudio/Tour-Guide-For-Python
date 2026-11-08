import re

teks = "Hubungi 012-3456789 atau 019-8765432"

print(re.search(r"\d{3}-\d{7}", teks).group())
print(re.findall(r"\d{3}-\d{7}", teks))
print(re.sub(r"\d", "*", teks))
print(re.split(r"\s+", teks))
