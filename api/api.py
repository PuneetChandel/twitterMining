from utils.database import Database
from flask import Blueprint,Response
from bson.json_util import dumps
import pymongo

api_route = Blueprint('api', __name__)

@api_route.route('/v1/gadgetscore/<gadget>', methods=['GET'])
def getRating(gadget):
    resp = Response(dumps(Database.find("gadgetscore",
                                           filter={"name":gadget},
                                           projection={"name":1,"score":1,"location":1,"_id":0},
                                           sort=[("score", pymongo.DESCENDING)],
                                           limit=5
                                           )))
    resp.headers['Content-Type'] = 'application/json'
    return resp



