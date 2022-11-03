# calculator blueprint class.
class PythonCalc:

    # constructor method.
    def __init__(self, first_number, next_number):
        self.first_number = first_number
        self.next_number = next_number

    # operation methods.
    def add(self):
        return self.first_number + self.next_number

    def subtract(self):
        return self.first_number - self.next_number

    def multiply(self):
        return self.first_number * self.next_number

    def divide(self):
        return self.first_number / self.next_number

# end of PythonCalc class
