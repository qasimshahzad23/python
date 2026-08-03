# important libraries

import pandas as pd
import matplotlib.pyplot as plt

# dataset loading 
df = pd.read_csv("student_dataset.csv")

print("=" * 60)
print("STUDENT PERFORMANCE DATASET")
print("=" * 60)

print(df.head())
# basic information about the dataset
print("\nDataset Information")
print(df.info())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nSummary")
print(df.describe())

# average score in each subject
print("\nAverage Scores")

print("Assignment Average:",
      df["Assignment Score"].mean())

print("Midterm Average:",
      df["Midterm Score"].mean())

print("Final Average:",
      df["Final Score"].mean())
# highest and lowest scores in each subject
print("\nHighest Final Score")

print(df[df["Final Score"] ==
      df["Final Score"].max()])

print("\nLowest Final Score")

print(df[df["Final Score"] ==
      df["Final Score"].min()])
# attandance below 75% students
low_attendance = df[df["Attendance"] < 75]

print("\nStudents Below 75% Attendance")

print(low_attendance)
# student at risk of falling 
risk_students = df[df["Final Score"] < 50]

print("\nStudents At Risk")

print(risk_students)
# average score by course 
course_average = df.groupby("Course")["Final Score"].mean()

print("\nAverage Final Score by Course")

print(course_average)
# relation between attandance and final score 
correlation = df["Attendance"].corr(df["Final Score"])

print("\nCorrelation")

print(correlation)
# check the missing values
print(df.isnull().sum())

# replace missing values
df.fillna(df.mean(numeric_only=True), inplace=True)
# remove duplocat value
df.drop_duplicates(inplace=True)

# score distribution chart 
plt.figure(figsize=(8,5))

plt.hist(df["Final Score"], bins=10)

plt.title("Final Score Distribution")
plt.xlabel("Final Score")
plt.ylabel("Students")

plt.show()
# avrage score by coures 
course_average.plot(kind="bar")

plt.title("Average Final Score By Course")
plt.xlabel("Course")
plt.ylabel("Average Score")

plt.show()

# attandance vs final score 
plt.figure(figsize=(8,5))

plt.scatter(df["Attendance"],
            df["Final Score"])

plt.title("Attendance vs Final Score")

plt.xlabel("Attendance")

plt.ylabel("Final Score")

plt.show()