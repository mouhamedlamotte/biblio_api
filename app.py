from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from dotenv import load_dotenv

import os


from flask_cors import CORS




load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:{os.getenv('POSTGRESS_PW')}@localhost:5432/biblio"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"

    
    db.init_app(app)
    
    
    from src.routes.user import register_users_route
    from src.routes.books import resgiter_books_route
    from src.routes.auth.login import register_login_route
    
     
        
    register_users_route(app, db)
    resgiter_books_route(app, db)
    register_login_route(app, db)
    
    migrate = Migrate(app, db)
    
    return app