from flask import Blueprint, render_template
from sqlalchemy import func
from models import db, Expense, Guest

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    total_income = db.session.query(func.coalesce(func.sum(Guest.amount), 0)).scalar()
    total_expense = db.session.query(func.coalesce(func.sum(Expense.amount), 0)).scalar()
    net_profit = total_income - total_expense

    groom_total = db.session.query(func.coalesce(func.sum(Guest.amount), 0)).filter(Guest.side == 'groom').scalar()
    bride_total = db.session.query(func.coalesce(func.sum(Guest.amount), 0)).filter(Guest.side == 'bride').scalar()

    expense_rows = db.session.query(
        Expense.category,
        func.coalesce(func.sum(Expense.amount), 0)
    ).group_by(Expense.category).all()

    expense_labels = [row[0] for row in expense_rows]
    expense_values = [row[1] for row in expense_rows]

    return render_template(
        'index.html',
        total_income=total_income,
        total_expense=total_expense,
        net_profit=net_profit,
        groom_total=groom_total,
        bride_total=bride_total,
        expense_labels=expense_labels,
        expense_values=expense_values
    )
