import json

class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time_taken = distance / velocity
        arrival_time = moveHour + time_taken
        return arrival_time > targetHour

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp:
            targetHour = 9.0  # 9:00 AM
            velocity = emp.car.velocity if emp.car.velocity > 0 else 60 # fallback to avoid division by zero
            is_late = Office.calculate_lateness(targetHour, moveHour, emp.distanceToWork, velocity)
            
            if is_late:
                self.deduct(empId, 10)
                print(f"{emp.name} was late. Deducted 10 L.E.")
            else:
                self.reward(empId, 10)
                print(f"{emp.name} arrived on time. Rewarded 10 L.E.")

    def save_office_data(self, filename="iti_office.json"):
        data = {
            "office_name": self.name,
            "total_employees": Office.employeesNum,
            "employees": []
        }
        for emp in self.employees:
            emp_data = {
                "id": emp.id,
                "name": emp.name,
                "email": emp.email,
                "salary": emp.salary,
                "car": emp.car.name
            }
            data["employees"].append(emp_data)

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Office data saved to {filename}")