from flask import Blueprint, request
from repositories.user_repo import UserRepo
from database.database import SessionLocal
from flask_jwt_extended import create_access_token

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        return { "message": "400 bad request" }
    
    session = SessionLocal()
    repo = UserRepo(session=session)

    try:
        user = repo.get_by_email(email=email)
        if repo.login(email=email, password=password):
            accessToken = create_access_token(identity=user.id)
            return { "message": "logged in 200", "accessToken": accessToken }
        else:
            return { "message": "thats not your account lil bro" }
    except Exception as e:
        return { "message": f"error {str(e)}" }
