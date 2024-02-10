from flask import Flask
from flask_cors import CORS
from .inference import inference_bp


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    

  

    # Import and register your blueprints
    app.register_blueprint(inference_bp, url_prefix='/inference')
    



    return app

app = create_app()



if __name__ == '__main__':
    app.run(debug=True)
