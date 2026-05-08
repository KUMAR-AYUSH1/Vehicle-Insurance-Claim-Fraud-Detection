from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
import joblib
import pandas as pd
import uvicorn


app = FastAPI()
model = joblib.load('svc_model.pkl')
ct = joblib.load('ct.pkl')

class Data(BaseModel):
    Suspicious_Report: Literal[0,1]
    Sex: Literal["Male", "Female"]
    MaritalStatus: Literal["Single", "Married", "Divorced", "Widow"]
    RepNumber: int = Field(..., ge=1, le=16, description="ID of agent who handled the claim 1-16")
    Age: int = Field(..., ge=0, le=100)
    High_Risk_Individual: Literal[0,1]
@app.get('/')
async def root():
    return {'vehicle-claim-fraud-detection'}


@app.post('/predict')
async def predict(x: Data):
    
    input={
        'Suspicious_Report': x.Suspicious_Report,
        'Sex': x.Sex,
        'MaritalStatus': x.MaritalStatus,
        'RepNumber': x.RepNumber,
        'Age': x.Age,
        'High_Risk_Individual': x.High_Risk_Individual
    }
    df = pd.DataFrame([input], columns=['Suspicious_Report', 'Sex', 'MaritalStatus', 'RepNumber', 'Age', 'High_Risk_Individual'])

    df = ct.transform(df)
    prediction = model.predict(df)

    probabilities = model.predict_proba(df)
    confidence = float(probabilities.max())

    result = 'Fraud' if prediction[0] == 1 else 'No Fraud'
    return {'result': result, 'confidence': confidence}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)