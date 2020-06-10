from models.user import User as UserModel
from helpers.helper import handler_response, jwt_secret
from bcrypt import hashpw, gensalt
from jwt import encode


class User:

    def add_user2(self, user, app):
        try:
            password = hashpw(user.password.encode('utf-8'), gensalt())
            UserModel.insert({
                'username': user.username,
                'password': password.decode('utf-8'),
                'full_name': user.full_name,
                'document_number': user.document_number
            })
            return handler_response(
                app, 201, f'Se creo el usuario {user.username}')
        except Exception as e:
            return handler_response(app, 500, str(e))

    def add_user(self, user, app):
        try:
            password = hashpw(user.password.encode('utf-8'), gensalt())
            UserModel.password = password.decode('utf-8')
            UserModel.save()
            return handler_response(
                app, 201, f'Se creo el usuario {user.username}')
        except Exception as e:
            return handler_response(app, 500, str(e))

    def login(self, user, app):
        try:
            user_found = UserModel.where_username(user.username).first()
            if user_found and user_found.password_valid(user.password):
                token = encode(
                    user_found.serialize(), jwt_secret(), algorithm='HS256')
                response = {
                    'token': token,
                    'user': user_found.serialize()
                }
                return handler_response(
                    app, 200, 'Logeado con exito', response)
            message = f'el usuario : {user.username}' \
                ' y/o la contraseña es incorrecta'
            return handler_response(app, 401, message)
        except Exception as error:
            return handler_response(app, 500, str(error))

    def find_user(self, user_id, app):
        try:
            user = UserModel.find(user_id)
            user = {
                'id': user.id,
                'username': user.username,
                'role_id': user.role.id,
                'role': user.role.name
            }
            return handler_response(
                app, 200, f'Datos Usuario {user_id}', True, user
            )
        except Exception as e:
            return handler_response(app, 501, str(e))
