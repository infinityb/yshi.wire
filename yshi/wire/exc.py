class WireError(Exception):
    pass


class WireValueError(WireError, ValueError):
    pass


class WireTypeError(WireError, TypeError):
    pass
