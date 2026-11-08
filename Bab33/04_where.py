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

kursor.execute(
    "SELECT nama, markah FROM pelajar WHERE markah >= %s ORDER BY markah DESC",
    (80,),
)

for nama, markah in kursor.fetchall():
    print(nama, "-", markah)

kursor.close()
cn.close()
