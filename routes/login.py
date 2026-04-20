from flask import Blueprint, request
from json import loads

login_bp = Blueprint("login", __name__)