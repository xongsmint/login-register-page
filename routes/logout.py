from flask import Blueprint, request
from json import loads

logout_bp = Blueprint("logout", __name__)