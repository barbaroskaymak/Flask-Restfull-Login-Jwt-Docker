#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from app.services.listenJson import JsonCall
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from app.models.data import DataModel
from app.util.logz import create_logger

class DataList(Resource):
    def __init__(self):
         self.logger = create_logger()
    @jwt_required()
    def get(self):
        JsonCall()
        return {
            'data': [data.json() for data in DataModel.query.all()]} 