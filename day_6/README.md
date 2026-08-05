# 📊 Day 5 – AI/ML Internship (HisabDo)

# Student Performance Prediction – Model Comparison

## 📌 Project Overview

This project was completed as part of the **Day 5 AI/ML Internship** at **HisabDo**.

The objective of this project is to compare two Machine Learning classification models for predicting whether a student will **Pass** or **Fail** based on academic performance.

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier

---

# 🎯 Objectives

- Load the student performance dataset
- Clean duplicate and missing data
- Select useful features
- Create the target variable
- Split the dataset into training and testing sets
- Train multiple classification models
- Compare model performance
- Generate evaluation reports
- Save visualizations

---

# 📂 Project Structure

```text
day_6/
│
├── data/
│   └── student_performance.csv
│
├── visuals/
│   ├── logistic_confusion_matrix.png
│   ├── decision_tree_confusion_matrix.png
│   ├── model_comparison.png
│   ├── feature_importance.png
│   └── correlation_heatmap.png
│
├── student_model_comparison.py
├── evaluation_results.txt
├── model_comparison.csv
├── README.md
└── requirements.txt
```

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

# 📦 Required Libraries

Install all required libraries using:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

# ▶️ Run the Project

```bash
python student_model_comparison.py
```

---

# 📊 Dataset Information

### Dataset Shape

- Rows: **301**
- Columns: **6**

### Features Used

- Attendance
- Assignment_Score
- Midterm_Score
- Final_Score

### Target Variable

| Result | Target |
|--------|--------|
| Pass | 1 |
| Fail | 0 |

---

# 🧹 Data Cleaning

The following preprocessing steps were performed:

- Removed **1 duplicate row**
- Filled missing values using the **column mean**
- Selected four important academic features
- Created a binary target column

---

# ✂ Train/Test Split

- Training Samples: **240**
- Testing Samples: **60**

Train/Test Ratio:

- 80% Training
- 20% Testing

---

# 🤖 Machine Learning Models

## Model 1

**Logistic Regression**

## Model 2

**Decision Tree Classifier**

---

# 📈 Evaluation Metrics

The following metrics were used to compare both models:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

# 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|--------|---------:|----------:|--------:|---------:|
| Logistic Regression | **95.00%** | **96.49%** | **98.21%** | **97.35%** |
| Decision Tree | **95.00%** | **94.92%** | **100.00%** | **97.39%** |

---

# 📄 Classification Results

## Logistic Regression

- Accuracy: **95.00%**
- Precision: **96.49%**
- Recall: **98.21%**
- F1 Score: **97.35%**

Confusion Matrix

```text
[[ 2  2 ]
 [ 1 55 ]]
```

---

## Decision Tree

- Accuracy: **95.00%**
- Precision: **94.92%**
- Recall: **100.00%**
- F1 Score: **97.39%**

Confusion Matrix

```text
[[ 1  3 ]
 [ 0 56 ]]
```

---

# 📊 Dataset Balance

| Class | Count |
|-------|------:|
| Pass | 282 |
| Fail | 18 |

The dataset is **imbalanced**, with significantly more Pass samples than Fail samples.

---

# 📈 Generated Files

After running the program, the following files are generated automatically.

## Reports

- evaluation_results.txt
- model_comparison.csv

## Visualizations

- Logistic Regression Confusion Matrix
- Decision Tree Confusion Matrix
- Model Comparison Chart
- Feature Importance
- Correlation Heatmap

---

# 🧠 Analysis

### Which model performed better?

Both models achieved **95% Accuracy**.

However, **Logistic Regression** produced higher **Precision**, while the **Decision Tree** achieved **100% Recall** for the Pass class.

Overall, Logistic Regression provides more balanced performance across the evaluation metrics.

### Dataset Balance

The dataset contains:

- Pass Students: **282**
- Fail Students: **18**

Because the dataset is imbalanced, performance on the minority (Fail) class can be improved.

---

# 🚀 Suggestions for Improvement

- Collect more student records.
- Balance the dataset using resampling techniques.
- Tune Decision Tree hyperparameters.
- Perform feature engineering.
- Use Cross Validation.
- Try ensemble models such as Random Forest or Gradient Boosting.

---

# 📚 Learning Outcomes

Through this project, I learned how to:

- Load datasets using Pandas.
- Clean missing and duplicate data.
- Prepare data for Machine Learning.
- Train multiple classification models.
- Compare model performance.
- Evaluate models using Accuracy, Precision, Recall, and F1 Score.
- Generate Confusion Matrices.
- Save reports and visualizations.
- Interpret model evaluation metrics.

---

# 👨‍💻 Author

**Qasim Shahzad**

**AI/ML Internship – HisabDo**

**Day 5 – Student Performance Prediction & Model Comparison**

---

# ⭐ Acknowledgement

This project was completed as part of the **HisabDo AI/ML Internship Program** to practice machine learning model training, evaluation, and comparison using Python and Scikit-learn.