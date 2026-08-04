# 📊 Day 4 - AI/ML Internship (HisabDo)

## 🎯 Task: Student Performance Prediction (Pass / Fail)

This project demonstrates a complete **Machine Learning Classification** workflow using **Logistic Regression** to predict whether a student will **Pass** or **Fail** based on academic performance.

---

# 📋 Project Workflow

The project follows these steps:

1. Load Dataset
2. Clean Data
3. Select Features
4. Create Target Column (Pass = 1, Fail = 0)
5. Split Data into Training & Testing Sets
6. Train Logistic Regression Model
7. Make Predictions
8. Evaluate Model Performance

Additionally, the project generates visualizations including:

- Confusion Matrix
- Feature Distribution
- Correlation Heatmap

---

# 📂 Project Structure

```text
day_4/
│
├── data/
│   └── student_performance.csv
│
├── visuals/
│   ├── confusion_matrix.png
│   ├── feature_distribution.png
│   └── correlation_heatmap.png
│
├── student_performance_prediction.py
├── evaluation_results.txt
└── README.md
```

---

# 📦 Required Libraries

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

# 🚀 Run the Project

```bash
python student_performance_prediction.py
```

---

# 💻 Source Code

```python
"""
==============================================================
 Day 4 - AI/ML Internship (HisabDo)
 Task: Student Performance Prediction (Pass / Fail)
==============================================================

This script follows the exact steps required by the task:
    1. Load dataset
    2. Clean data
    3. Select useful features
    4. Create target column (Pass = 1, Fail = 0)
    5. Train/Test split
    6. Train Logistic Regression model
    7. Make predictions
    8. Evaluate (Accuracy, Confusion Matrix, Classification Report)
    + 3 visualizations saved to /visuals

Run:
    python student_performance_prediction.py
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
)

# STEP 0: Set Working Directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
os.makedirs("visuals", exist_ok=True)

# STEP 1: Load Dataset
print("STEP 1: Loading dataset...")
df = pd.read_csv("data/student_performance.csv")
print(f"Raw shape: {df.shape}")
print(df.head())

# STEP 2: Clean Data
before = df.shape[0]
df = df.drop_duplicates()

numeric_cols = [
    "Attendance",
    "Assignment_Score",
    "Midterm_Score",
    "Final_Score"
]

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# STEP 3: Feature Selection
features = [
    "Attendance",
    "Assignment_Score",
    "Midterm_Score",
    "Final_Score"
]

X = df[features]

# STEP 4: Create Target
df["Target"] = df["Result"].map({
    "Pass": 1,
    "Fail": 0
})

y = df["Target"]

# STEP 5: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# STEP 6: Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# STEP 7: Predictions
y_pred = model.predict(X_test)

# STEP 8: Evaluation
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

report = classification_report(
    y_test,
    y_pred,
    target_names=["Fail", "Pass"]
)

print("Accuracy:", accuracy)
print(cm)
print(report)

# Save Evaluation Report
with open("evaluation_results.txt", "w") as f:
    f.write(report)

# Visualization 1
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
)
disp.plot(cmap="Blues")
plt.savefig("visuals/confusion_matrix.png")
plt.close()

# Visualization 2
fig, axes = plt.subplots(2, 2, figsize=(10,8))
axes = axes.flatten()

for i, col in enumerate(features):
    sns.boxplot(
        data=df,
        x="Result",
        y=col,
        hue="Result",
        ax=axes[i],
        palette="Set2",
        legend=False
    )

plt.tight_layout()
plt.savefig("visuals/feature_distribution.png")
plt.close()

# Visualization 3
corr = df[features + ["Target"]].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.savefig("visuals/correlation_heatmap.png")
plt.close()

print("Project Completed Successfully!")
```

---

# 📊 Output Files

After successful execution, the following files are generated:

```text
evaluation_results.txt

visuals/
├── confusion_matrix.png
├── feature_distribution.png
└── correlation_heatmap.png
```

---

# 📈 Model Evaluation

The model is evaluated using:

- ✅ Accuracy Score
- ✅ Confusion Matrix
- ✅ Classification Report

---

# 📉 Visualizations

The project automatically generates:

- 📊 Confusion Matrix
- 📦 Feature Distribution (Box Plots)
- 🔥 Correlation Heatmap

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

---
# output of the above code 
## ✅ Step 1: Loading Dataset

**Raw Shape:** `(301, 6)`

| Student_ID | Attendance | Assignment_Score | Midterm_Score | Final_Score | Result |
|------------|-----------:|-----------------:|--------------:|------------:|--------|
| S001 | 82.5 | 55.1 | 80.1 | 67.4 | Pass |
| S002 | 72.9 | 59.9 | 46.6 | 52.1 | Pass |
| S003 | 84.7 | 83.5 | 82.4 | 60.6 | Pass |
| S004 | 97.8 | 81.0 | 92.1 | 85.6 | Pass |
| S005 | 71.5 | 69.6 | 73.3 | 63.8 | Pass |

---

## ✅ Step 2: Cleaning Data

- Removed **1 duplicate row**
- Handled missing values successfully

### Missing Values Before Cleaning

| Column | Missing Values |
|--------|---------------:|
| Attendance | 2 |
| Assignment_Score | 1 |
| Midterm_Score | 1 |
| Final_Score | 2 |

### Missing Values After Cleaning

| Column | Missing Values |
|--------|---------------:|
| Attendance | 0 |
| Assignment_Score | 0 |
| Midterm_Score | 0 |
| Final_Score | 0 |

---

## ✅ Step 3: Selecting Features

The following features were used for model training:

- Attendance
- Assignment_Score
- Midterm_Score
- Final_Score

---

## ✅ Step 4: Creating Target Column

| Result | Target |
|--------|-------:|
| Pass | 1 |
| Pass | 1 |
| Pass | 1 |
| Pass | 1 |
| Pass | 1 |

### Class Distribution

| Class | Count |
|-------|------:|
| Pass (1) | 282 |
| Fail (0) | 18 |

---

## ✅ Step 5: Train-Test Split

- **Training Samples:** 240
- **Testing Samples:** 60

Split Ratio:

- **80% Training**
- **20% Testing**

---

## ✅ Step 6: Model Training

**Algorithm Used:**

- Logistic Regression

Model Status:

✅ Successfully Trained

---

## ✅ Step 7: Predictions

| Attendance | Assignment | Midterm | Final | Actual | Predicted |
|-----------:|-----------:|---------:|-------:|-------:|----------:|
| 74.52 | 54.7 | 57.8 | 55.5 | 1 | 1 |
| 87.30 | 56.2 | 49.4 | 22.2 | 0 | 1 |
| 57.10 | 77.2 | 54.1 | 74.2 | 1 | 1 |
| 91.20 | 44.8 | 66.9 | 100.0 | 1 | 1 |
| 88.80 | 67.2 | 53.9 | 16.9 | 1 | 1 |
| 76.00 | 33.3 | 45.4 | 26.6 | 0 | 0 |
| 67.10 | 87.1 | 79.2 | 55.6 | 1 | 1 |
| 66.00 | 83.9 | 69.5 | 58.0 | 1 | 1 |
| 86.70 | 82.1 | 50.5 | 77.7 | 1 | 1 |
| 90.90 | 44.7 | 63.9 | 46.2 | 1 | 1 |

---

# ✅ Step 8: Model Evaluation

## Accuracy

**95.00%**

---

## Confusion Matrix

```
[[ 2  2 ]
 [ 1 55 ]]
```

---

## Classification Report

| Class | Precision | Recall | F1-Score | Support |
|------|----------:|-------:|---------:|--------:|
| Fail | 0.67 | 0.50 | 0.57 | 4 |
| Pass | 0.96 | 0.98 | 0.97 | 56 |

### Overall Performance

| Metric | Value |
|--------|------:|
| Accuracy | 95% |
| Macro Avg Precision | 0.82 |
| Macro Avg Recall | 0.74 |
| Macro Avg F1-Score | 0.77 |
| Weighted Avg Precision | 0.95 |
| Weighted Avg Recall | 0.95 |
| Weighted Avg F1-Score | 0.95 |

---

# 📈 Generated Visualizations

The following visualizations were successfully created:

- ✅ Confusion Matrix
- ✅ Feature Distribution
- ✅ Correlation Heatmap

Saved Files:

```
visuals/
│── confusion_matrix.png
│── feature_distribution.png
│── correlation_heatmap.png
```

---

# 📁 Output Files

- `evaluation_results.txt`
- `visuals/confusion_matrix.png`
- `visuals/feature_distribution.png`
- `visuals/correlation_heatmap.png`

---

# 🎉 Conclusion

The Logistic Regression model was successfully trained and evaluated on the student performance dataset.

### Final Results

- **Algorithm:** Logistic Regression
- **Training Samples:** 240
- **Testing Samples:** 60
- **Accuracy:** **95.00%**
- **Visualizations Generated:** 3
- **Evaluation Report Saved:** ✅

The project demonstrates a complete Machine Learning workflow including data preprocessing, feature selection, model training, prediction, evaluation, and visualization.




# 👨‍💻 Author

**Qasim Shahzad**

**AI/ML Internship – HisabDo**

**Day 4 Project**







