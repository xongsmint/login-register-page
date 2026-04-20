from flask import Blueprint, request
from json import loads

delete_bp = Blueprint("delete", __name__)