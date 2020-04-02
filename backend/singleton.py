# TODO
# 1) gg в проде, сериосли?
# 2) У тебя есть PEP-8 чекер? Ты тут переопределил str, на что он и ругается
# 3) А почему синглтоном может быть только объект, конструриющийся от одного аргумента / одной строки? args, kwargs
# 4) Ну и singleton не завязан на словарь, а значит лучше отделить в другой файл


def singleton(cls):
    def gg(str):
        instance = {}

        def wrap(str):
            if cls not in instance:
                instance[cls] = cls(str)
            return instance[cls]

        return wrap

    return gg