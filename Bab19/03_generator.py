def nombor(n):
    for i in range(n):
        yield i

for nilai in nombor(3):
    print(nilai)

gen = nombor(3)
print(next(gen))
print(next(gen))
