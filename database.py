import psycopg
from datetime import date

today = date.today()

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
            description VARCHAR(50),
            date DATE
        )
    """)


def add_expense(amount, category, description, today):
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        conn.execute(
            """
            INSERT INTO expense_tracker (price, category, description, date)
            VALUES (%s, %s, %s, %s)
            """,
            (amount, category, description, today)
        )
        
def show_expense():
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        print()
        print(f"{'ID':<5} {'PRICE':<10} {'CATEGORY':<15} {'DESCRIPTION':<20} {'DATE'}")
        print("-" * 60)

        for row in conn.execute("SELECT * FROM expense_tracker"):
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<15} {row[4]}")
            
def remove_expense(userdeleteid):
    with psycopg.connect(
            host="localhost",
            port=5432,
            dbname="anikettiwari",
            user="anikettiwari"
    ) as conn:
        conn.execute("DELETE FROM expense_tracker WHERE id = %s", (userdeleteid,))
        
def update_expensedb(userupdateid, amount, category, description):
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        conn.execute("UPDATE expense_tracker SET price = %s, category = %s, description = %s WHERE id = %s", (amount, category, description, userupdateid))
        print()
        print(f"{'ID':<5} {'PRICE':<10} {'CATEGORY':<15} {'DESCRIPTION':<20} {'DATE'}")
        print("-" * 60)
        for row in conn.execute("SELECT * FROM expense_tracker"):
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<15} {row[4]}")
            
def viewbyinc():
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        print()
        print(f"{'ID':<5} {'PRICE':<10} {'CATEGORY':<15} {'DESCRIPTION':<20} {'DATE'}")
        print("-" * 60)
        for row in conn.execute("SELECT * FROM expense_tracker ORDER BY id ASC"):
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<15} {row[4]}")
            
def viewbydesc():
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        print()
        print(f"{'ID':<5} {'PRICE':<10} {'CATEGORY':<15} {'DESCRIPTION':<20} {'DATE'}")
        print("-" * 60)
        for row in conn.execute("SELECT * FROM expense_tracker ORDER BY id DESC"):
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<15} {row[4]}")
            
def costsum():
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        total = conn.execute(
            "SELECT SUM(price) FROM expense_tracker"
        ).fetchone()[0]

        print(f"Total Expenses: ₹{total}")
        
def filterbyfood():
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        print()
        print(f"{'ID':<5} {'PRICE':<10} {'CATEGORY':<15} {'DESCRIPTION':<20} {'DATE'}")
        print("-" * 60)
        for row in conn.execute("SELECT * FROM expense_tracker WHERE category = 'Food'"):
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<15} {row[4]}")
            
def filterbytransport():
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        print()
        print(f"{'ID':<5} {'PRICE':<10} {'CATEGORY':<15} {'DESCRIPTION':<20} {'DATE'}")
        print("-" * 60)
        for row in conn.execute("SELECT * FROM expense_tracker WHERE category = 'Transport'"):
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<15} {row[4]}")
            
def filterbyshopping():
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        print()
        print(f"{'ID':<5} {'PRICE':<10} {'CATEGORY':<15} {'DESCRIPTION':<20} {'DATE'}")
        print("-" * 60)
        for row in conn.execute("SELECT * FROM expense_tracker WHERE category = 'Shopping'"):
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<15} {row[4]}")
            
def sortbyyear(yearstart, yearend):
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        print()
        print(f"{'ID':<5} {'PRICE':<10} {'CATEGORY':<15} {'DESCRIPTION':<20} {'DATE'}")
        print("-" * 60)
        for row in conn.execute("SELECT * FROM expense_tracker WHERE date BETWEEN '%s-01-01' AND '%s-12-30' ORDER BY date ASC", (yearstart, yearend)):
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<15} {row[4]}")

def sortbymonth(monthyearstart, montyearend, monthstart, monthend):
    start_date = f"{monthyearstart}-{monthstart:02d}-01"
    end_date = f"{montyearend}-{monthend:02d}-30"

    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        print()
        print(f"{'ID':<5} {'PRICE':<10} {'CATEGORY':<15} {'DESCRIPTION':<20} {'DATE'}")
        print("-" * 80)

        for row in conn.execute(
            """
            SELECT *
            FROM expense_tracker
            WHERE date BETWEEN %s AND %s
            ORDER BY date ASC
            """,
            (start_date, end_date)
        ):
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<15} {row[4]}")

def sortbydate(dateyearstart, dateyearend, datemonthstart, datemonthend, datestart, dateend):
    start_date = f"{dateyearstart}-{datemonthstart:02d}-{datestart:02d}"
    end_date = f"{dateyearend}-{datemonthend:02d}-{dateend:02d}"
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        print()
        print(f"{'ID':<5} {'PRICE':<10} {'CATEGORY':<15} {'DESCRIPTION':<20} {'DATE'}")
        print("-" * 80)
        
        for row in conn.execute(
            """
            SELECT *
            FROM expense_tracker
            WHERE date BETWEEN %s AND %s
            ORDER BY date ASC
            """,
            (start_date, end_date)
        ):
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<15} {row[4]}")
        
def keywordsearch(keyword):
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        for row in conn.execute(
                    """
                    SELECT *
                    FROM expense_tracker
                    WHERE description ILIKE %s
                    """,
                    (f"%{keyword}%",)
                ):
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<15} {row[4]}")