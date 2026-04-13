from flask import Flask
from routes.project_routes import project_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(project_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)