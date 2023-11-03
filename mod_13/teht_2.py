import json
import mysql.connector
from flask import Flask, Response

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='',
    autocommit=True
)

app = Flask(__name__)

@app.route('/ICAO/<ICAO>')
def getAirportByICAO(ICAO):
    try:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
        cursor.execute(sql, (ICAO,))
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            response = []
            for row in result:
                airport_info = {
                    "ICAO": row['ident'],
                    "Name": row['name'],
                    "Location": row['municipality']
                }
                response.append(airport_info)
            return json.dumps(response)
        else:
            response = {
                "message": "ICAO not found",
                "status": 404
            }
            return Response(response=json.dumps(response), status=404, mimetype="application/json")
    except mysql.connector.Error as e:
        response = {
            "message": "Database error",
            "status": 500
        }
        return Response(response=json.dumps(response), status=500, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
