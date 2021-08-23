class AppliedMath:

    @staticmethod
    def NOD(a, b):
        a = abs(a)
        b = abs(b)
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    @staticmethod
    def NOK(a, b):
        return a / AppliedMath.NOD(a, b) * b
