class Singleton():
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception('this class is a singleton')
        else:
            Singleton.__instance = self


ss = Singleton()
print(ss)

s = Singleton.getInstance()
print(s)

s1 = Singleton.getInstance()

print(s1)
