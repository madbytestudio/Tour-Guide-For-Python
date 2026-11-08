import mysql.connector

konfigurasi = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "tourguide",
    "password": "tourguide123",
    "database": "tour_guide",
}

def sambung():
    return mysql.connector.connect(**konfigurasi)

def sediakan_jadual():
    cn = sambung()
    kursor = cn.cursor()
    kursor.execute("DROP TABLE IF EXISTS pelajar_projek")
    kursor.execute("""
        CREATE TABLE pelajar_projek (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(100) NOT NULL,
            kursus VARCHAR(100),
            markah FLOAT
        )
    """)
    cn.commit()
    kursor.close()
    cn.close()

def tambah_pelajar(nama, kursus, markah):
    cn = sambung()
    kursor = cn.cursor()
    kursor.execute(
        "INSERT INTO pelajar_projek (nama, kursus, markah) VALUES (%s, %s, %s)",
        (nama, kursus, markah),
    )
    cn.commit()
    kursor.close()
    cn.close()

def laporan():
    cn = sambung()
    kursor = cn.cursor()
    kursor.execute("SELECT nama, kursus, markah FROM pelajar_projek ORDER BY markah DESC")
    for nama, kursus, markah in kursor.fetchall():
        print(f"{nama} - {kursus} - {markah}")
    kursor.close()
    cn.close()

sediakan_jadual()
tambah_pelajar("Aiman Hakim", "Diploma Sains Komputer", 85.5)
tambah_pelajar("Siti Aminah", "Diploma Teknologi Maklumat", 90.0)
tambah_pelajar("Raj Kumar", "Diploma Multimedia", 78.5)

print("=== LAPORAN PELAJAR ===")
laporan()
