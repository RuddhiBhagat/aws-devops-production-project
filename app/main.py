from flask import Flask, jsonify
import psycopg2

from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


@app.route("/")
def home():
    return jsonify({
        "message": "AWS DevOps Project is running",
        "status": "success"
    })


@app.route("/health")
def health():
    try:
        connection = get_db_connection()
        connection.close()

        return jsonify({
            "status": "healthy",
            "database": "connected"
        })

    except Exception as error:
        return jsonify({
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)