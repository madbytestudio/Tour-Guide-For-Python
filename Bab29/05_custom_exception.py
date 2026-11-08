class MarkahTidakSah(Exception):
    pass

def semak_markah(markah):
    if markah < 0 or markah > 100:
        raise MarkahTidakSah("Markah mesti antara 0 dan 100")
    return markah

try:
    semak_markah(150)
except MarkahTidakSah as e:
    print("Ralat:", e)
