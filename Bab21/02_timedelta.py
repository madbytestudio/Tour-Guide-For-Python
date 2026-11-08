from datetime import date, timedelta

tarikh = date(2026, 11, 8)
tujuh_hari = timedelta(days=7)

print("Tarikh asal:", tarikh)
print("Selepas 7 hari:", tarikh + tujuh_hari)
print("Sebelum 7 hari:", tarikh - tujuh_hari)
print("Beza hari:", (tarikh + tujuh_hari) - tarikh)
