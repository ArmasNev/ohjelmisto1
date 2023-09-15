import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )
def getAirportsByArea(maakoodi):
    parametrit = (maakoodi, )
    sql = 'SELECT type, COUNT(*) AS count FROM airport WHERE iso_country = %s GROUP BY type;'
    kursor = connection.cursor(dictionary=True)
    kursor.execute(sql, parametrit)
    tulos = kursor.fetchall()
    return (tulos)

code = input("Laita maakoodi: ").upper()
kentat = getAirportsByArea(code)
for kentta in kentat:
    print(kentta['type'], kentta['count'])



