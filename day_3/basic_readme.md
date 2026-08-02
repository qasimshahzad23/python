# 🐍 Python Basics - Day 1 Practice

This project contains basic Python concepts for beginners, including:

- Print statements
- Variables
- Operators
- Comments
- User Input
- Conditional Statements
- Type Conversion
- Functions
- Loops
- Math Library
- Types of Errors

---

# 1. Hello World

```python
print("hello world")

sum = 2 + 4
print(sum)
```

### Output

```
hello world
6
```

---

# 2. Python Operators

```python
print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 / 4)
print(2 % 4)
print(2 ** 4)
```

### Output

```
6
-2
8
0.5
2
16
```

---

# 3. Comments in Python

```python
# This is a comment

print("the # symbol is used for comment in python")
```

### Output

```
the # symbol is used for comment in python
```

---

# 4. User Input

## String Input

```python
name = input("Enter your name: ")

print("Hello", name)
print("Hello " + name)
```

### Example Output

```
Enter your name: Qasim
Hello Qasim
Hello Qasim
```

---

## Integer Input

```python
num = int(input("Enter a number: "))

print("The number you entered is:", num)
print("The number you entered is: " + str(num))
```

### Example Output

```
Enter a number: 12
The number you entered is: 12
The number you entered is: 12
```

---

# 5. Comparison Operators

```python
print(4 == 6)
print(4 != 6)
print(4 > 6)
print(4 < 6)
print(4 >= 6)
print(4 <= 6)
```

### Output

```
False
True
False
True
False
True
```

---

# 6. Type Conversion

```python
sum = 2 + 4

print(sum)

print(type(sum))

sum = float(sum)
print(type(sum))

sum = str(sum)
print(type(sum))
```

### Output

```
6
<class 'int'>
<class 'float'>
<class 'str'>
```

---

# 7. If, Elif, Else

```python
x = 10

if x < 10:
    print("The value of x is less than 10", x)

elif x > 10:
    print("The value of x is greater than 10", x)

else:
    print("The value of x is equal to 10", x)
```

### Output

```
The value of x is equal to 10 10
```

---

# 8. Functions

## Function Without Return

```python
def sum():
    sum = 2 + 4
    print("The sum of 2 and 4 is:", sum)

sum()
```

### Output

```
The sum of 2 and 4 is: 6
```

---

## Function With Return

```python
def add():
    sum = 2 + 4
    return sum

new_result = add()

print("The sum of 2 and 4 is:", new_result)
```

### Output

```
The sum of 2 and 4 is: 6
```

---

# 9. While Loop

```python
x = 0

while x < 10:
    print("The value of x is:", x)
    x += 1
```

### Output

```
The value of x is: 0
The value of x is: 1
The value of x is: 2
The value of x is: 3
The value of x is: 4
The value of x is: 5
The value of x is: 6
The value of x is: 7
The value of x is: 8
The value of x is: 9
```

---

# 10. For Loop

```python
for i in range(4, 12):
    print("The value of i is:", i)
```

### Output

```
The value of i is: 4
The value of i is: 5
The value of i is: 6
The value of i is: 7
The value of i is: 8
The value of i is: 9
The value of i is: 10
The value of i is: 11
```

---

# 11. Math Library

```python
import math

print("The value of pi is:", math.pi)
print("2 raised to the power 3 is:", math.pow(2, 3))
```

### Output

```
The value of pi is: 3.141592653589793
2 raised to the power 3 is: 8.0
```

---

# 12. Popular Python Libraries

```python
print(
    "Some important Python libraries are:",
    "NumPy",
    "Pandas",
    "Matplotlib",
    "Seaborn",
    "Scikit-learn"
)
```

### Output

```
Some important Python libraries are:
NumPy Pandas Matplotlib Seaborn Scikit-learn
```

---

# 13. Types of Errors in Python

```python
print(
    "Syntax Error, Runtime Error, Logical Error, and Semantic Error are the types of errors in Python."
)
```

### Output

# 📌 Output

```text
hello world
6
6
-2
8
0.5
2
16
the # symbole is used for comment in python
enter your name:qasim
hello qasim
helloqasim
enter the number you want to print:12
the number you entered is: 12
the number you entered is:12
False
True
False
True
False
True
6
the type of sum is: <class 'int'>
the type of sum is: <class 'float'>
the type of sum is: <class 'str'>
the value of x is equal to 10   10
the sum of 2 and 4 is: 6
the sum of 2 and 4 is: 6
the value of x is: 0
the value of x is: 1
the value of x is: 2
the value of x is: 3
the value of x is: 4
the value of x is: 5
the value of x is: 6
the value of x is: 7
the value of x is: 8
the value of x is: 9
the value of i is: 4
the value of i is: 5
the value of i is: 6
the value of i is: 7
the value of i is: 8
the value of i is: 9
the value of i is: 10
the value of i is: 11
the value of pi is: 3.141592653589793
the value of e is: 8.0
some important libraries in python are: numpy pandas matplotlib seaborn scikit-learn
syntax error, runtime error, logical error, semantic error are the types of error in python
```
Syntax Error, Runtime Error, Logical Error, and Semantic Error are the types of errors in Python.
```

---

# 📚 Concepts Covered

- ✅ Print Statements
- ✅ Variables
- ✅ Arithmetic Operators
- ✅ Comments
- ✅ User Input
- ✅ Type Casting
- ✅ Comparison Operators
- ✅ If, Elif, Else
- ✅ Functions
- ✅ While Loop
- ✅ For Loop
- ✅ Math Module
- ✅ Python Libraries
- ✅ Error Types

---

# 🚀 Author

**Qasim Shahzad**

Learning Python step by step and practicing core programming concepts.