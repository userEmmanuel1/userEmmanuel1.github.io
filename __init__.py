from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import multiprocessing

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app2():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Database 
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

  
    from .models import User, Stocks
     
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database2(app):
    try:
        if not path.exists(DB_NAME):
            db.create_all(app=app)
            print('Created Database! 2')
        else:
            print('Database already exists 2')
    except Exception as e:
        print(f'Error creating database:  2  {e}')

if __name__ == '__main__':
    
    app = create_app2()
    create_database2(app)
    print(f'Database created 2 NOT THIS ONE')