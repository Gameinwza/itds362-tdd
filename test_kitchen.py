# Test list
# [ ] 200 g x 3 = 600 g
# [ ] Multiplication does not change the original quantity
# [ ] Quantities with the same amount and unit are equal
# [ ] 1 oz is not equal to 1 g
# [ ] 200 g + 300 g = 500 g
# [ ] 200 g + 1 oz can be reduced to grams using an exchange rate
# [ ] (200 g + 1 oz) x 2

from kitchen import Quantity


def test_multiplication():
    flour = Quantity(200)
    assert flour.times(3).amount == 600


def test_multiplication_by_two():
    flour = Quantity(200)
    assert flour.times(2).amount == 400


def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200)
    assert flour.times(3) == Quantity(600)
    assert flour.times(2) == Quantity(400)


def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)
