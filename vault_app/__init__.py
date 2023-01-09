# Код приложения на Flask
from flask import Flask
from config import Config
from vault_app.routes.index import bluprint as index_blueprint
from vault_app.routes.send_data import bluprint as send_data_blueprint
from vault_app.routes.login import bluprint as login_blueprint


app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(index_blueprint)
app.register_blueprint(send_data_blueprint)
app.register_blueprint(login_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
