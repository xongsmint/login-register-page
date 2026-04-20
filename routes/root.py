# basically useless
from flask import Blueprint, request
from json import loads

root_bp = Blueprint("root", __name__)

@root_bp.route("/")
def root():
    if request.method == "POST":
        data = loads(request.get_data(as_text=True))
        return { "message": "Hello World!... This is just a test route dumbass, i ain't posting nothing.", "yourRequest": data }

    if request.method == "GET":
        return { "message": "Hello World!... This is just a test route dumbass, i'm not getting shit for you." }
    
    if request.method == "DELETE":
        data = loads(request.get_data(as_text=True))
        return { "message": "Hello World!... This is just a test route dumbass, i ain't posting nothing.", "yourRequest": data if data else "your request didn't have any body" }
    
    if request.method == "PUT":
        data = loads(request.get_data(as_text=True))
        return { "message": "Hello World!... This is just a test route dumbass, i ain't updating nothing.", "yourRequest": data if data else "your request didn't have any body" }
