def log(function):
    def wrapper(*args, **kwargs):
        print("Mula:", function.__name__)
        hasil = function(*args, **kwargs)
        print("Selesai:", function.__name__)
        return hasil
    return wrapper

@log
def tambah(a, b):
    return a + b

print(tambah(2, 3))
