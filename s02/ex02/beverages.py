class HotBeverage:
    def __init__(self, price = 0.3, name = "hot beverage"):
        self.price = price
        self.name = name

    def __str__(self) -> str:
        str = ""
        str += f"name: {self.name}\n"
        str += f"price: {self.price}\n"
        str += f"description: {self.description()}"
        return str

    def description(self, value = "Just some hot water in a cup."):
        return self.Description(value)
    class Description:
        def __init__(self, msg) -> None:
            self.msg = msg

        def __str__(self) -> str:
            return self.msg

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(price = 0.4, name = "coffee")

    def description(self):
        return super().description("A coffee, to stay awake.")

class Tea(HotBeverage):
    def __init__(self):
        super().__init__(name = "tea")

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__(price = 0.5, name = "chocolate")

    def description(self):
        return super().description("Chocolate, sweet chocolate...")

class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__(price = 0.45, name = "cappuccino")

    def description(self):
        return super().description("Un po' di Italia nella sua tazza!")