# Test list
# [x] 200 g x 3 = 600 g
# [x] Multiplication does not change the original quantity
# [x] Quantities with the same amount and unit are equal
# [x] 1 oz is not equal to 1 g
# [x] 200 g + 300 g = 500 g
# [x] 200 g + 1 oz can be reduced to grams using an exchange rate
# [x] (200 g + 1 oz) x 2

from kitchen import Converter, Quantity


def grams(amount):
    return Quantity(amount, "g")


def ounces(amount):
    return Quantity(amount, "oz")


def test_multiplication():
    flour = grams(200)
    assert flour.times(3).amount == 600


def test_multiplication_by_two():
    flour = grams(200)
    assert flour.times(2).amount == 400


def test_multiplication_returns_a_new_quantity():
    flour = grams(200)
    assert flour.times(3) == grams(600)
    assert flour.times(2) == grams(400)
    assert flour == grams(200)


def test_equality():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)


def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)


def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)


def test_addition_across_units():
    converter = Converter()
    converter.add_rate("oz", "g", 28.35)
    total = grams(200).plus(ounces(1))
    assert converter.reduce(total, "g") == grams(228.35)


def test_multiply_a_sum():
    converter = Converter()
    converter.add_rate("oz", "g", 28.35)
    total = grams(200).plus(ounces(1)).times(2)
    assert converter.reduce(total, "g") == grams(456.70)
