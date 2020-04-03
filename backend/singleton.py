def singleton(cls):
    def decorator(new_cls):
        instance = {}

        def wrap(*args, **kwargs):
            if (cls, *args, tuple(**kwargs)) not in instance.keys():
                instance[(cls, *args, tuple(**kwargs))] = cls(*args, **kwargs)
            return instance[(cls, *args, tuple(**kwargs))]

        return wrap

    return decorator
