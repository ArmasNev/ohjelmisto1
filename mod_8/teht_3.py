import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )
def getAirportByICAO(ICAO):
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident='" + ICAO + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        return result
    else:
        print("Virheellinen ICAO-koodi. Lentokenta ei löytynyt.")
    return
ICAO = input("Laita lentokentan ICAO-koodi: ").upper()
Lentokennta1 = getAirportByICAO(ICAO)
ICAO = input("Laita lentokentan ICAO-koodi: ").upper()
Lentokennta2 = getAirportByICAO(ICAO)
print(f"Lentokenttien välisen etäisyys on: {int(distance.distance(Lentokennta1, Lentokennta2).km)} km.")
