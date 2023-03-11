"""
This module provides implementation for singleton

"""


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
       """ Virtually private constructor. """
       if Singleton.__instance != None:
          raise Exception("This class is a singleton!")
       else:
          Singleton.__instance = self



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
    print(obj.getInstance())
    try:
        obj1= log()
        print(obj.info('test message 1'))
        print(obj.getInstance())
    except Exception as error:
        print(error)
