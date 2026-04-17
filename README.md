# 🚀 End-to-End ML Pipeline with FastAPI and UI Dashboard

This project demonstrates a production-style machine learning pipeline that covers the full lifecycle from data ingestion to real-time prediction, integrated with an interactive frontend dashboard.

---

## 📊 Overview

This system automates the complete ML workflow:

- Data Ingestion from external API (Yahoo Finance)
- ETL pipeline for cleaning and transformation
- Feature Engineering for time-series modeling
- Model Training and Evaluation
- Real-time Prediction API using FastAPI
- Interactive UI Dashboard for predictions

---

## 🧠 Key Features

- Modular pipeline architecture
- Automated data processing workflow
- Time-series feature engineering
- Logistic Regression model training
- Real-time inference via REST API
- Frontend dashboard for user interaction
- Bash automation for pipeline execution
- Cloud-ready system design

---

## 🏗️ Architecture
Data Source → Ingestion → ETL → Feature Engineering → Model Training → FastAPI → UI Dashboard


---

## ⚙️ Tech Stack

- **Python** (Pandas, NumPy, scikit-learn)
- **FastAPI** (Backend API)
- **HTML, CSS, JavaScript** (Frontend UI)
- **Bash** (Pipeline automation)
- **yfinance API** (Data source)
- **Docker** (Deployment-ready)

---

## 📁 Project Structure
├── data/
│ ├── raw/
│ └── processed/
├── models/
├── src/
│ ├── ingestion/
│ ├── etl/
│ ├── features/
│ ├── training/
│ ├── api/
│ └── utils/
├── static/
├── templates/
├── README.md


---

## 🚀 How to Run

### 1. Install dependencies
pip install -r requirements.txt


### 2. Run pipeline
python -m src.ingestion.fetch_data
python -m src.etl.build_dataset
python -m src.training.train_model


### 3. Start API
uvicorn src.api.main:app --reload


### 4. Open UI
http://127.0.0.1:8000


---

## 📊 Sample Output
<img width="1555" height="732" alt="image" src="https://github.com/user-attachments/assets/de2c814f-2404-43c5-8db9-4a5312e3f2a3" />


---

## 🎯 Use Case

This project simulates how real-world ML systems are built in production, combining data engineering, machine learning, and backend development into a unified workflow.

---

## ☁️ Cloud Readiness

The system is designed to be easily deployable:

- Can be containerized using Docker
- Storage can be mapped to AWS S3 / GCP / Azure
- API can be deployed on cloud platforms
- Pipeline can be orchestrated with Airflow

---

## 💡 Learning Outcomes

- Designing modular ML pipelines
- Handling real-world data preprocessing
- Integrating ML models with APIs
- Building full-stack ML applications
- Structuring scalable, production-ready systems

---

## 👤 Author

**Asha Subramaniyan**

---

