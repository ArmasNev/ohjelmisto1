import json

from flask import Flask, Response

app = Flask(__name__)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

@app.route('/primenumber/<int:number>')
def prime_number(number):
    try:
        num = int(number)
        if is_prime(num):
            response = {
                "number": num,
                "isPrime": True,
            }
        else:
            response = {
                "number": num,
                "isPrime": False,
            }
        return json.dumps(response)
    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        return Response(response=json.dumps(response), status=400, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
