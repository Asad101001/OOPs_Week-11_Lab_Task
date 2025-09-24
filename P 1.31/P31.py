class P31:
    def make_change(self, charged, given):
        if given < charged:
            return "Insufficient amount given."
        
        change = round(given - charged, 2)
        denominations = {
            "1000 bill": 1000,
            "500 bill": 500,
            "100 bill": 100,
            "50 bill": 50,
            "20 bill": 20,
            "10 bill": 10,
            "5 coin": 5,
            "2 coin": 2,
            "1 coin": 1,
            "0.5 coin": 0.5
        }
        
        result = {}
        for name, value in denominations.items():
            count = int(change // value)
            if count > 0:
                result[name] = count
                change -= count * value
        
        return result
