class GeneratorConfig:
    def __init__(self):
        self.count = 1

    @property
    def count(self):
        return self.count

    @count.setter
    def count(self, number: int):
        self.count = number
