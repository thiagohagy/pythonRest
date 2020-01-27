import json
from pymongo import MongoClient

class Db():

  dbConn = []

  def __init__(self):
    # reding config file
    with open("config.json", "r") as f:
      config = json.load(f)

    # conectar à porta
    dbConn = MongoClient(config['dbPath'])
    # conectar ao db
    self.dbConn = dbConn[config['dbName']]


  def count(self, collection, filter = {}):
    resp = self.dbConn[collection].count(filter)
    return resp


  def find(self, collection, filter = {}):
    resp = self.dbConn[collection].find(filter, { "login": 1, "_id": 1, "email": 1, "name":1})

    newResp = [];
    for r in resp:
      r['_id'] = str(r['_id'])
      newResp.append(r)

    return newResp
