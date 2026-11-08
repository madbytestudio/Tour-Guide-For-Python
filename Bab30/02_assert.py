def kira_purata(markah):
    return sum(markah) / len(markah)

assert kira_purata([80, 90]) == 85
assert kira_purata([100]) == 100

print("Semua assert lulus")
