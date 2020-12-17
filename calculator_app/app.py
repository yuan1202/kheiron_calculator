import sys
import logging
import json
import flask
from flask import Blueprint, request, jsonify, current_app, abort
from calculators.calculators import prefix_op, infix_op


# Logging
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler])


bp = Blueprint('calculator', __name__)


@bp.route('/prefix', methods=['POST'])
def prefix():
    data = request.get_data(as_text=True)
    try:
        return prefix_op(data)
    except Exception as e:
        current_app.logger.info(e)
        abort(400)
    

@bp.route('/infix', methods=['POST'])
def infix():
    data = request.get_data(as_text=True)
    try:
        return infix_op(data)
    except Exception as e:
        current_app.logger.info(e)
        abort(400)
    

# The flask app
app = flask.Flask(__name__)
app.register_blueprint(bp)


def launch():
    app.run(debug=True, host='0.0.0.0')