import sqlite3 as sql

conn=sql.connect("/home/gabriel/prog/matrix/cows.db")
cursor=conn.cursor()


# Crea la db
def createDB():
    conn.commit()
    conn.close()


# Crea la tabla en la db
def createTable():
    cursor.execute(
        """CREATE TABLE milk (
            day INTEGER,
            vaca INTEGER,
            liters INTEGER
        )"""
    )
    conn.commit()
    conn.close()


# crea una fila en la db
def insertRowData(day, vaca, liters):
    sqlQuery = f"""INSERT INTO milk VALUES (
        {day},
        '{vaca}',
        '{liters}'
    )"""
    cursor.execute(sqlQuery)
    conn.commit()
    conn.close()


# Leer db y ordenar data
# fields === day, vaca, liters
def readOrdered(field):
    sqlQuery = f"""SELECT * FROM milk ORDER BY {field}"""
    cursor.execute(sqlQuery)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    for dato in datos:
        print(dato)



# CREATE DATABASE
#createDB()
# CREATE TABLE
#createTable()

# CREATE REGISTER
"""
day = input("Production Day (0 ~ n): ")
vaca = input("Cow: ")
liters = input("Cow Production: ")

insertRowData(day, vaca, liters)
"""

# GET DATA ORDER BY FIELD

field = input("Enter field to order (day, vaca or liters): ")
readOrdered(field)

