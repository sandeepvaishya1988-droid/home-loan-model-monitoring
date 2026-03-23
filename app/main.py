from fastapi import FastAPI
from monitoring import calculate_psi

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Home Loan Monitoring API Running"}

@app.get("/psi")
def psi():
    return {"psi": calculate_psi()}
