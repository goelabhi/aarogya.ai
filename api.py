from fastapi import FastAPI
import sqlite3

from database import create_database

app = FastAPI(
    title="aarogya.ai API",
    description="Medicine access and pharmacy information API"
)

create_database()


@app.get("/pharmacies")
def get_pharmacies(
    medicine: str,
    location: str = "Mathura"
):
    conn = sqlite3.connect("aarogya.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            name,
            area,
            address,
            medicine,
            price,
            available,
            last_updated
        FROM pharmacies
        WHERE LOWER(medicine) = LOWER(?)
        AND LOWER(address) LIKE LOWER(?)
        AND available = 1
    """, (medicine, f"%{location}%"))

    results = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return {
        "medicine": medicine,
        "location": location,
        "count": len(results),
        "results": results
    }
