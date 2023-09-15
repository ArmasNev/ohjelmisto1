import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )
def getAirportByICAO(ICAO):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + ICAO + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f" This is {row[0]} at {row[1]} ")
    else:
        print("Virheellinen ICAO-koodi. Lentokenta ei löytynyt.")
    return
ICAO = input("Laita lentokentan ICAO-koodi: ").upper()
getAirportByICAO(ICAO)
