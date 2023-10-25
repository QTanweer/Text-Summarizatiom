from fastapi import FastAPI
import uvicorn
import sys
import os

from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.textSummarization.pipeline.prediction import PredictionPipeline

text:str = "What is Text Summarizaton"
app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful")
    
    except Exception as e:
        return Response(f"Training failed..!!! {e}")
    
@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        result = obj.predict(text)
        return Response(result)
    
    except Exception as e:
        return Response(f"Prediction failed..!!! {e}")
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)