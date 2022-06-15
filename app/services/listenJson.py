import json
from app.models.data import DataModel
import os

path=os.getcwd()


def JsonCall():
    f = open(path+'/alert.json')
    for x in f:
        data = json.loads(x)
        data = DataModel(alert=str(data))
        data.save_to_db()
    f.close()
    
