import matplotlib.pyplot as plt

# Finds the GCD (greatest common divisor) using the Euclidean Algorithm
def GCD(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    q = a // b
    r = a - b * q
    return GCD(b, r)

class Fraction:
    def __init__(self, num, denom):
        if denom == 0:
            raise ZeroDivisionError("Denominator cannot be 0")
        self.num = num
        self.denom = denom

    def reciprocal(self):
        if self.num == 0:
            raise ZeroDivisionError("Numerator is 0, reciprocal does not exist")
        return Fraction(self.denom, self.num)

    def simplify(self):
        gcd = GCD(self.num, self.denom)
        return Fraction(self.num // gcd, self.denom // gcd)

    def add(self, other):
        new_num = self.num * other.denom + self.denom * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom).simplify()

    def sub(self, other):
        new_num = self.num * other.denom - self.denom * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom).simplify()

    def mult(self, other):
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def div(self, other):
        if other.num == 0:
            raise ZeroDivisionError("Division by 0 undefined")
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        return Fraction(new_num, new_denom)

    @classmethod
    def from_continued_fraction(cls, terms):
        frac = Fraction(terms[-1], 1)
        # want to iterate through terms in reverse order, skipping original last term
        for i in range(len(terms) - 2, -1, -1):
            frac = frac.reciprocal().add(Fraction(terms[i], 1))
        return frac

    def continued_fraction(self):
        terms = []
        num = self.num
        denom = self.denom
        while denom != 0:
            whole = num // denom
            num -= whole * denom

            terms.append(whole)
            num, denom = denom, num
        return terms

    def graph_continued_fraction(self):
        terms = self.continued_fraction()
        plt.plot(terms, 'bo')
        plt.show()

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(str(self.simplify()))

    def __add__(self, other):
        assert isinstance(other, Fraction)
        return self.add(other)

    def __sub__(self, other):
        assert isinstance(other, Fraction)
        return self.sub(other)

    def __mul__(self, other):
        assert isinstance(other, Fraction)
        return self.mult(other)

    def __div__(self, other):
        assert isinstance(other, Fraction)
        return self.div(other)

    def __eq__(self, other):
        assert isinstance(other, Fraction)
        self_simple = self.simplify()
        other_simple = self.simplify()
        return self_simple.num == other_simple.num and self_simple.denom == other_simple.denom

if __name__ == "__main__":
    # testing