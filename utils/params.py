def parse_int(value, default: int, min_value: int = None, max_value: int = None) -> int:
    try:
        num = int(value)
    except (TypeError, ValueError):
        return default

    if min_value is not None and num < min_value:
        return default
    if max_value is not None and num > max_value:
        return default
    return num


def parse_pagination(args, default_page: int = 1, default_per_page: int = 20, max_per_page: int = 100) -> tuple[int, int]:
    page = parse_int(args.get('page'), default_page, min_value=1)
    per_page = parse_int(args.get('per_page'), default_per_page, min_value=1, max_value=max_per_page)
    return page, per_page
