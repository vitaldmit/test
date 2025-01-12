# Example test class
class Test:
    def __init__(self):
        self.name = "Test"
        self.age = 20
        self.gender = "Male"
        self.address = "123 Main St"
        self.phone = "555-555-5555"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone


test = Test()
print(test.get_name())
