from flask import request, Blueprint
import requests
import json
from config import AzureMapskey

priceBP = Blueprint('priceBP', __name__)

@addressToLocationBP.route('/price', methods=['GET'])
def price():
    args = request.args
    query = args.get("address")
    url = "https://atlas.microsoft.com/search/fuzzy/json?&api-version=1.0&subscription-key=" + AzureMapskey + "&language=en-US&query=" + query
    response = requests.get(url)
    json_object = json.loads(response.text)
    answer = []
    if len(json_object["results"]) > 0:
        for result in json_object["results"]:
            dic = {
                "data" : result["address"]["freeformAddress"]
            }
            answer.append(dic)
        return str(answer)
    return "[]"