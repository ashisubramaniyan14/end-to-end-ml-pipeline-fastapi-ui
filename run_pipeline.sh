#!/bin/bash

echo "Fetching raw data..."
python -m src.ingestion.fetch_data

echo "Building processed dataset..."
python -m src.etl.build_dataset

echo "Training model..."
python -m src.training.train_model

echo "Pipeline completed successfully."