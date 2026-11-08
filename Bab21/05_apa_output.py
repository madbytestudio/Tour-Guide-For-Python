from datetime import date, timedelta
import math

tarikh = date(2026, 1, 1)

print(tarikh + timedelta(days=31))
print(tarikh.strftime("%d-%m-%Y"))
print(math.floor(9.9))
print(math.ceil(9.1))
