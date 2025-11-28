from typing import List, Tuple
from sqlalchemy import func
from models import db, Expense


def list_expenses() -> Tuple[List[Expense], int]:
    expenses_list = Expense.query.order_by(Expense.id.desc()).all()
    total_expense = db.session.query(
        func.coalesce(func.sum(Expense.amount), 0)
    ).scalar()
    return expenses_list, total_expense


def create_expense(category: str, description: str, amount_value: int) -> Expense:
    new_expense = Expense(
        category=category,
        description=description,
        amount=amount_value
    )
    db.session.add(new_expense)
    db.session.commit()
    return new_expense


def get_expense(expense_id: int) -> Expense:
    return Expense.query.get_or_404(expense_id)


def update_expense(expense: Expense, category: str, description: str, amount_value: int) -> Expense:
    expense.category = category
    expense.description = description
    expense.amount = amount_value
    db.session.commit()
    return expense


def delete_expense_record(expense: Expense) -> None:
    db.session.delete(expense)
    db.session.commit()
