#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from app.db import db


class DataModel(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    alert = db.Column(db.String(3000))


    def __init__(self, alert):
        self.alert = alert

    def json(self):
        return {'data': self.alert}

    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()  

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

