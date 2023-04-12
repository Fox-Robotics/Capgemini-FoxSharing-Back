from flask import Blueprint
blueprint = Blueprint('prueba_blueprint', __name__)


@blueprint.route("/url", methods=['GET'])
def hello():
  return 'hello world'