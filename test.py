# Example test class
class Test:
    def __init__(self):
        self.name = "Test"
        self.age = 20
        self.gender = "Male"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender


test = Test()
print(test.get_name())
