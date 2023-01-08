# Код приложения на Flask
from flask import Flask
from config import Config
from vault_app.index.index import bluprint as index_blueprint


app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(index_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
