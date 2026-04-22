from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from repositories.user_repo import UserRepo
from database.database import SessionLocal

register_bp = Blueprint("register", __name__)

@register_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")
    nickname = data.get("nickname")

    if not all([email, password, nickname]):
        return { "error": "400 bad request" }

    session = SessionLocal()
    repo = UserRepo(session=session)

    try:
        user = repo.register_user(email=email, password=password, nickname=nickname)
        accessToken = create_access_token(identity=user.id)
        return { "user": user.serialize(), "accessToken": accessToken }
    except Exception as e:
        return { "message": f"{str(e)}", "error": "lowkey internal server error 500" }
