from car import Car
from employee import Employee
from office import Office


# Samy has a fiat 128 Car
fiat128 = Car(name="Fiat 128", fuelRate=100, velocity=0)

# Samy is an Employee (Distance is 20km to ITI)
samy = Employee(
    name="Samy", 
    money=500, 
    mood="happy", 
    healthRate=100, 
    emp_id=1, 
    car=fiat128, 
    email="samy@iti.com", 
    salary=2000, 
    distanceToWork=20
)

# ITI is an Office
iti = Office(name="ITI Smart Village")

# ITI has Samy as an employee
iti.hire(samy)

# Samy leaves at 8:30 AM (8.5) and drives at 60km/h
samy.drive(distance=20, velocity=60)
iti.check_lateness(empId=1, moveHour=8.5)

# Test Email Generation
print("\n--- Testing Email Generation ---")
samy.send_mail(
    to="manager@mail.com", 
    subject="Lab 4 Submission", 
    msg="This is an email template", 
    receiver_name="Mohamed"
)

# Save Office data as JSON
iti.save_office_data()