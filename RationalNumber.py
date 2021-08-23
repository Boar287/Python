from AppliedMath import AppliedMath


class RationalNumber:
    def __init__(self, Numerator, Denominator):
        if Numerator % 1 != 0 or Denominator % 1 != 0:
            raise TypeError("Denominator and Numerator must be integers")
        if Denominator == 0:
            raise ValueError("Denominator can't be equal to 0")
        self.Numerator = Numerator
        self.Denominator = Denominator

    def __add__(self, other):
        if isinstance(other, RationalNumber):
            NewDenominator = AppliedMath.NOK(self.Denominator, other.Denominator)
            NOD = abs(AppliedMath.NOD(
                self.Numerator * NewDenominator / self.Denominator + other.Numerator * NewDenominator / other.Denominator,
                NewDenominator))
            return RationalNumber((
                                          self.Numerator * NewDenominator / self.Denominator + other.Numerator * NewDenominator / other.Denominator) / NOD,
                                  NewDenominator / NOD)
        elif isinstance(other, int):
            NOD = abs(AppliedMath.NOD(self.Numerator + other * self.Denominator, self.Denominator))
            return RationalNumber((self.Numerator + other * self.Denominator) / NOD, self.Denominator / NOD)

    def __sub__(self, other):
        if isinstance(other, RationalNumber):
            NewDenominator = AppliedMath.NOK(self.Denominator, other.Denominator)
            NOD = abs(AppliedMath.NOD(
                self.Numerator * NewDenominator / self.Denominator - other.Numerator * NewDenominator / other.Denominator,
                NewDenominator))
            return RationalNumber((
                                          self.Numerator * NewDenominator / self.Denominator - other.Numerator * NewDenominator / other.Denominator) / NOD,
                                  NewDenominator / NOD)
        elif isinstance(other, int):
            NOD = abs(AppliedMath.NOD(self.Numerator - other * self.Denominator, self.Denominator))
            return RationalNumber((self.Numerator - other * self.Denominator) / NOD, self.Denominator / NOD)

    def __mul__(self, other):
        if isinstance(other, RationalNumber):
            NOD = abs(AppliedMath.NOD(self.Numerator * other.Numerator, self.Denominator * other.Denominator))
            return RationalNumber((self.Numerator * other.Numerator) / NOD,
                                  (self.Denominator * other.Denominator) / NOD)
        elif isinstance(other, int):
            NOD = abs(AppliedMath.NOD(self.Numerator * other, self.Denominator))
            return RationalNumber(self.Numerator * other / NOD, self.Denominator / NOD)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, RationalNumber):
            NOD = abs(AppliedMath.NOD(self.Numerator * other.Denominator, self.Denominator * other.Numerator))
            return RationalNumber(self.Numerator * other.Denominator / NOD, self.Denominator * other.Numerator / NOD)
        elif isinstance(other, int):
            temp = RationalNumber(other, 1)
            NOD = abs(AppliedMath.NOD(self.Numerator * temp.Denominator, self.Denominator * temp.Numerator))
            return RationalNumber(self.Numerator * temp.Denominator / NOD, self.Denominator * temp.Numerator / NOD)

    def __eq__(self, other):
        if isinstance(other, RationalNumber):
            return self.Numerator * other.Denominator == other.Numerator * self.Denominator
        elif isinstance(other, int):
            return self.Numerator * 1 == other * self.Denominator

    def __ne__(self, other):
        if isinstance(other, RationalNumber):
            return self.Numerator * other.Denominator < other.Numerator * self.Numerator
        elif isinstance(other, int):
            return self.Numerator * 1 < other * self.Numerator

    def __gt__(self, other):
        if isinstance(other, RationalNumber):
            return self.Numerator * other.Denominator > other.Numerator * self.Denominator
        if isinstance(other, int):
            return self.Numerator * 1 > other * self.Denominator

    def __lt__(self, other):
        if isinstance(other, RationalNumber):
            return self.Numerator * other.Denominator < other.Numerator * self.Denominator
        if isinstance(other, int):
            return self.Numerator * 1 < other * self.Denominator

    def __str__(self, fraction_style="default"):
        if fraction_style == "default":
            NOD = abs(AppliedMath.NOD(self.Numerator, self.Denominator))
            return str(int(self.Numerator / NOD)) + '/' + str(int(self.Denominator / NOD))
        else:
            return str(round(self.Numerator / self.Denominator, 3))

    __iadd__ = __add__

    @staticmethod
    def sort(*args):
        return sorted(args, key=lambda x: x.Numerator / x.Denominator)
