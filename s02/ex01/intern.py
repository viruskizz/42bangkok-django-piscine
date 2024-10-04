class Intern:
    def __init__(self, Name = "My name? I'm nobody, an intern, I have no name"):
        self.Name = Name

    def __str__(self) -> str:
        return self.Name

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return self.Coffee()
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
