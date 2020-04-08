def singleton(cls):
    def decorator(_):
        instance = {}

        def wrap(*args, **kwargs):
            if (cls, *args, frozenset(kwargs.items())) not in instance.keys():
                instance[(cls, *args, frozenset(kwargs.items()))] = cls(*args, **kwargs)
            return instance[(cls, *args, frozenset(kwargs.items()))]

        return wrap

    return decorator
