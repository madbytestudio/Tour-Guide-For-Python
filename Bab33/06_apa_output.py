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

kursor.execute("SELECT COUNT(*) FROM pelajar")
print("Bilangan pelajar:", kursor.fetchone()[0])

kursor.execute("SELECT AVG(markah) FROM pelajar")
print("Purata markah:", kursor.fetchone()[0])

kursor.close()
cn.close()
