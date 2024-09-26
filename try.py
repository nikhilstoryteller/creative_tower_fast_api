import pickle
import numpy as np
import tensorflow as tf
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import List
from fastapi.responses import JSONResponse

# Create FastAPI instance
app = FastAPI()
import pandas as pd
# Step 1: Load the creative tower model from the pickle file
with open('creative_tower.pkl', 'rb') as f:
    creative_tower = pd.read_pickle(f)

# Step 2: Define the input data structure for API requests
class CreativeInput(BaseModel):
    creative_embedding: List[float]  # This is the input embedding that will be passed
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# Step 3: API endpoint to generate the creative embedding
@app.post("/get-creative-embedding/")
async def get_creative_embedding(input_data: CreativeInput, response_class=JSONResponse):
    # Convert input to numpy array and reshape for model input
    creative_embedding = np.array([input_data.creative_embedding], dtype=np.float32)
    
    # Generate the embedding using the creative tower
    creative_output = creative_tower.predict(creative_embedding)  # Call predict directly
    
    # Convert the output to a list before returning it as JSON
    creative_output_list = creative_output.tolist()
    
    # Return the output embedding as a JSON response
    return {"creative_embedding": creative_output_list}

# Step 4: Run the FastAPI app using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
