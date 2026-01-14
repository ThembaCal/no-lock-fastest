import sqlite3




def create_db():
    conn = sqlite3.connect('data/cars.db')
    c = conn.cursor()
    # 
    c.execute("""
        CREATE TABLE Cars(
            id INTEGER PRIMARY KEY,
            'Vehicle Name' TEXT,
            'Vehicle Class' TEXT,
            'Top Speed (mph)' TEXT,
            'Price ($)' TEXT
        )
    """)
    conn.commit()
    conn.close()

create_db()