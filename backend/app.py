from flask import Flask
from config import Config
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from routes.project_routes import project_bp
    app.register_blueprint(project_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

    