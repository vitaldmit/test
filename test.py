# Example test class
class Test:
    def __init__(self):
        self.name = "Test"
        self.age = 20

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name


test = Test()
print(test.get_name())
