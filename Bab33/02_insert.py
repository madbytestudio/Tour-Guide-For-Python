import mysql.connector

konfigurasi = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "tourguide",
    "password": "tourguide123",
    "database": "tour_guide",
}

cn = mysql.connector.connect(**konfigurasi)
kursor = cn.cursor()

sql = "INSERT INTO pelajar (nama, kursus, markah) VALUES (%s, %s, %s)"
data = [
    ("Aiman Hakim", "Diploma Sains Komputer", 85.5),
    ("Siti Aminah", "Diploma Teknologi Maklumat", 90.0),
    ("Raj Kumar", "Diploma Multimedia", 78.5),
]

kursor.executemany(sql, data)
cn.commit()

print("Baris dimasukkan:", kursor.rowcount)
kursor.close()
cn.close()
