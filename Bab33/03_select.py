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

kursor.execute("SELECT id, nama, kursus, markah FROM pelajar ORDER BY id")

for baris in kursor.fetchall():
    print(baris)

kursor.close()
cn.close()
