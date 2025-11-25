import os
from flask import Flask
from models import db
from dashboard_routes import dashboard_bp
from expenses_routes import expenses_bp
from guests_routes import guests_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wedding_budget.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-should-be-changed')
app.config['EXPENSES_ACCESS_CODE'] = os.environ.get('EXPENSES_ACCESS_CODE', '0000')

db.init_app(app)

# 블루프린트 등록
app.register_blueprint(dashboard_bp, url_prefix='/')
app.register_blueprint(expenses_bp, url_prefix='/expenses')
app.register_blueprint(guests_bp, url_prefix='/guests')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
