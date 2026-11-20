import sqlite3


DB_NAME = "aarogya.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pharmacies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            area TEXT NOT NULL,
            address TEXT NOT NULL,
            medicine TEXT NOT NULL,
            price REAL,
            available INTEGER NOT NULL,
            last_updated TEXT
        )
    """)

    pharmacies = [
        (
            "Jan Aushadhi Kendra",
            "Krishna Nagar",
            "Krishna Nagar, Mathura",
            "paracetamol",
            12,
            1,
            "2026-11-20"
        ),
        (
            "Apollo Pharmacy",
            "Dampier Nagar",
            "Dampier Nagar, Mathura",
            "paracetamol",
            25,
            1,
            "2026-11-20"
        ),
        (
            "MedPlus",
            "Maholi Road",
            "Maholi Road, Mathura",
            "paracetamol",
            22,
            1,
            "2026-11-20"
        ),
        (
            "Jan Aushadhi Kendra",
            "Dampier Nagar",
            "Dampier Nagar, Mathura",
            "metformin",
            18,
            1,
            "2026-11-20"
        ),
        (
            "Apollo Pharmacy",
            "Krishna Nagar",
            "Krishna Nagar, Mathura",
            "metformin",
            32,
            1,
            "2026-11-20"
        )
    ]

    cursor.executemany("""
        INSERT INTO pharmacies
        (name, area, address, medicine, price, available, last_updated)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, pharmacies)

    conn.commit()
    conn.close()
