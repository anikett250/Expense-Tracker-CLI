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
    conn.execute(
                """
                CREATE TABLE IF NOT EXISTS budget(
                    id SERIAL PRIMARY KEY,
                    amount INT NOT NULL
                )
                """
            )


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
        foodtotal = conn.execute(
            "SELECT SUM(price) FROM expense_tracker WHERE category = 'Food'"
        ).fetchone()[0]
        shoppingtotal = conn.execute(
            "SELECT SUM(price) FROM expense_tracker WHERE category = 'Shopping'"
        ).fetchone()[0]
        traveltotal = conn.execute(
            "SELECT SUM(price) FROM expense_tracker WHERE category = 'Travelling'"
        ).fetchone()[0]

        print(f"Total Expenses: ₹{total}")
        print(f"Total Food Expenses: ₹{foodtotal}")
        print(f"Total Shopping Expenses: ₹{shoppingtotal}")
        print(f"Total Travel Expenses: ₹{traveltotal}")
        
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
            
def monthspend(spendstartmonth, spendendmonth):
    startmonth = f"2026-{spendstartmonth:02d}-01"
    endmonth = f"2026-{spendendmonth:02d}-30"

    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:

        total = conn.execute(
            """
            SELECT SUM(price)
            FROM expense_tracker
            WHERE date BETWEEN %s AND %s
            """,
            (startmonth, endmonth)
        ).fetchone()[0]
        print()
        print(f"Total spending: ₹{total}")
        
def totalmonthspend():
    startmonth = f"2026-{today.month:02d}-01"
    endmonth = f"2026-{today.month:02d}-30"

    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:

        print()
        print(f"{'ID':<5} {'PRICE':<10} {'CATEGORY':<15} {'DESCRIPTION':<15} {'DATE'}")
        print("-" * 80)

        for row in conn.execute(
            """
            SELECT *
            FROM expense_tracker
            WHERE date BETWEEN %s AND %s
            ORDER BY date ASC
            """,
            (startmonth, endmonth)
        ):
            print(
                f"{row[0]:<5} {row[1]:<10} {row[2]:<15} "
                f"{row[3]:<15} {row[4]}"
            )

        total = conn.execute(
            """
            SELECT COALESCE(SUM(price), 0)
            FROM expense_tracker
            WHERE date BETWEEN %s AND %s
            """,
            (startmonth, endmonth)
        ).fetchone()[0]

        print(f"\nTotal Month Spending: ₹{total}")

def storebudget(budget):
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        conn.execute(
            """
            INSERT INTO budget (id, amount)
            VALUES (1, %s)
            ON CONFLICT (id)
            DO UPDATE SET amount = EXCLUDED.amount
            """,
            (budget,)
        )

def remainingbudget(budget):
    startmonth = f"2026-{today.month}-01"
    endmonth = f"2026-{today.month}-30"
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        total = conn.execute(
            """
            SELECT SUM(price) FROM expense_tracker WHERE date BETWEEN %s AND %s
            """, (startmonth, endmonth)
        ).fetchone()[0]
        remaining = budget - total
        print()
        print(f"Remaining Budget: ₹{remaining}")
        
def getbudget():
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="anikettiwari",
        user="anikettiwari"
    ) as conn:
        row = conn.execute(
            """
            SELECT amount
            FROM budget
            WHERE id = 1
            """
        ).fetchone()

        return row[0] if row else 0