from flask import Flask
from flask import request
from classes import AppUsers, AppSecret


app = Flask(__name__)


@app.route("/users", methods=['GET'])
def test():
    # Ничего умнее не придумал чем IF
    # Но наверне как то надо чере try.
    # Как я не понял потому что  request.args.get ни какого экспешна не вовзращает.
    # Надо наверное завернуть в фугкцию и вовзращать экспшен если там не тот парметр пришел на вход?
    # Если да то как это сделать и в какой части кода.
    user_id = request.args.get('user_id')
    if type(user_id) is int:    
        return AppUsers.get_user(user_id)
    else:
        return f'надо было передать id пользователья параметром'


@app.route("/secret", methods=['GET'])
def get_secret():  
    secret_id = request.args.get('secret_id')
    return AppSecret.get_secret(secret_id)

if __name__ == "__main__":
    app.run()

#  return AppUsers.get_user(request.args.get('user_id'))