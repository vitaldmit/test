# Example test class
class Test:
    def __init__(self):
        self.name = "Test"
        self.age = 20
        self.gender = "Male"
        self.height = 170
        self.weight = 60
        self.bmi = 20
        self.bmi_category = "Normal"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_bmi(self):
        return self.bmi


test = Test()
print(test.get_name())
