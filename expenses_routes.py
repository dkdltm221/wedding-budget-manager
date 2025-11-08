from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import func
from models import db, Expense

expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route('/', methods=['GET', 'POST'])
def list_expenses():
    if request.method == 'POST':
        category = request.form.get('category', '').strip()
        description = request.form.get('description', '').strip()
        amount = request.form.get('amount', '').strip()

        if not category or not amount:
            flash('항목과 금액은 필수입니다.', 'danger')
        else:
            try:
                amount_value = int(amount)
                new_expense = Expense(category=category, description=description, amount=amount_value)
                db.session.add(new_expense)
                db.session.commit()
                flash('지출 항목이 추가되었습니다.', 'success')
                return redirect(url_for('expenses.list_expenses'))
            except ValueError:
                flash('금액은 숫자로 입력해주세요.', 'danger')

    expenses_list = Expense.query.order_by(Expense.id.desc()).all()
    total_expense = db.session.query(func.coalesce(func.sum(Expense.amount), 0)).scalar()

    return render_template('expenses.html', expenses=expenses_list, total_expense=total_expense)


@expenses_bp.route('/<int:expense_id>/delete', methods=['POST'])
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    flash('지출 항목이 삭제되었습니다.', 'info')
    return redirect(url_for('expenses.list_expenses'))
