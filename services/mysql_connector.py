import mysql.connector

mydb = mysql.connector.connect(
    host="mysql",
    user="root",
    password="pwd",
    port=3306,
    database="mydb"
)

def init_table():
  mycursor = mydb.cursor()

  mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  val = ("John", "Highway 21")
  mycursor.execute(sql, val)

  mydb.commit()

def select_table():
  cursor = mydb.cursor()

  cursor.execute("SELECT * FROM customers")

  return cursor.fetchall()
