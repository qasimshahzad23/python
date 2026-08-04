"""
generate_dataset.py
--------------------
Creates a synthetic but realistic 'student performance' dataset for Day 4
of the AI/ML Internship task.

Columns:
    Student_ID         - unique id
    Attendance          - % attendance (0-100)
    Assignment_Score    - score out of 100
    Midterm_Score       - score out of 100
    Final_Score         - score out of 100
    Result              - "Pass" / "Fail" (derived from average score + attendance rule)

Run:
    python generate_dataset.py
Output:
    student_performance.csv  (saved in the same folder)
"""

import numpy as np
import pandas as pd

np.random.seed(42)          # so results are reproducible every time
N_STUDENTS = 300

# ---- 1. Generate realistic feature values -------------------------------
attendance = np.clip(np.random.normal(75, 15, N_STUDENTS), 30, 100)
assignment_score = np.clip(np.random.normal(70, 18, N_STUDENTS), 0, 100)
midterm_score = np.clip(np.random.normal(65, 20, N_STUDENTS), 0, 100)
final_score = np.clip(np.random.normal(60, 20, N_STUDENTS), 0, 100)

# ---- 2. Build a "true" underlying rule to decide Pass/Fail ---------------
# Weighted average of all four factors (attendance counts too, since
# students who don't attend usually perform worse).
weighted_avg = (
    0.15 * attendance +
    0.20 * assignment_score +
    0.30 * midterm_score +
    0.35 * final_score
)

# Add a little random noise so the data isn't perfectly separable
# (real life is messy - this makes the ML problem realistic).
noise = np.random.normal(0, 4, N_STUDENTS)
final_metric = weighted_avg + noise

# Pass if the weighted score crosses 50, AND attendance is not extremely low
result = np.where((final_metric >= 50) & (attendance >= 40), "Pass", "Fail")

# ---- 3. Assemble dataframe ------------------------------------------------
df = pd.DataFrame({
    "Student_ID": [f"S{str(i+1).zfill(3)}" for i in range(N_STUDENTS)],
    "Attendance": attendance.round(1),
    "Assignment_Score": assignment_score.round(1),
    "Midterm_Score": midterm_score.round(1),
    "Final_Score": final_score.round(1),
    "Result": result
})

# ---- 4. Inject a few missing values + a duplicate row (to make cleaning meaningful) ----
missing_idx = np.random.choice(df.index, size=6, replace=False)
for idx in missing_idx:
    col = np.random.choice(["Attendance", "Assignment_Score", "Midterm_Score", "Final_Score"])
    df.loc[idx, col] = np.nan

df = pd.concat([df, df.iloc[[0]]], ignore_index=True)  # duplicate row for cleaning practice

df.to_csv("student_performance.csv", index=False)
print("Dataset created: student_performance.csv")
print(df.head())
print("\nShape:", df.shape)
print("Missing values:\n", df.isnull().sum())
