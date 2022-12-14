from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap4
from flask_minify import Minify
from flask_moment import Moment
from flask_toastr import Toastr
from flask_ckeditor import CKEditor

# import config
from config import ProductionConfig

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap4()
minify = Minify(html=True, js=True, cssless=True)
moment = Moment()
toastr = Toastr()
ckeditor = CKEditor()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_message = "Login terlebih dahulu sebelum menggunakan aplikasi."
login_manager.login_message_category = 'error'
login_manager.login_view = 'auth.login'

DOCS = set(['pdf'])
IMG = set(['png', 'jpg', 'jpeg'])


def documents_allowed_extension(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in DOCS


def images_allowed_extension(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in IMG


def page_not_found(e):
    return render_template('error/404.html'), 404


def internal_server_error(e):
    db.session.rollback()
    return render_template('error/500.html'), 500


def forbidden(e):
    return render_template('error/403.html'), 403


def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    minify.init_app(app=app)
    moment.init_app(app)
    toastr.init_app(app)
    ckeditor.init_app(app)

    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    from .user import users as user_blueprint
    from .daily_activity import daily_activity as daily_activity_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(daily_activity_blueprint, url_prefix="/activity")
    app.register_blueprint(main_blueprint)

    # error handler
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, forbidden)
    app.register_error_handler(500, internal_server_error)

    return app
