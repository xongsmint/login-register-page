# basically useless
from flask import Blueprint, request
from json import loads

root_bp = Blueprint("root", __name__)

@root_bp.route("/", methods=["GET"])
def root():
    return { "message": "Hello World!... This is just a test route dumbass, i'm not getting shit for you." }
