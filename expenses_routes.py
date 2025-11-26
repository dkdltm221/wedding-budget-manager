from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from models import Expense
from services.expenses_service import (
    list_expenses,
    create_expense,
    get_expense,
    update_expense,
    delete_expense_record
)
from services.expenses_view import build_expenses_context
from forms import ExpenseForm

expenses_bp = Blueprint('expenses', __name__, url_prefix='/expenses')


@expenses_bp.before_request
def require_access_code():
    # 접근 허용 경로 제외: 패스코드 해제
    if request.endpoint in ('expenses.unlock', 'expenses.lock'):
        return

    if not session.get('expenses_unlocked'):
        flash('지출 관리로 이동하려면 비밀번호가 필요합니다.', 'warning')
        return redirect(url_for('dashboard.index'))


@expenses_bp.route('/unlock', methods=['POST'])
def unlock():
    access_code = request.form.get('access_code', '').strip()
    expected = current_app.config.get('EXPENSES_ACCESS_CODE', '1234')

    if access_code == expected:
        session['expenses_unlocked'] = True
        flash('지출 관리가 열렸습니다.', 'success')
        return redirect(url_for('expenses.list_expenses'))

    flash('비밀번호가 올바르지 않습니다.', 'danger')
    return redirect(url_for('dashboard.index'))


@expenses_bp.route('/lock', methods=['POST'])
def lock():
    session.pop('expenses_unlocked', None)
    flash('지출 관리 잠금이 설정되었습니다.', 'info')
    return redirect(url_for('dashboard.index'))


@expenses_bp.route('/', methods=['GET', 'POST'])
def list_expenses():
    # 지출 추가
    form = ExpenseForm(request.form, meta={'csrf': False})
    if request.method == 'POST':
        if form.validate():
            try:
                create_expense(
                    category=form.category.data.strip(),
                    description=(form.description.data or '').strip(),
                    amount_value=form.amount.data
                )
                flash('지출 항목이 추가되었습니다.', 'success')
                return redirect(url_for('expenses.list_expenses'))
            except ValueError:
                flash('금액은 0 이상의 숫자로 입력해주세요.', 'danger')
        else:
            flash('항목과 금액은 필수이며, 금액은 0 이상이어야 합니다.', 'danger')

    # 목록 + 총합 조회
    context = build_expenses_context()
    context['form'] = form
    return render_template('expenses.html', **context)


@expenses_bp.route('/<int:expense_id>/edit', methods=['GET', 'POST'])
def edit_expense(expense_id):
    expense = get_expense(expense_id)

    if request.method == 'POST':
        category = request.form.get('category', '').strip()
        description = request.form.get('description', '').strip()
        amount = request.form.get('amount', '').strip()

        if not category or not amount:
            flash('항목과 금액은 필수입니다.', 'danger')
            return redirect(url_for('expenses.edit_expense', expense_id=expense.id))

        try:
            amount_value = int(amount)
            if amount_value < 0:
                raise ValueError

            update_expense(expense, category=category, description=description, amount_value=amount_value)
            flash('지출 항목이 수정되었습니다.', 'success')
            return redirect(url_for('expenses.list_expenses'))

        except ValueError:
            flash('금액은 0 이상의 숫자로 입력해주세요.', 'danger')
            return redirect(url_for('expenses.edit_expense', expense_id=expense.id))

    # GET 요청: 수정 화면 렌더링
    return render_template('expenses_edit.html', expense=expense)


@expenses_bp.route('/<int:expense_id>/delete', methods=['POST'])
def delete_expense(expense_id):
    expense = get_expense(expense_id)
    delete_expense_record(expense)
    flash('지출 항목이 삭제되었습니다.', 'info')
    return redirect(url_for('expenses.list_expenses'))
