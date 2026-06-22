# 🎓 Placement Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Project Overview

This project predicts whether a student will be **placed or not placed** based on academic and aptitude-related attributes using Machine Learning.

The system trains a classification model using historical student data and provides placement predictions for new students based on their:

* 🏙️ City
* 📊 CGPA
* 🧠 IQ Score

The project also includes exploratory data analysis (EDA) and visualizations to understand factors influencing student placements.

---

## 🎯 Problem Statement

Campus placements play a crucial role in a student's career journey.

Educational institutions often seek to understand the factors affecting placement outcomes. This project leverages Machine Learning to analyze student data and predict placement status, helping institutions and students make informed decisions.

---

## 📂 Dataset Information

### Placement Dataset

| Feature   | Description                 |
| --------- | --------------------------- |
| City      | Student's city              |
| CGPA      | Academic performance        |
| IQ        | Intelligence Quotient score |
| Placement | Target variable             |

### Target Variable

| Value | Meaning    |
| ----- | ---------- |
| 1     | Placed     |
| 0     | Not Placed |

---

### Study Hours Dataset

A secondary dataset used for practicing and understanding Linear Regression concepts.

| Feature | Description   |
| ------- | ------------- |
| Hours   | Study hours   |
| Scores  | Student score |

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Joblib
* VS Code
* Git & GitHub

---

## 🤖 Machine Learning Model

### Logistic Regression

The project uses **Logistic Regression** for binary classification.

### Why Logistic Regression?

✅ Suitable for binary classification problems

✅ Fast training and prediction

✅ Easy interpretation

✅ Strong baseline model for placement prediction

---

## 🔄 Project Workflow

### 1️⃣ Data Loading

* Load placement dataset using Pandas
* Inspect structure and columns

### 2️⃣ Data Preprocessing

* Handle missing values
* Encode categorical features
* Separate features and target variable

### 3️⃣ Model Training

Features used:

* City
* CGPA
* IQ

Target:

* Placement Status

### 4️⃣ Model Evaluation

Metrics used:

* Accuracy Score
* Classification Report

### 5️⃣ Model Saving

Trained model is stored as:

```text
placement_model.pkl
```

### 6️⃣ Placement Prediction

User enters:

* City
* CGPA
* IQ

Model predicts:

* ✅ Placed
* ❌ Not Placed

---

## 📊 Data Visualizations

The project includes the following visualizations:

### 🥧 Placement Distribution Pie Chart

Displays the percentage of:

* Placed Students
* Not Placed Students

### 📊 CGPA-wise Placement Bar Chart

Shows placement distribution across different CGPA ranges.

### 📊 City-wise Placement Bar Chart

Displays the number of placed students from each city.

### 🔥 Correlation Heatmap

Shows relationships among:

* CGPA
* IQ
* Placement Status

---

## 📁 Project Structure

```text
placementprediction/
│
├── archive (3)
│   └── Study Hour(Linear Regression).csv
│
├── archive (4)
│   └── placement-dataset.csv
│
├── train.py
├── predict.py
├── explore.py
├── placement_model.pkl
├── requirements.txt
└── README.md
```

---

## 📜 File Description

### train.py

* Trains Logistic Regression model
* Evaluates model performance
* Saves trained model

### predict.py

* Loads saved model
* Accepts user input
* Predicts placement status

### explore.py

* Performs exploratory data analysis
* Generates visualizations

### placement_model.pkl

* Serialized trained machine learning model

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Tsubiksha/placementprediction.git
```

Move into project folder:

```bash
cd placementprediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Train Model

```bash
python train.py
```

### Predict Placement

```bash
python predict.py
```

### Generate Visualizations

```bash
python explore.py
```

---

## 🧪 Sample Prediction

### Input

```text
City : New York
CGPA : 8.5
IQ   : 130
```

### Output

```text
Prediction: Student will be Placed
```

---

## 📈 Model Performance

Current Model:

* Logistic Regression

Evaluation Metric:

* Accuracy Score

Example Accuracy:

```text
Accuracy = 0.85
```

*(Accuracy may vary depending on train-test split.)*

---

## 🚀 Future Enhancements

* Random Forest Classifier
* Decision Tree Classifier
* K-Nearest Neighbors (KNN)
* Model Comparison Dashboard
* Streamlit Web Application
* Placement Probability Prediction
* Feature Importance Analysis
* Hyperparameter Tuning
* Deployment using Flask/Streamlit

---

## 👩‍💻 Author

**Subiksha Thangavel**

B.Tech – Artificial Intelligence and Data Science

📌 Passionate about Machine Learning, Data Analytics, and AI Solutions.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
