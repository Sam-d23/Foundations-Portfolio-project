from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        database='solar_monitoring',
        user='solar_user',
        password='securepassword'
    )

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    voltage = data['voltage']
    current = data['current']
    temperature = data['temperature']
    light_intensity = data['light_intensity']
    connection = get_db_connection()
    cursor = connection.cursor()
    sql_insert_query = """ INSERT INTO solar_data (voltage, current, temperature, light_intensity)
                           VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql_insert_query, (voltage, current, temperature, light_intensity))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

