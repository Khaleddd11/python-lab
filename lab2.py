#vowels
word = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for char in word:
    if char not in vowels:
        result += char

print(result)

#count
sentence = "This is javaScript"
target_letter = "i"
locations = []

for i in range(len(sentence)):
    if sentence[i] == target_letter:
        locations.append(i)

print(locations)

#multiplication
number = int(input("Enter a number: "))
table = []

for i in range(1, number + 1):
    row = []
    for j in range(1, i + 1):
        row.append(i * j)
    table.append(row)

print(table)

#area
def calculate_area():
    shape = input("Enter shape (t, r, s, c): ")
    
    if shape == "t":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Triangle Area:", area)
        
    elif shape == "r":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        area = width * height
        print("Rectangle Area:", area)
        
    elif shape == "s":
        side = float(input("Enter side: "))
        area = side ** 2 # Using exponent operator from slides
        print("Square Area:", area)
        
    elif shape == "c":
        radius = float(input("Enter radius: "))
        area = 3.14159 * (radius ** 2) 
        print("Circle Area:", area)
        
    else:
        print("unknown shape")

calculate_area()

#dictionnary
names = ["ahmed", "fatma", "Ibrahim"]
alpha_dict = {}

for name in names:
    first_letter = name[0].lower() 
    
    if first_letter in alpha_dict:
        alpha_dict[first_letter].append(name)
    else:
        alpha_dict[first_letter] = [name]

print(alpha_dict)

#mario
number = int(input("Enter a number: "))

for i in range(number):
    spaces = " " * (number - i)
    stars = "*" * (i + 1)
    print(spaces + stars)