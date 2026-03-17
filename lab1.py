# Task 1
number = input("Enter the number: ")
start = input("Enter the start of range: ")
end = input("Enter the end of range: ")

if not number.isdigit() or not start.isdigit() or not end.isdigit():
    print("Invalid input: please enter numbers only.")
else:
    number = int(number)
    start = int(start)
    end = int(end)

    if start > end:
        print("Invalid range: start should be less than or equal to end.")
    else:
        print(number >= start and number <= end)


# Task 2
age = int(input("Enter your age: "))
have_coupon = input("Do you have a coupon? (True/False): ")

have_coupon = have_coupon == "True"

print(age < 18 or age > 65 or have_coupon)


# Task 3
name = input("Enter your name: ")

if name == "":
    print("Invalid input: name cannot be empty.")
else:
    greeting = "Hello, " + name + "!"
    print(greeting)


# Task 4
full_name = input("Enter your full name: ")

names = full_name.split()
initials = names[0][0] + names[-1][0]
print(initials)


# Task 5
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("{} is {} years old.".format(name, age))