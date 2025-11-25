from flask import Blueprint, render_template
from sqlalchemy import func
from models import db, Expense, Guest

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    total_income = db.session.query(
        func.coalesce(func.sum(Guest.amount), 0)
    ).scalar()
    total_expense = db.session.query(
        func.coalesce(func.sum(Expense.amount), 0)
    ).scalar()
    net_profit = total_income - total_expense
    coverage_percent = int(round((total_income / total_expense) * 100)) if total_expense else 0

    expense_rows = db.session.query(
        Expense.category,
        func.coalesce(func.sum(Expense.amount), 0)
    ).group_by(Expense.category).all()

    expense_labels = [row[0] for row in expense_rows]
    expense_values = [row[1] for row in expense_rows]
    top_expenses = sorted(
        [{'category': label, 'amount': value} for label, value in expense_rows],
        key=lambda x: x['amount'],
        reverse=True
    )[:3]

    return render_template(
        'index.html',
        total_income=total_income,
        total_expense=total_expense,
        net_profit=net_profit,
        coverage_percent=coverage_percent,
        expense_labels=expense_labels,
        expense_values=expense_values,
        top_expenses=top_expenses
    )
