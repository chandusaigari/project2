from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import os
import time
import logging

app = Flask(__name__)
CORS(app)

# Setup logging
os.makedirs('/app/logs', exist_ok=True)
logging.basicConfig(
    filename='/app/logs/calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_db_connection():
    retries = 15
    delay = 4

    while retries > 0:
        try:
            print(f"🔄 Trying to connect to DB... ({retries} attempts left)")
            conn = mysql.connector.connect(
                host=os.environ.get('DB_HOST', 'mysql'),  # ← default mysql
                user=os.environ.get('DB_USER', 'db'),     # ← default db
                password=os.environ.get('DB_PASSWORD', 'db'),  # ← default db
                database=os.environ.get('DB_NAME', 'db'),      # ← default db
                connection_timeout=10,
                autocommit=True
            )
            if conn.is_connected():
                print("✅ Database connected successfully!")
                logging.info("Database connected successfully!")
                return conn
        except Error as e:
            print(f"❌ DB Error: {e}")
            logging.error(f"DB connection failed: {e}")
            retries -= 1
            time.sleep(delay)

    raise Exception("❌ Could not connect to database after all retries")


def init_db():
    """Create table if not exists"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS calculations (
                id INT AUTO_INCREMENT PRIMARY KEY,
                operand1 FLOAT NOT NULL,
                operand2 FLOAT NOT NULL,
                operator VARCHAR(10) NOT NULL,
                result FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Table ready!")
    except Exception as e:
        print(f"❌ Init DB error: {e}")
        logging.error(f"Init DB error: {e}")


@app.route('/health', methods=['GET'])
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({'status': 'ok', 'database': 'connected'})
    except Exception as e:
        return jsonify({'status': 'error', 'database': str(e)}), 500


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data received'}), 400

    num1 = data.get('num1')
    num2 = data.get('num2')
    operator = data.get('operator')

    # Validate
    if num1 is None or num2 is None or operator is None:
        return jsonify({'error': 'Missing parameters'}), 400

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': 'Invalid numbers'}), 400

    # Calculate
    result = None
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operator'}), 400

    # Save to DB
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO calculations (operand1, operand2, operator, result) VALUES (%s, %s, %s, %s)",
            (num1, num2, operator, result)
        )
        conn.commit()
        cursor.close()
        conn.close()
        logging.info(f"Saved: {num1} {operator} {num2} = {result}")
    except Exception as e:
        print(f"❌ Save error: {e}")
        logging.error(f"Save error: {e}")
        return jsonify({'error': f'Database error: {str(e)}'}), 500

    return jsonify({'result': result})


@app.route('/history', methods=['GET'])
def history():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM calculations ORDER BY created_at DESC LIMIT 10"
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        for row in rows:
            row['created_at'] = str(row['created_at'])

        return jsonify(rows)
    except Exception as e:
        print(f"❌ History error: {e}")
        logging.error(f"History error: {e}")
        return jsonify({'error': f'Database error: {str(e)}'}), 500


if __name__ == '__main__':
    print("⏳ Waiting for database...")
    time.sleep(10)
    init_db()
    print("🚀 Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)