from flask import request
from controllers.user import User
from helpers.helper import token_required

UserController = User()


def user_routes(app):
    @app.route('/users', methods=['POST'])
    @token_required
    def create_user():
        values = request.values
        UserController.username = values.get('username')
        UserController.password = values.get('password')
        UserController.name = values.get('name')
        UserController.last_name = values.get('last_name')
        UserController.age = values.get('age')
        return UserController.add_user(UserController, app)

    @app.route('/users/<id>', methods=['GET'])
    @token_required
    def get_user_by_id(id):
        return UserController.find_user(id, app)

    @app.route('/login', methods=['POST'])
    def login():
        values = request.values
        UserController.username = values.get('username')
        UserController.password = values.get('password')
        return UserController.login(UserController, app)
