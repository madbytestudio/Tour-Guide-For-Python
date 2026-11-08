def kira_purata(markah):
    print("DEBUG markah:", markah)
    print("DEBUG bilangan:", len(markah))
    return sum(markah) / len(markah)

print(kira_purata([80, 90, 100]))
