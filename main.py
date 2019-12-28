import json
from bson import BSON, json_util
from bson.objectid import ObjectId
from flask import Flask, request, jsonify
import pymongo
import datetime

mongodb = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongodb["th"]
collection = db["example"]

collection.create_index("createdAt", expireAfterSeconds=300)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return {'status': '200 ok', 'message': 'server is running, please visit route /values'}

@app.route("/values", methods=['GET'])
def get():
    response = {}
    args = request.args
    query = args.get('keys', default=None, type=None)

    if query == None:
        result = collection.aggregate([
            { "$group": { "_id": "$key", "data": { "$push": "$$ROOT" } } }
        ])

        for x in result:
            key = x['_id']
            # del x['data'][0]['key']
            response[key] = x['data']

    elif query != None:
        dbSKeys = query.split(',')
        dbFKey = []
        for key in dbSKeys:
            response[key] = []
            dbFKey.append(str(key))
        result = collection.find({"key" : {"$in" : dbFKey}})
        
        for doc in result:
            key = doc['key']
            response[key].append(doc)

    return json.dumps(response, sort_keys=True, indent=4, default=json_util.default)

@app.route("/values", methods=['PATCH'])
def patch():
    """
    update format:
    {
        "key1": {"id": "5e0592cc58c3c6474c62bfdd", "data": ["a","b","c"]}
    }
    """
    r = request.json

    if type(r) is dict:
        updateData = []

        for key in r:
            id = r[key]['id']
            data = r[key]['data']
            exists = collection.find_one({"_id" : ObjectId(id)})

            print(exists)

            if exists != None:
                updateData.append(pymongo.UpdateOne({ "_id": ObjectId(id)},{ "$set": { "data": data }},upsert=True))
            
        if len(updateData) > 0:
            saved = collection.bulk_write(updateData)
            saved_count = saved.modified_count

            if saved.modified_count > 0:
                return {"status": "%d data updated" %saved_count, "status_code": 201}
            elif saved.modified_count == 0:
                return {"status": "No data updated", "status_code": 302}
            else:
                return {"status": "cannot update", "status_code": 401}
        else:
            return {"error": "data doesn't exists"}
    else:
        return {"error": "format doesn't match!"}
        
@app.route("/values", methods=['POST'])
def post():
    """
        {
            "key1": 1234567890,
            "key2": "Just some string",
            "key3": ["Just", "some", "string"],
            "key4": [{"name": "unknown"}, ["a", "b", "c" ]],
            "key5": {"name": "anybody", "arrays": ["d","e"]}
        }
    """
    r = request.json
    if type(r) is dict:
        utc_timeStamp = datetime.datetime.utcnow()
        data = []
        for key in r:
            dict_items = {}
            dict_items['key'] = key
            dict_items['data'] = r[key]
            dict_items['createdAt'] = utc_timeStamp
            data.append(dict_items)
            
        saved = collection.insert_many(data)

        if saved.acknowledged == True:
            return {"status": "%d data created" %len(saved.inserted_ids), "status_code": 201}
        else:
            return {"status": "cannot create", "status_code": 401}
    else:
        return {"error": "format doesn't match!"}