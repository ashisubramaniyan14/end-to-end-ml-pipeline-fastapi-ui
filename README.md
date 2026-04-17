# End-to-End ML Data Pipeline with FastAPI and Bash Automation

This project demonstrates a modular machine learning pipeline built using Python. It covers the full lifecycle of data processing, including ingestion, ETL, feature engineering, model training, and real-time inference with FastAPI.

## Project Architecture

Data Ingestion → ETL → Feature Engineering → Model Training → API Serving

## Tech Stack

- Python
- Pandas
- NumPy
- scikit-learn
- FastAPI
- Bash
- yfinance
- joblib

## Features

- Automated stock data ingestion
- Data cleaning and preprocessing
- Feature engineering for time-series prediction
- Logistic Regression model training
- Real-time prediction API using FastAPI
- Bash-based pipeline execution

## Project Structure

```text
data/
  raw/
  processed/
models/
src/
  ingestion/
  etl/
  features/
  training/
  api/
  utils/