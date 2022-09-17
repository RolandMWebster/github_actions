from src.coffee import Coffee, CoffeeGrinder, GroundCoffee


class TestCoffeeGrinder:

    def test_set_grind_size(self):
        coffee_grinder = CoffeeGrinder(grind_size=10)
        coffee_grinder.set_grind_size(grind_size=5)
        assert coffee_grinder.grind_size == 5

    def test_grind_coffee(self):
        coffee = Coffee(origin="ethiopia", process="washed", roast="light")
        coffee_grinder = CoffeeGrinder(grind_size=10)
        ground_coffee = coffee_grinder.grind_coffee(coffee=coffee)
        assert isinstance(ground_coffee, GroundCoffee)
        assert ground_coffee.grind_size == 10
