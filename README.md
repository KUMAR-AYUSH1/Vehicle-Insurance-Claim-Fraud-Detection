# 🚗 Vehicle Insurance Claim Fraud Detection

A complete end-to-end Machine Learning project for detecting fraudulent vehicle insurance claims using classification models, hyperparameter tuning with Optuna, deployment with FastAPI & Streamlit, and containerization using Docker.

---

## 📌 Project Overview

Insurance fraud leads to significant financial losses every year.
This project aims to automatically identify suspicious vehicle insurance claims using Machine Learning models trained on structured claim data.

The project includes:

* ✅ Data preprocessing & feature engineering
* ✅ Handling imbalanced datasets
* ✅ Model training & evaluation
* ✅ Hyperparameter tuning using Optuna
* ✅ FastAPI backend API
* ✅ Streamlit frontend UI
* ✅ Dockerized deployment

---

## 📂 Dataset

Dataset from Kaggle:

[Vehicle Claim Fraud Detection Dataset](https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection?utm_source=chatgpt.com)

---

# ⚙️ Workflow

## 1️⃣ Feature Engineering & Selection

Notebook: `test1`

* Data cleaning
* Feature creation
* Feature selection
* Exploratory preprocessing

---

## 2️⃣ Handling Imbalanced Data

Notebook: `test2`

Since fraud datasets are highly imbalanced:

* Applied imbalance handling techniques
* Generated balanced dataset
* Saved processed dataset as:

```bash
balanced.csv
```

---

## 3️⃣ Model Training

Notebook: `test3`

Models tested:

* Logistic Regression
* Support Vector Classifier (SVC)
* KNN
* Random Forest
* XGBoost Classifier
* Gaussian Naive Bayes

### Top Performing Models

* GaussianNB
* XGBoost
* Random Forest
* SVC

---

## 4️⃣ Hyperparameter Tuning with Optuna

Notebook: `test4`

Applied Optuna optimization on:

* GaussianNB
* XGBoost
* Random Forest
* SVC

### Best Models After Tuning

* XGBoost
* SVC

---

## 5️⃣ Final Model Selection

Notebook: `test5`

Final comparison between:

* XGBoost
* SVC

### ✅ Selected Final Model: SVC

### Final Performance

* Accuracy: **77%**
* Recall Score: **91%**

Saved artifacts:

```bash
svc_model.pkl
ct.pkl
```

---

# 🚀 Deployment

## 🔹 FastAPI Backend

FastAPI is used to serve the trained model through REST API endpoints.

### API Features

* Input validation using Pydantic
* Prediction endpoint
* Fraud probability confidence score

---

## 🔹 Streamlit Frontend

Interactive Streamlit application for real-time predictions.

### Features

* User-friendly UI
* Real-time fraud prediction
* Confidence score display
* API integration with FastAPI

---

# 🐳 Docker Support

The project is fully containerized using Docker.

## Pull Docker Image

```bash
docker pull kumar2700/vehicle-fraud-detection:latest
```

## Run Container

```bash
docker run -p 8000:8000 -p 8501:8501 kumar2700/vehicle-fraud-detection:latest
```


## Streamlit UI

```bash
http://localhost:8501
```

## FastAPI Docs

```bash
http://localhost:8000/docs
```

---

# 🛠️ Tech Stack

## Machine Learning

* Scikit-learn
* XGBoost
* Optuna
* Pandas
* NumPy

## Backend

* FastAPI
* Uvicorn

## Frontend

* Streamlit

## Deployment

* Docker

---

