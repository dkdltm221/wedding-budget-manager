from flask import Blueprint, render_template
from services.dashboard_service import fetch_dashboard_metrics

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    metrics = fetch_dashboard_metrics()
    return render_template('index.html', **metrics)
