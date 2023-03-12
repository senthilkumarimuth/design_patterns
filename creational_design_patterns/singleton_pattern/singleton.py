"""
This module provides implementation for singleton

"""


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == "__main__":


    # without singleton

    class log():

        @classmethod
        def info(cls, message):
            return message


    obj = log()
    print(obj.info('test message'))
    print(id(obj))
    obj1 = log()
    print(obj1.info('test message 1'))
    print(id(obj1))

    # with singleton

    class log(Singleton):

        @classmethod
        def info(cls, message):
            return message

    obj = log()
    print(obj.info('test message'))
    print(id(obj))
    obj1= log()
    print(obj.info('test message 1'))
    print(id(obj1))

