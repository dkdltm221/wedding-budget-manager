from typing import Dict, Any
from models import Guest
from services.guests_service import (
    sorting_from_request,
    search_filter,
    fetch_guests,
    fetch_guests_paginated,
    totals,
    count_guests,
)
from view_models import GuestsPageVM
from utils.params import parse_pagination


def build_guest_page_context(args) -> Dict[str, Any]:
    search_name = args.get('search_name', '').strip()
    sort_by, order, order_clause = sorting_from_request(args)
    search_filter_obj = search_filter(search_name)
    page, per_page = parse_pagination(args, default_page=1, default_per_page=20, max_per_page=200)

    groom_guests = fetch_guests_paginated('groom', order_clause, page, per_page, search_filter_obj=None)
    bride_guests = fetch_guests_paginated('bride', order_clause, page, per_page, search_filter_obj=None)
    groom_total, bride_total = totals(search_filter_obj=None)
    groom_count = count_guests('groom', search_filter_obj=None)
    bride_count = count_guests('bride', search_filter_obj=None)

    search_results = (
        Guest.query.filter(search_filter_obj).order_by(order_clause, Guest.id).all()
        if search_filter_obj is not None else []
    )

    vm = GuestsPageVM(
        groom_guests=groom_guests,
        bride_guests=bride_guests,
        groom_total=groom_total,
        bride_total=bride_total,
        search_name=search_name,
        sort_by=sort_by,
        order=order,
        search_results=search_results,
        highlight_threshold=300000,
        page=page,
        per_page=per_page,
        groom_count=groom_count,
        bride_count=bride_count
    )
    return vm.to_dict()
