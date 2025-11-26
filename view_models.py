from dataclasses import dataclass, asdict
from typing import List, Dict, Any
from models import Guest, Expense


@dataclass
class GuestsPageVM:
    groom_guests: List[Guest]
    bride_guests: List[Guest]
    groom_total: int
    bride_total: int
    search_name: str
    sort_by: str
    order: str
    search_results: List[Guest]
    highlight_threshold: int
    page: int
    per_page: int
    groom_count: int
    bride_count: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DashboardPageVM:
    total_income: int
    total_expense: int
    net_profit: int
    coverage_percent: int
    expense_labels: list
    expense_values: list
    top_expenses: list

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ExpensesPageVM:
    expenses: List[Expense]
    total_expense: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
