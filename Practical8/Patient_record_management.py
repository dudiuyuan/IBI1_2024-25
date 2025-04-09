class patients:
    def __init__(self, name, age, date, medical_history):
        self.name = name
        self.age = age
        self.date = date
        self.medical_history = medical_history
    
    def print_details(self):
        print(f"Patient Name:{self.name}, Age: {self.age}, date of latest adimission: {self.date}, medical_history: {self.medical_history}")

# for example
p = patients("John", 25, "2023-10-05", "Diabetes")
p.print_details()  # output：John, 25, 2023-10-05, Diabetes