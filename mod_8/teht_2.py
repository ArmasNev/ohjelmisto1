import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )
heli = 0
small_airport = 0
medium_airport = 0
large_airport = 0
closed = 0
seaplane_base = 0
def getAirportsByArea(code):
    global heli, small_airport, medium_airport, large_airport, closed, seaplane_base
    sql = "SELECT type  FROM airport "
    sql += " WHERE iso_country='" + code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            airport_type = row[0]  # Extract the airport type from the result
            if airport_type == 'heliport':
                heli += 1
            elif airport_type == 'small_airport':
                small_airport += 1
            elif airport_type == 'medium_airport':
                medium_airport += 1
            elif airport_type == 'large_airport':
                large_airport += 1
            elif airport_type == 'closed':
                closed += 1
            elif airport_type == 'seaplane_base':
                seaplane_base += 1


    else:
        print("Virheellinen maakoodi. Lentokentat ei löytynyt.")
    return
code = input("Laita maakoodi: ").upper()
getAirportsByArea(code)
print(f"Small airport: {small_airport}. \n"
      f"Medium airport: {medium_airport}. \n"
      f"Large airport: {large_airport}. \n"
      f"Heliport: {heli}. \n"
      f"Seaplane base: {seaplane_base}. \n"
      f"Closed: {closed}.")
