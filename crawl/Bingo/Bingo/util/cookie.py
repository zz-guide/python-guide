def cookie_str_to_dict(cookie: str):
    if len(cookie) == 0:
        return {}

    cookie_dict = {}
    for item in cookie.split('; '):
        key, value = item.split('=', maxsplit=1)
        cookie_dict[key] = value
