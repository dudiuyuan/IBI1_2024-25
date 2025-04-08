class patients:
    def __init__(self, name, age, date, medical_history):
        self.name = name
        self.age = age
        self.date = date
        self.medical_history = medical_history
    
    def print_details(self):
        print(f"{self.name}, {self.age}, {self.date}, {self.medical_history}")

# for example
p = patients("John", 25, "2023-10-05", "Diabetes")
p.print_details()  # output：John, 25, 2023-10-05, Diabetes