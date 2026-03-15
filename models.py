from datetime import datetime

class from datetime import datetime

class Patient:
    def __init__(self, name, age, illness):
        self.name = name
        self.age = age
        self.illness = illness
        self.admission_time = datetime.now()

    def display(self):
        return f"{self.name} - {self.illness}"