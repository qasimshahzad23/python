# Python Basics Practice

This project contains basic Python programs for beginners. It demonstrates the use of:

- User Input
- Lists
- If-Else Conditions
- For Loops
- While Loops
- Functions
- Calculator Program

---

# 1. Taking User Input

This program takes user information and stores it in a list.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
qualification = input("Enter your qualification: ")

userdata = [name, age, address, qualification]
print(userdata)
```

---

# 2. If-Else Condition

Checks whether the user is an adult or not.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
qualification = input("Enter your qualification: ")

userdata = [name, age, address, qualification]

if age < 18:
    print("You are so young.")
else:
    print("You are an adult.")
```

---

# 3. For Loop with List

Prints each item stored in a list.

```python
name = "Qasim Shahzad"
age = 18
address = "Karachi"
qualification = "Fresh Graduate"

userdata = [name, age, address, qualification]

for item in userdata:
    print(item)
```

---

# 4. Using range() in For Loop

Prints numbers from 0 to 4.

```python
for i in range(5):
    print(i)
```

Prints numbers from 0 to 9.

```python
for i in range(10):
    print(i)
```

---

# 5. While Loop

Prints the list once using a while loop.

```python
name = "Qasim Shahzad"
age = 18
address = "Karachi"
qualification = "Fresh Graduate"

userdata = [name, age, address, qualification]

while userdata:
    print(userdata)
    break
```

---

# 6. Function to Store User Data

Creates a function that returns user information.

```python
def userdata():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    qualification = input("Enter your qualification: ")

    userdata = [name, age, address, qualification]
    return userdata

print(userdata())
```

---

# 7. Function Without Parameters

Displays predefined user information.

```python
def user_info():
    name = "Qasim Shahzad"
    age = 23
    my_address = "Islamabad"

    print("My Name:", name)
    print("My Age:", age)
    print("My Address:", my_address)

user_info()
```

---

# 8. Addition of Two Numbers

Adds two numbers entered by the user.

```python
def added(num1, num2):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 + num2
    print("Result:", result)

added(5, 6)
```

---

# 9. Simple Calculator

Performs basic arithmetic operations.

Supported Operators:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

```python
def simple_cal():
    symbol = input("Enter the operator (+, -, *, /): ")
    entry_1 = int(input("Enter first number: "))
    entry_2 = int(input("Enter second number: "))

    while True:

        if symbol == '+':
            print("Result:", entry_1 + entry_2)

        elif symbol == '-':
            print("Result:", entry_1 - entry_2)

        elif symbol == '*':
            print("Result:", entry_1 * entry_2)

        elif symbol == '/':
            print("Result:", entry_1 / entry_2)

        else:
            print("Invalid Operator")

        choice = input("Do you want to continue? (y/n): ").lower()

        if choice == 'n':
            break

        symbol = input("Enter the operator (+, -, *, /): ")
        entry_1 = int(input("Enter first number: "))
        entry_2 = int(input("Enter second number: "))

simple_cal()
```

---

# Topics Covered

- Variables
- User Input
- Data Types
- Lists
- If-Else Statements
- For Loops
- While Loops
- Functions
- Parameters
- Return Statements
- Simple Calculator Project

---

# Author

**Qasim Shahzad**

Learning Python Programming 🚀