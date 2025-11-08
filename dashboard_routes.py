from flask import Blueprint, render_template
from sqlalchemy import func, case
from models import db, Expense, Guest

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    # 여러 쿼리를 하나로 통합하여 Guest 관련 데이터를 한 번에 가져옵니다.
    guest_summary = db.session.query(
        func.coalesce(func.sum(Guest.amount), 0).label('total_income'),
        func.coalesce(func.sum(case((Guest.side == 'groom', Guest.amount), else_=0)), 0).label('groom_total'),
        func.coalesce(func.sum(case((Guest.side == 'bride', Guest.amount), else_=0)), 0).label('bride_total')
    ).one()

    total_expense = db.session.query(func.coalesce(func.sum(Expense.amount), 0)).scalar()
    net_profit = guest_summary.total_income - total_expense

    expense_rows = db.session.query(
        Expense.category,
        func.coalesce(func.sum(Expense.amount), 0)
    ).group_by(Expense.category).all()

    expense_labels = [row[0] for row in expense_rows]
    expense_values = [row[1] for row in expense_rows]

    return render_template(
        'index.html',
        total_income=guest_summary.total_income,
        total_expense=total_expense,
        net_profit=net_profit,
        groom_total=guest_summary.groom_total,
        bride_total=guest_summary.bride_total,
        expense_labels=expense_labels,
        expense_values=expense_values
    )
