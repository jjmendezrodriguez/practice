from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola, Flask!"

@app.route('/api/v1/clima', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    return jsonify({
        "city": city,
        "temperature": "20°C",
        "description": "Parcialmente nublado"
    })

if __name__ == '__main__':
    app.run(debug=True)
