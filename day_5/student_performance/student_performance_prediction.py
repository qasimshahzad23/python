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
    + 2 visualizations saved to /visuals

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

# --------------------------------------------------------------
# STEP 0: Make sure we always run relative to THIS file's folder
# (fixes "FileNotFoundError" when run from VS Code Run button
#  or from a different working directory)
# --------------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
os.makedirs("visuals", exist_ok=True)   # create visuals/ if missing

# --------------------------------------------------------------
# STEP 1: Load the dataset
# --------------------------------------------------------------
print("STEP 1: Loading dataset...")
df = pd.read_csv("data/student_performance.csv")
print(f"Raw shape: {df.shape}")
print(df.head(), "\n")

# --------------------------------------------------------------
# STEP 2: Clean the data
# --------------------------------------------------------------
print("STEP 2: Cleaning data...")

# 2a. Remove exact duplicate rows
before = df.shape[0]
df = df.drop_duplicates()
print(f"Removed {before - df.shape[0]} duplicate row(s).")

# 2b. Handle missing values -> fill numeric columns with column mean
numeric_cols = ["Attendance", "Assignment_Score", "Midterm_Score", "Final_Score"]
print("Missing values before cleaning:\n", df[numeric_cols].isnull().sum())

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

print("Missing values after cleaning:\n", df[numeric_cols].isnull().sum(), "\n")

# --------------------------------------------------------------
# STEP 3: Select useful features
# --------------------------------------------------------------
print("STEP 3: Selecting features...")
features = ["Attendance", "Assignment_Score", "Midterm_Score", "Final_Score"]
X = df[features]
print("Features used:", features, "\n")

# --------------------------------------------------------------
# STEP 4: Create target column (Pass = 1, Fail = 0)
# --------------------------------------------------------------
print("STEP 4: Creating target column...")
df["Target"] = df["Result"].map({"Pass": 1, "Fail": 0})
y = df["Target"]
print(df[["Result", "Target"]].head(), "\n")
print("Class balance:\n", y.value_counts(), "\n")

# --------------------------------------------------------------
# STEP 5: Train / Test split
# --------------------------------------------------------------
print("STEP 5: Splitting into train/test sets (80/20)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Training samples: {X_train.shape[0]} | Testing samples: {X_test.shape[0]}\n")

# --------------------------------------------------------------
# STEP 6: Train a Logistic Regression model
# --------------------------------------------------------------
print("STEP 6: Training Logistic Regression model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
print("Model trained successfully.\n")

# --------------------------------------------------------------
# STEP 7: Make predictions on test data
# --------------------------------------------------------------
print("STEP 7: Making predictions on test data...")
y_pred = model.predict(X_test)
results_df = X_test.copy()
results_df["Actual"] = y_test.values
results_df["Predicted"] = y_pred
print(results_df.head(10), "\n")

# --------------------------------------------------------------
# STEP 8: Evaluate the model
# --------------------------------------------------------------
print("STEP 8: Evaluating model...")
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=["Fail", "Pass"])

print(f"Accuracy: {acc*100:.2f}%\n")
print("Confusion Matrix:\n", cm, "\n")
print("Classification Report:\n", report)

# Save a text report for the README / repo
with open("evaluation_results.txt", "w") as f:
    f.write("STUDENT PERFORMANCE PREDICTION - EVALUATION RESULTS\n")
    f.write("=" * 55 + "\n\n")
    f.write(f"Accuracy: {acc*100:.2f}%\n\n")
    f.write("Confusion Matrix:\n")
    f.write(np.array2string(cm) + "\n\n")
    f.write("Classification Report:\n")
    f.write(report)

# --------------------------------------------------------------
# VISUALIZATION 1: Confusion Matrix heatmap
# --------------------------------------------------------------
plt.figure(figsize=(5, 4))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fail", "Pass"])
disp.plot(cmap="Blues", values_format="d")
plt.title("Confusion Matrix - Logistic Regression")
plt.tight_layout()
plt.savefig("visuals/confusion_matrix.png", dpi=150)
plt.close()
print("Saved visuals/confusion_matrix.png")

# --------------------------------------------------------------
# VISUALIZATION 2: Feature distributions by Result (Pass vs Fail)
# --------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()
for i, col in enumerate(features):
    sns.boxplot(data=df, x="Result", y=col, hue="Result", ax=axes[i], palette="Set2", legend=False)
    axes[i].set_title(f"{col} by Result")
plt.tight_layout()
plt.savefig("visuals/feature_distribution.png", dpi=150)
plt.close()
print("Saved visuals/feature_distribution.png")

# --------------------------------------------------------------
# VISUALIZATION 3 (bonus): Correlation heatmap
# --------------------------------------------------------------
plt.figure(figsize=(6, 5))
corr = df[features + ["Target"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("visuals/correlation_heatmap.png", dpi=150)
plt.close()
print("Saved visuals/correlation_heatmap.png")

print("\nAll done! Check the 'visuals' folder and evaluation_results.txt")