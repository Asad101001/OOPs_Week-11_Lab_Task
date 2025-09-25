from P31 import P31

class App:
    def __init__(self):
        pass

    @staticmethod
    def run():
            obj = P31()
            print(obj.make_change(674.5, 1000))