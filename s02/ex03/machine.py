import beverages
import random

class CoffeeMachine:
    def __init__(self) -> None:
        self.used = 0

    def repair(self):
        self.used = 0
    
    def serve(self, cup):
        if self.used == 10:
            raise self.BrokenMachineException()
        items = [cup, EmptyCup()]
        self.used += 1
        return random.choice(items)
    class BrokenMachineException(Exception):
        def __init__(self, *args: object) -> None:
            self.message = "This coffee machine has to be repaired."
            super().__init__(self.message)

class EmptyCup(beverages.HotBeverage):
    def __init__(self) -> None:
        super().__init__(price=0.9, name="empty cup")

    def description(self):
        return super().description("An empty cup?! Gimme my money back!")
