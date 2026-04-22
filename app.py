from flask import Flask
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from routes.register import register_bp
from routes.root import root_bp
from database.database import Base, engine

# START Db
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "corinthians_minha_vida" # mudar depois
jwt = JWTManager(app)

# routes
app.register_blueprint(root_bp, url_prefix="/")
app.register_blueprint(register_bp, url_prefix="/api")
