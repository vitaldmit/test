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
    

test = Test()
print(test.get_name())