from flask import Flask, request, jsonify
import pymysql
import pymysql.cursors

app = Flask(__name__)

# Database configuration
DB_HOST = "192.168.59.13"
DB_USER = "flaskuser"
DB_PASSWORD = "flaskpass123"
DB_NAME = "flaskdb"

# Connect to the database
def get_db_connection():
    try:
        return pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.Cursor
        )
    except Exception as e:
        print("Database connection failed:", e)
        return None

# Create the table if it doesn't exist
def init_db():
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS votes (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        vote_option VARCHAR(10) NOT NULL
                    )
                """)
            conn.commit()
        finally:
            conn.close()

# Initialize the DB at startup
init_db()

# ✅ تم تعديل المسارات لتبدأ بـ /api
@app.route('/api/', methods=['GET'])
def index():
    conn = get_db_connection()
    votes = {"cat": 0, "dog": 0}
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT vote_option, COUNT(*) FROM votes GROUP BY vote_option")
                results = cursor.fetchall()
                for vote_option, count in results:
                    votes[vote_option] = count
        finally:
            conn.close()
    return jsonify(votes)

@app.route('/api/vote', methods=['POST'])
def vote():
    # يمكن التصويت عبر JSON أو query param
    option = request.json.get('vote') if request.is_json else request.args.get('vote')

    if option not in ['cat', 'dog']:
        return jsonify({"error": "Invalid vote option"}), 400

    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO votes (vote_option) VALUES (%s)", (option,))
            conn.commit()
        finally:
            conn.close()
    return jsonify({"message": "Vote submitted successfully", "vote": option}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
