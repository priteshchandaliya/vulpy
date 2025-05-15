import sqlite3
import os
from flask import Flask, request

app = Flask(__name__)

# Hardcoded secret (insecure!)
DB_PASSWORD = "supersecretpassword123"

@app.route("/user")
def get_user():
    user_id = request.args.get('id')

    # SQL Injection Vulnerability
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return str(result)

@app.route("/run")
def run_command():
    cmd = request.args.get('cmd')

    # Command Injection Vulnerability
    os.system(cmd)
    return f"Executed command: {cmd}"

@app.route("/file")
def read_file():
    filename = request.args.get('file')

    # Path Traversal Vulnerability
    with open(f"./files/{filename}", "r") as f:
        content = f.read()
    return content

if __name__ == "__main__":
    app.run(debug=True)
