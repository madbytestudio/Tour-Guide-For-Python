class MarkahTidakSah(Exception):
    pass

def semak_markah(markah):
    if not isinstance(markah, (int, float)):
        raise MarkahTidakSah("Markah mesti nombor")
    if markah < 0 or markah > 100:
        raise MarkahTidakSah("Markah mesti antara 0 dan 100")
    return markah

data = [85.5, -10, 150, "abc", 90.0]

for nilai in data:
    try:
        markah = semak_markah(nilai)
        print("Sah:", markah)
    except MarkahTidakSah as e:
        print("Tidak sah:", nilai, "-", e)
