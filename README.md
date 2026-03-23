# Home Loan Model Monitoring System

## Overview
Production-ready monitoring system for home loan ML models.

## Features
- PSI (Population Stability Index)
- Data Drift Detection
- REST API using FastAPI

## Run Locally
pip install -r requirements.txt
uvicorn app.main:app --reload

## API Endpoint
/psi → Returns PSI value
