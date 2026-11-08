def semak_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif")
    return umur

try:
    semak_umur(-5)
except ValueError as e:
    print("Ralat:", e)
