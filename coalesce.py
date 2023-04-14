def coalesce(*args):
    for arg in args:
        match bool(arg):
            case False:
                continue
            case _:
                return arg
    return None
