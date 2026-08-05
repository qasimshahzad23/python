"""
==============================================================
 Day 5 - AI/ML Internship (HisabDo)

 Task:
 Model Comparison using Multiple Classification Algorithms

 Models Used:
 1. Logistic Regression
 2. Decision Tree Classifier

==============================================================

Project Steps

1. Load Dataset
2. Clean Dataset
3. Select Features
4. Create Target Column
5. Split Dataset
6. Train Logistic Regression
7. Train Decision Tree
8. Compare Both Models
9. Generate Visualizations
10. Save Results

Run:
    python student_model_comparison.py
"""

# ==========================================================
# Import Libraries
# ==========================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
)

# ==========================================================
# STEP 0
# Set Current Working Directory
# ==========================================================

script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)

# Create visuals folder automatically
os.makedirs("visuals", exist_ok=True)

print("=" * 60)
print("DAY 5 - MODEL COMPARISON")
print("=" * 60)

# ==========================================================
# STEP 1
# Load Dataset
# ==========================================================

print("\nSTEP 1: Loading Dataset...\n")

df = pd.read_csv("data/student_performance.csv")

print("Dataset Loaded Successfully\n")

print("First Five Rows\n")

print(df.head())

print("\nDataset Shape")

print(df.shape)

print("\nColumn Names")

print(df.columns.tolist())

# ==========================================================
# STEP 2
# Clean Dataset
# ==========================================================

print("\nSTEP 2: Cleaning Dataset...\n")

# Remove duplicate rows

before = df.shape[0]

df = df.drop_duplicates()

after = df.shape[0]

print(f"Removed {before-after} duplicate rows.\n")

# Numeric Columns

numeric_columns = [

    "Attendance",

    "Assignment_Score",

    "Midterm_Score",

    "Final_Score"

]

print("Missing Values Before Cleaning\n")

print(df[numeric_columns].isnull().sum())

# Fill Missing Values

for column in numeric_columns:

    df[column] = df[column].fillna(

        df[column].mean()

    )

print("\nMissing Values After Cleaning\n")

print(df[numeric_columns].isnull().sum())

# ==========================================================
# STEP 3
# Feature Selection
# ==========================================================

print("\nSTEP 3: Selecting Features...\n")

features = [

    "Attendance",

    "Assignment_Score",

    "Midterm_Score",

    "Final_Score"

]

X = df[features]

print("Selected Features\n")

print(features)

# ==========================================================
# STEP 4
# Create Target Column
# ==========================================================

print("\nSTEP 4: Creating Target Column...\n")

df["Target"] = df["Result"].map({

    "Pass":1,

    "Fail":0

})

y = df["Target"]

print(df[["Result","Target"]].head())

print("\nClass Distribution\n")

print(y.value_counts())

# ==========================================================
# STEP 5
# Split Dataset
# ==========================================================

print("\nSTEP 5: Splitting Dataset...\n")

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

print("Training Samples :",len(X_train))

print("Testing Samples  :",len(X_test))

print("\nData Preparation Completed Successfully.")
# ==========================================================
# STEP 6
# Train Logistic Regression Model
# ==========================================================

print("\n" + "=" * 60)
print("STEP 6: Training Logistic Regression Model")
print("=" * 60)

logistic_model = LogisticRegression(max_iter=1000)

logistic_model.fit(X_train, y_train)

print("✅ Logistic Regression Model Trained Successfully.\n")


# ==========================================================
# STEP 7
# Train Decision Tree Model
# ==========================================================

print("=" * 60)
print("STEP 7: Training Decision Tree Model")
print("=" * 60)

decision_tree_model = DecisionTreeClassifier(
    random_state=42
)

decision_tree_model.fit(X_train, y_train)

print("✅ Decision Tree Model Trained Successfully.\n")


# ==========================================================
# STEP 8
# Generate Predictions
# ==========================================================

print("=" * 60)
print("STEP 8: Making Predictions")
print("=" * 60)

# Logistic Regression Prediction

logistic_prediction = logistic_model.predict(X_test)

# Decision Tree Prediction

decision_tree_prediction = decision_tree_model.predict(X_test)

print("Predictions Generated Successfully.\n")


# ==========================================================
# STEP 9
# Logistic Regression Evaluation
# ==========================================================

print("=" * 60)
print("LOGISTIC REGRESSION RESULTS")
print("=" * 60)

log_accuracy = accuracy_score(
    y_test,
    logistic_prediction
)

log_precision = precision_score(
    y_test,
    logistic_prediction
)

log_recall = recall_score(
    y_test,
    logistic_prediction
)

log_f1 = f1_score(
    y_test,
    logistic_prediction
)

log_cm = confusion_matrix(
    y_test,
    logistic_prediction
)

print(f"Accuracy : {log_accuracy:.4f}")
print(f"Precision: {log_precision:.4f}")
print(f"Recall   : {log_recall:.4f}")
print(f"F1 Score : {log_f1:.4f}")

print("\nConfusion Matrix")

print(log_cm)

print("\nClassification Report\n")

print(
    classification_report(
        y_test,
        logistic_prediction,
        target_names=["Fail", "Pass"]
    )
)


# ==========================================================
# STEP 10
# Decision Tree Evaluation
# ==========================================================

print("=" * 60)
print("DECISION TREE RESULTS")
print("=" * 60)

tree_accuracy = accuracy_score(
    y_test,
    decision_tree_prediction
)

tree_precision = precision_score(
    y_test,
    decision_tree_prediction
)

tree_recall = recall_score(
    y_test,
    decision_tree_prediction
)

tree_f1 = f1_score(
    y_test,
    decision_tree_prediction
)

tree_cm = confusion_matrix(
    y_test,
    decision_tree_prediction
)

print(f"Accuracy : {tree_accuracy:.4f}")
print(f"Precision: {tree_precision:.4f}")
print(f"Recall   : {tree_recall:.4f}")
print(f"F1 Score : {tree_f1:.4f}")

print("\nConfusion Matrix")

print(tree_cm)

print("\nClassification Report\n")

print(
    classification_report(
        y_test,
        decision_tree_prediction,
        target_names=["Fail", "Pass"]
    )
)


# ==========================================================
# STEP 11
# Create Comparison Table
# ==========================================================

print("=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

comparison = pd.DataFrame({

    "Model": [

        "Logistic Regression",

        "Decision Tree"

    ],

    "Accuracy": [

        round(log_accuracy, 4),

        round(tree_accuracy, 4)

    ],

    "Precision": [

        round(log_precision, 4),

        round(tree_precision, 4)

    ],

    "Recall": [

        round(log_recall, 4),

        round(tree_recall, 4)

    ],

    "F1 Score": [

        round(log_f1, 4),

        round(tree_f1, 4)

    ]

})

print(comparison)


# Save Comparison Table

comparison.to_csv(

    "model_comparison.csv",

    index=False

)

print("\n✅ model_comparison.csv Saved Successfully.")
# ==========================================================
# STEP 12
# Save Evaluation Results
# ==========================================================

print("\n" + "=" * 60)
print("STEP 12: Saving Evaluation Results")
print("=" * 60)

with open("evaluation_results.txt", "w") as file:

    file.write("=" * 70 + "\n")
    file.write("DAY 5 - MODEL COMPARISON RESULTS\n")
    file.write("=" * 70 + "\n\n")

    file.write("LOGISTIC REGRESSION\n")
    file.write("-" * 70 + "\n")
    file.write(f"Accuracy : {log_accuracy:.4f}\n")
    file.write(f"Precision: {log_precision:.4f}\n")
    file.write(f"Recall   : {log_recall:.4f}\n")
    file.write(f"F1 Score : {log_f1:.4f}\n\n")

    file.write("Confusion Matrix\n")
    file.write(str(log_cm))
    file.write("\n\n")

    file.write(classification_report(
        y_test,
        logistic_prediction,
        target_names=["Fail", "Pass"]
    ))

    file.write("\n\n")

    file.write("=" * 70 + "\n")
    file.write("DECISION TREE\n")
    file.write("=" * 70 + "\n\n")

    file.write(f"Accuracy : {tree_accuracy:.4f}\n")
    file.write(f"Precision: {tree_precision:.4f}\n")
    file.write(f"Recall   : {tree_recall:.4f}\n")
    file.write(f"F1 Score : {tree_f1:.4f}\n\n")

    file.write("Confusion Matrix\n")
    file.write(str(tree_cm))
    file.write("\n\n")

    file.write(classification_report(
        y_test,
        decision_tree_prediction,
        target_names=["Fail", "Pass"]
    ))

print("evaluation_results.txt saved successfully.\n")


# ==========================================================
# STEP 13
# Logistic Regression Confusion Matrix
# ==========================================================

print("=" * 60)
print("Generating Logistic Regression Confusion Matrix")
print("=" * 60)

disp = ConfusionMatrixDisplay(
    confusion_matrix=log_cm,
    display_labels=["Fail", "Pass"]
)

disp.plot(cmap="Blues")

plt.title("Logistic Regression Confusion Matrix")

plt.tight_layout()

plt.savefig(
    "visuals/logistic_confusion_matrix.png",
    dpi=150
)

plt.close()

print("Saved: visuals/logistic_confusion_matrix.png")


# ==========================================================
# STEP 14
# Decision Tree Confusion Matrix
# ==========================================================

disp = ConfusionMatrixDisplay(
    confusion_matrix=tree_cm,
    display_labels=["Fail", "Pass"]
)

disp.plot(cmap="Greens")

plt.title("Decision Tree Confusion Matrix")

plt.tight_layout()

plt.savefig(
    "visuals/decision_tree_confusion_matrix.png",
    dpi=150
)

plt.close()

print("Saved: visuals/decision_tree_confusion_matrix.png")


# ==========================================================
# STEP 15
# Model Comparison Bar Chart
# ==========================================================

print("=" * 60)
print("Generating Model Comparison Chart")
print("=" * 60)

comparison_plot = comparison.set_index("Model")

comparison_plot.plot(
    kind="bar",
    figsize=(9,6)
)

plt.title("Model Performance Comparison")

plt.ylabel("Score")

plt.xlabel("Models")

plt.xticks(rotation=0)

plt.grid(axis="y")

plt.tight_layout()

plt.savefig(
    "visuals/model_comparison.png",
    dpi=150
)

plt.close()

print("Saved: visuals/model_comparison.png")


# ==========================================================
# STEP 16
# Decision Tree Feature Importance
# ==========================================================

print("=" * 60)
print("Generating Feature Importance")
print("=" * 60)

importance = pd.DataFrame({

    "Feature":features,

    "Importance":decision_tree_model.feature_importances_

})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

plt.figure(figsize=(8,5))

sns.barplot(
    data=importance,
    x="Importance",
    y="Feature",
    hue="Feature",
    palette="viridis",
    legend=False
)

plt.title("Decision Tree Feature Importance")

plt.tight_layout()

plt.savefig(
    "visuals/feature_importance.png",
    dpi=150
)

plt.close()

print("Saved: visuals/feature_importance.png")


# ==========================================================
# STEP 17
# Correlation Heatmap
# ==========================================================

print("=" * 60)
print("Generating Correlation Heatmap")
print("=" * 60)

plt.figure(figsize=(7,6))

corr = df[features + ["Target"]].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    "visuals/correlation_heatmap.png",
    dpi=150
)

plt.close()

print("Saved: visuals/correlation_heatmap.png")


# ==========================================================
# STEP 18
# Final Analysis
# ==========================================================

print("\n" + "=" * 70)
print("MODEL ANALYSIS")
print("=" * 70)

best_model = comparison.loc[
    comparison["Accuracy"].idxmax(),
    "Model"
]

print(f"\nBest Performing Model: {best_model}")

print("\nComparison Table\n")

print(comparison)

print("\nDataset Balance")

print(df["Target"].value_counts())

print("\nSuggestions")

print("1. Collect more student records.")
print("2. Balance Pass and Fail classes.")
print("3. Tune Decision Tree hyperparameters.")
print("4. Perform Feature Engineering.")
print("5. Try Random Forest or Gradient Boosting.")
print("6. Use Cross Validation for better evaluation.")


# ==========================================================
# STEP 19
# Project Completed
# ==========================================================

print("\n" + "=" * 70)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 70)

print("Generated Files:")

print("✔ model_comparison.csv")
print("✔ evaluation_results.txt")
print("✔ visuals/logistic_confusion_matrix.png")
print("✔ visuals/decision_tree_confusion_matrix.png")
print("✔ visuals/model_comparison.png")
print("✔ visuals/feature_importance.png")
print("✔ visuals/correlation_heatmap.png")

print("\nThank you for completing Day 5 of the AI/ML Internship!")