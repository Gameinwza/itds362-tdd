class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, other):
        return Sum(self, other)

    def reduce(self, unit, converter):
        return converter.convert(self, unit)

    def __eq__(self, other):
        return (
            isinstance(other, Quantity)
            and self.amount == other.amount
            and self.unit == other.unit
        )

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def times(self, multiplier):
        return Sum(self.left.times(multiplier), self.right.times(multiplier))

    def reduce(self, unit, converter):
        left = converter.reduce(self.left, unit)
        right = converter.reduce(self.right, unit)
        return Quantity(left.amount + right.amount, unit)


class Converter:
    def __init__(self):
        self.rates = {}

    def add_rate(self, source, target, rate):
        self.rates[source, target] = rate

    def reduce(self, expression, unit):
        return expression.reduce(unit, self)

    def convert(self, quantity, unit):
        rate = 1 if quantity.unit == unit else self.rates[quantity.unit, unit]
        return Quantity(quantity.amount * rate, unit)
