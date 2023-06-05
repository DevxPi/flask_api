import os
from os import environ, path

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = path.join(app.instance_path, 'app.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from .api import api_bp

    app.register_blueprint(api_bp, url_prefix='/api')

    # a simple route with return hello world
    @app.route('/hello')
    def hello():
        return 'Hello World'
    
    return app