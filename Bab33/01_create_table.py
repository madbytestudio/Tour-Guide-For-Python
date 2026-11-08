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

kursor.execute("DROP TABLE IF EXISTS pelajar")
kursor.execute("""
    CREATE TABLE pelajar (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(100) NOT NULL,
        kursus VARCHAR(100),
        markah FLOAT
    )
""")

print("Jadual pelajar dicipta.")
kursor.close()
cn.close()
