from flask import Flask
from flask import request
import logging

app = Flask(__name__)

logger = logging.getLogger('j7s-app')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


@app.route("/", defaults={"path": ""}, methods = ['POST', 'GET'])
@app.route('/<path:path>', methods=['POST', 'GET'])
def root(path):
    logger.info("Path")
    logger.info(path)
    logger.info("Headers:")
    logger.info(request.headers)
    logger.info("Body:")
    logger.info(request.json)
    return "<p>Hello</p>"
