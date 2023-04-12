from flask import request, Blueprint
import requests
import json
from databaseConection import AzureMapskey

addressToLocationBP = Blueprint('addressToLocationBP', __name__)


@addressToLocationBP.route('/address', methods=['GET'])
def login():
    args = request.args
    query = args.get("address")
    url = "https://atlas.microsoft.com/search/fuzzy/json?&api-version=1.0&subscription-key=" + AzureMapskey + "&language=en-US&query=" + query
    response = requests.get(url)
    json_object = json.loads(response.text)
    if len(json_object["results"]) > 0:
        print(json_object["results"][0]["position"])
        return json_object["results"][0]["position"]
    return "{}"
