# Example test class
class Test:
    def __init__(self):
        self.name = "Test"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


test = Test()
print(test.get_name())
