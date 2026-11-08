def bubble_sort(data):
    data = data.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def selection_sort(data):
    data = data.copy()
    for i in range(len(data)):
        minimum = i
        for j in range(i + 1, len(data)):
            if data[j] < data[minimum]:
                minimum = j
        data[i], data[minimum] = data[minimum], data[i]
    return data

def insertion_sort(data):
    data = data.copy()
    for i in range(1, len(data)):
        kunci = data[i]
        j = i - 1
        while j >= 0 and data[j] > kunci:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = kunci
    return data

markah = [85, 70, 95, 60, 80]

print(bubble_sort(markah))
print(selection_sort(markah))
print(insertion_sort(markah))
