from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request,Flask
from config import *

def app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config['MONGO_URI'] = MONGO_URL
    mongo = PyMongo(app)

    @app.route('/')
    def index():
        listOfIndexes = {0: '/', 1: '/add (give name, email, mobile in json format)', 2: '/searchByEmail (give email)',
                         3: '/searchByName (give name in json format)', 4: '/update (give new name, email, mobile in json format)', 5: '/delete (give email in json format)'}
        return jsonify(status="success",data=listOfIndexes)

    @app.route('/add', methods=['POST'])
    def add_user():
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        _phone = _json['mobile']
        x = dumps(mongo.db.contact.find({"_id": _email}))
        print(x)
        if x != "[]":
            return jsonify("Email Already Exist, Please use a different Email!!!")
        elif _name and _email and _phone and request.method == 'POST':
            mongo.db.contact.insert(
                {'_id': _email, 'name': _name, 'mobile': _phone})
            resp = jsonify("User Added Successfully")
            resp.status_code = 200
            return resp
        else:
            return not_found()


    @app.errorhandler(404)
    def not_found(error=None):
        message = {
            'message': 'Sorry, Unable to process your request. Please fill the details correctly !!!'
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp


    @app.route('/searchByEmail', methods=['GET'])
    def searchByEmail():
        _json = request.json
        _email = _json["email"]
        _usr = mongo.db.contact.find({"_id": _email})
        resp = dumps(_usr)
        if resp == "[]":
            return jsonify("Unable to find the User with this Email")
        return resp


    @app.route('/searchByName', methods=['GET'])
    def searchByName():
        _json = request.json
        name = _json["name"]
        usrs = mongo.db.contact.find({"name": name})
        resp = dumps(usrs)
        if resp == "[]":
            return jsonify("User with this Name is not found")
        return resp


    @app.route('/delete', methods=['DELETE'])
    def delete_user():
        _json = request.json
        _email = _json["email"]
        mongo.db.contact.delete_one({"_id": _email})
        resp = jsonify("User Deleted Successfully")
        resp.status_code = 200
        return resp


    @app.route('/update', methods=['PUT'])
    def updateUserInfo():
        _json = request.json
        _email = _json["email"]
        _name = _json["name"]
        _phone = _json["mobile"]

        if _name and _email and _phone and request.method == 'PUT':
            mongo.db.contact.update_one(
                {"_id": _email}, {'$set': {'name': _name, 'mobile': _phone}})
            resp = jsonify("User Info. Updated Successfully")
            resp.status_code = 200
            return resp
        else:
            return not_found()
    return app
