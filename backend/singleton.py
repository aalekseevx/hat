def singleton(cls):
    def decorator(new_cls):
        instance = {}

        def wrap(*args, **kwargs):
            if cls not in instance:
                instance[cls] = cls(*args, **kwargs)
            return instance[cls]

        return wrap

    return decorator
