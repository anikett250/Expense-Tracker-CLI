import psycopg

with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="anikettiwari",
    user="anikettiwari"
) as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expense_tracker (
            id SERIAL PRIMARY KEY,
            price INT,
            category VARCHAR(15),
            description VARCHAR(50)
        )
    """)


def add_expense(amount, category, description):
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        conn.execute(
            """
            INSERT INTO expense_tracker (price, category, description)
            VALUES (%s, %s, %s)
            """,
            (amount, category, description)
        )
        
def show_expense():
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        print(f"{'ID':<5} {'PRICE':<10} {'CATEGORY':<15} {'DESCRIPTION'}")
        print("-" * 60)

        for row in conn.execute("SELECT * FROM expense_tracker"):
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]}")
            
def remove_expense(userdeleteid):
    with psycopg.connect(
            host="localhost",
            port=5432,
            dbname="anikettiwari",
            user="anikettiwari"
    ) as conn:
        conn.execute("DELETE FROM expense_tracker WHERE id = %s", (userdeleteid,))