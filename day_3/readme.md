# 📊 Day 2 Task – Student Data Analysis
### AI/ML Internship | HisabDo

## 📌 Objective

This project demonstrates how to use **Python** and **Pandas** to store, manage, and analyze student data.

---

## 🛠 Technologies Used

- Python 3.x
- Pandas

---

## 📁 Dataset

The dataset contains information for **10 students** with the following fields:

- Name
- Age
- Course
- Marks

---

## 💻 Python Code

```python
# ==========================================
# Day 2 Task - Student Data Analysis
# AI/ML Internship | HisabDo
# ==========================================

# Import Pandas library
import pandas as pd

# ------------------------------------------
# Step 1: Create Student Dataset
# ------------------------------------------

students = [
    {"Name": "Ali", "Age": 20, "Course": "BSCS", "Marks": 85},
    {"Name": "Ahmed", "Age": 21, "Course": "BBA", "Marks": 67},
    {"Name": "Fatima", "Age": 19, "Course": "BSIT", "Marks": 92},
    {"Name": "Ayesha", "Age": 22, "Course": "BSE", "Marks": 75},
    {"Name": "Bilal", "Age": 20, "Course": "BSCS", "Marks": 58},
    {"Name": "Hassan", "Age": 23, "Course": "BBA", "Marks": 81},
    {"Name": "Zain", "Age": 21, "Course": "BSIT", "Marks": 69},
    {"Name": "Sara", "Age": 20, "Course": "BSE", "Marks": 95},
    {"Name": "Usman", "Age": 22, "Course": "BSCS", "Marks": 73},
    {"Name": "Mariam", "Age": 19, "Course": "BSIT", "Marks": 88},
]

# ------------------------------------------
# Step 2: Convert List into DataFrame
# ------------------------------------------

df = pd.DataFrame(students)

# ------------------------------------------
# 1. Display All Students
# ------------------------------------------

print("=" * 50)
print("ALL STUDENTS")
print("=" * 50)
print(df)

# ------------------------------------------
# 2. Display Students with Marks Above 70
# ------------------------------------------

print("\n" + "=" * 50)
print("STUDENTS WITH MARKS ABOVE 70")
print("=" * 50)

above_70 = df[df["Marks"] > 70]
print(above_70)

# ------------------------------------------
# 3. Calculate Average Marks
# ------------------------------------------

average_marks = df["Marks"].mean()

print("\n" + "=" * 50)
print(f"Average Marks: {average_marks:.2f}")

# ------------------------------------------
# 4. Student with Highest Marks
# ------------------------------------------

highest = df.loc[df["Marks"].idxmax()]

print("\n" + "=" * 50)
print("STUDENT WITH HIGHEST MARKS")
print("=" * 50)
print(highest)

# ------------------------------------------
# 5. Student with Lowest Marks
# ------------------------------------------

lowest = df.loc[df["Marks"].idxmin()]

print("\n" + "=" * 50)
print("STUDENT WITH LOWEST MARKS")
print("=" * 50)
print(lowest)

# ------------------------------------------
# 6. Total Number of Students
# ------------------------------------------

total_students = len(df)

print("\n" + "=" * 50)
print(f"Total Number of Students: {total_students}")
print("=" * 50)
```

---

## 📷 Program Output

```text
==================================================
ALL STUDENTS
==================================================
     Name  Age Course  Marks
0     Ali   20   BSCS     85
1   Ahmed   21    BBA     67
2  Fatima   19   BSIT     92
3  Ayesha   22    BSE     75
4   Bilal   20   BSCS     58
5  Hassan   23    BBA     81
6    Zain   21   BSIT     69
7    Sara   20    BSE     95
8   Usman   22   BSCS     73
9  Mariam   19   BSIT     88

==================================================
STUDENTS WITH MARKS ABOVE 70
==================================================
     Name  Age Course  Marks
0     Ali   20   BSCS     85
2  Fatima   19   BSIT     92
3  Ayesha   22    BSE     75
5  Hassan   23    BBA     81
7    Sara   20    BSE     95
8   Usman   22   BSCS     73
9  Mariam   19   BSIT     88

==================================================
Average Marks: 78.30

==================================================
STUDENT WITH HIGHEST MARKS
==================================================
Name      Sara
Age         20
Course     BSE
Marks       95
Name: 7, dtype: object

==================================================
STUDENT WITH LOWEST MARKS
==================================================
Name      Bilal
Age          20
Course     BSCS
Marks        58
Name: 4, dtype: object

==================================================
Total Number of Students: 10
==================================================
```

---

## 📌 Project Summary

This project demonstrates the basic use of **Pandas DataFrames** for data analysis. It stores student information, converts the data into a DataFrame, performs filtering and calculations, and displays useful insights such as the average marks, highest and lowest scoring students, and the total number of students.

---

## 👨‍💻 Author

**Qasim Shahzad**

AI/ML Internship – HisabDo
