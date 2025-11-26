from typing import Optional, Tuple

from sqlalchemy import func, case, asc, desc
from models import db, Guest


def sorting_from_request(args) -> Tuple[str, str, object]:
    sort_by = args.get('sort_by', 'id')
    order = args.get('order', 'desc')
    sort_map = {'name': Guest.name, 'amount': Guest.amount, 'id': Guest.id}
    sort_column = sort_map.get(sort_by, Guest.id)
    order_fn = desc if order == 'desc' else asc
    return sort_by, order, order_fn(sort_column)


def search_filter(name: str) -> Optional[object]:
    return Guest.name.contains(name) if name else None


def fetch_guests(side: str, order_clause, search_filter_obj=None):
    query = Guest.query.filter(Guest.side == side)
    if search_filter_obj is not None:
        query = query.filter(search_filter_obj)
    return query.order_by(order_clause, Guest.id).all()


def totals(search_filter_obj=None) -> Tuple[int, int]:
    totals_query = db.session.query(
        func.coalesce(func.sum(case((Guest.side == 'groom', Guest.amount), else_=0)), 0).label('groom_total'),
        func.coalesce(func.sum(case((Guest.side == 'bride', Guest.amount), else_=0)), 0).label('bride_total')
    )
    if search_filter_obj is not None:
        totals_query = totals_query.filter(search_filter_obj)
    totals_row = totals_query.first()
    return (totals_row.groom_total or 0, totals_row.bride_total or 0)

def count_guests(side: str, search_filter_obj=None) -> int:
    query = Guest.query.filter(Guest.side == side)
    if search_filter_obj is not None:
        query = query.filter(search_filter_obj)
    return query.count()

def fetch_guests_paginated(side: str, order_clause, page: int, per_page: int, search_filter_obj=None):
    query = Guest.query.filter(Guest.side == side)
    if search_filter_obj is not None:
        query = query.filter(search_filter_obj)
    return query.order_by(order_clause, Guest.id).offset((page - 1) * per_page).limit(per_page).all()


def parse_amount(amount_str: str) -> int:
    amount_value = int(amount_str)
    if amount_value < 0:
        raise ValueError("amount must be >= 0")
    return amount_value


def create_guest(name: str, side: str, amount_value: int, note: str = "") -> Guest:
    new_guest = Guest(name=name, side=side, amount=amount_value, note=note)
    db.session.add(new_guest)
    db.session.commit()
    return new_guest
