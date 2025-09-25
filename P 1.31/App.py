from P31 import P31

class App:
    def __init__(self):
        pass

    @staticmethod
    def run():
            obj = P31()
            print("==== P-1.31 make_change ====")
            print("Case 1 (Valid - charged:347.5, given:1000):", obj.make_change(347.5, 1000))
            print("Case 2 (Insufficient - charged:500, given:300):", obj.make_change(500, 300))
            print("Case 3 (TypeError - charged:abc, given:1000):", obj.make_change("abc", 1000))
            print("Case 4 (Negative - charged:-100, given:500):", obj.make_change(-100, 500))