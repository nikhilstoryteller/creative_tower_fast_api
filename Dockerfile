# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose port 8000 for the FastAPI app
EXPOSE 8000

# Step 6: Define environment variable
ENV PYTHONUNBUFFERED=1

# Step 7: Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "try:app", "--host", "0.0.0.0", "--port", "8000"]
