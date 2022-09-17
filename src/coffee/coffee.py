class Coffee:
    def __init__(self, origin, process, roast):
        self.origin = origin
        self.process = process
        self.roast = roast


class GroundCoffee(Coffee):
    def __init__(self, origin, process, roast, grind_size):
        super().__init__(origin, process, roast)
        self.grind_size = grind_size


class CoffeeGrinder:
    def __init__(self, grind_size):
        self.grind_size = grind_size

    def set_grind_size(self, grind_size):
        self.grind_size = grind_size

    def grind_coffee(self, coffee: Coffee) -> GroundCoffee:
        return GroundCoffee(
            origin=coffee.origin,
            process=coffee.process,
            roast=coffee.roast,
            grind_size=self.grind_size
        )
