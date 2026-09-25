import sqlite3
from pathlib import Path

DB_PATH = Path("data/swim.db")


def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS swim_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            stroke TEXT NOT NULL,
            distance INTEGER NOT NULL,
            time_seconds REAL NOT NULL,
            stroke_count INTEGER,
            rpe INTEGER,
            note TEXT
        )
        """
    )

    conn.commit()
    conn.close()

def add_record(
    date,
    stroke,
    distance,
    time_seconds,
    stroke_count=None,
    rpe=None,
    note=None
):
    conn = sqlite3.connect(DB_PATH)

    conn.execute(
        """
        INSERT INTO swim_records (
            date,
            stroke,
            distance,
            time_seconds,
            stroke_count,
            rpe,
            note
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            date,
            stroke,
            distance,
            time_seconds,
            stroke_count,
            rpe,
            note
        )
    )

    conn.commit()
    conn.close()

def get_all_records():
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.execute(
        """
        SELECT
            id,
            date,
            stroke,
            distance,
            time_seconds,
            stroke_count,
            rpe,
            note
        FROM swim_records
        ORDER BY id
        """
    )

    records = cursor.fetchall()

    conn.close()

    return records