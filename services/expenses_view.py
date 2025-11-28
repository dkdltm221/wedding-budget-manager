from typing import Dict, Any
from services.expenses_service import list_expenses
from view_models import ExpensesPageVM


def build_expenses_context() -> Dict[str, Any]:
    expenses_list, total_expense = list_expenses()
    vm = ExpensesPageVM(expenses=expenses_list, total_expense=total_expense)
    return vm.to_dict()
