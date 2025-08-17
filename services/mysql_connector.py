import mysql.connector


def init_db():
    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        password="pwd",
        port=3306
    )

    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS mydb")

    cursor.close()
    mydb.close()


def init_table():
    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        password="pwd",
        port=3306,
        database="mydb"
    )

    mycursor = mydb.cursor()

    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            address VARCHAR(255)
        )
    """)

    # Insert sample row
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()

    mycursor.close()
    mydb.close()


def select_table():
    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        password="pwd",
        port=3306,
        database="mydb"
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()

    cursor.close()
    mydb.close()
    return result



