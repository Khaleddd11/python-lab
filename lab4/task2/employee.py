import re
from person import Person
from my_email import export_email_file

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value if value >= 1000 else 1000

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if re.match(r"[^@]+@[^@]+\.[^@]+", value):
            self._email = value
        else:
            raise ValueError("Invalid email format.")

    def work(self, hours):
        if hours == 8:
            self.mood = Person.moods[0] # happy
        elif hours > 8:
            self.mood = Person.moods[1] # tired
        else:
            self.mood = Person.moods[2] # lazy

    def drive(self, distance, velocity=60): 
        self.car.run(velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount

    def send_mail(self, to, subject, msg, receiver_name):
        filename = f"email_{receiver_name}.txt"
        with open(filename, "w") as file:
            file.write(f"From: {self.email}\n")
            file.write(f"To: {to}\n")
            file.write(f"Hi, {receiver_name}\n")
            file.write(f"{msg}\n")
        print(f"Email file '{filename}' has been generated.")

    def send_mail(self, to, subject, msg, receiver_name):
        export_email_file(self.email, to, subject, msg, receiver_name)