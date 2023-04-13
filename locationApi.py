from flask import request, Blueprint
import requests
import json
from config import AzureMapskey

addressToLocationBP = Blueprint('addressToLocationBP', __name__)


@addressToLocationBP.route('/addressFuzzy', methods=['GET'])
def addressFuzzy():
    args = request.args
    query = args.get("address")
    url = "https://atlas.microsoft.com/search/fuzzy/json?&api-version=1.0&subscription-key=" + AzureMapskey + "&language=en-US&query=" + query
    response = requests.get(url)
    json_object = json.loads(response.text)
    answer = []
    if len(json_object["results"]) > 0:
        for result in json_object["results"]:
            answer.append(result["address"]["freeformAddress"])
        return str(answer)
    return "[]"


@addressToLocationBP.route('/address', methods=['GET'])
def address():
    args = request.args
    query = args.get("address")
    url = "https://atlas.microsoft.com/search/fuzzy/json?&api-version=1.0&subscription-key=" + AzureMapskey + "&language=en-US&query=" + query
    response = requests.get(url)
    json_object = json.loads(response.text)
    if len(json_object["results"]) > 0:
        print(json_object["results"][0]["position"])
        return (json_object["results"][0]["position"])
    return "{}"


@addressToLocationBP.route('/route', methods=['GET'])
def route():
    args = request.args
    query = args.get("query") #latitudeInitial,longitudInitial:latitude,longitud
    url = "https://atlas.microsoft.com/route/directions/json?api-version=1.0&query=" + query + "&subscription-key=" + AzureMapskey + "&RouteType=eco&polyline=true"
    response = requests.get(url)
    json_object = json.loads(response.text)
    if len(json_object["routes"]) > 0:
        print(json_object["routes"][0]["legs"][0]["points"])
        return str(json_object["routes"][0]["legs"][0]["points"])
    return "{}"