class patients:
    def __init__(self, name, age, date, medical_history):
        self.name = name
        self.age = age
        self.date = date
        self.medical_history = medical_history
    
    def print_details(self):
        print(f"Patient Name:{self.name}, Age: {self.age}, date of latest adimission: {self.date}, medical_history: {self.medical_history}")

# for example
p1 = patients("John", 25, "2021-10-05", "Diabetes")
p1.print_details()  # output：Patient Name:John, Age: 25, date of latest adimission: 2021-10-05, medical_history: Diabetes