from flask import Flask
from app.vetclinic.route.client_route import client_bp

app = Flask(__name__)
app.register_blueprint(client_bp)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)