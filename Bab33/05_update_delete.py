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
    "UPDATE pelajar SET markah = %s WHERE nama = %s",
    (90.0, "Aiman Hakim"),
)
print("Baris dikemas kini:", kursor.rowcount)

kursor.execute("DELETE FROM pelajar WHERE nama = %s", ("Raj Kumar",))
print("Baris dipadam:", kursor.rowcount)

cn.commit()

kursor.execute("SELECT nama, markah FROM pelajar ORDER BY nama")
for baris in kursor.fetchall():
    print(baris)

kursor.close()
cn.close()
