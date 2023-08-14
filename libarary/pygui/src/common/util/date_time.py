import arrow


def now() -> str:
    return arrow.now().format('YYYY-MM-DD HH:mm:ss')


def today() -> str:
    return arrow.now().format('YYYY-MM-DD')
