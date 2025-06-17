from flask import Flask
import os
app = Flask(__name__)

server_id = os.environ.get('SERVER_ID', 'Unknown')
@app.route('/')
def home():
    return f"<h1>Response from Backend Server: {server_id}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
