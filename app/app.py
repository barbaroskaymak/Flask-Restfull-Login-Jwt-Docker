#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from app.resources.data import DataList
from app.resources.user import UserRegister, User
from app.config import postgresqlConfig

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "SecretKey" 
jwt = JWTManager(app)
api = Api(app)


@app.before_first_request
def create_tables():
    from app.db import db
    db.init_app(app)
    db.create_all()



api.add_resource(DataList, '/data')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user')

if __name__ == '__main__':
    create_tables()
    print("çalıştı")
    app.run(host='0.0.0.0', port='5000',debug=True)
