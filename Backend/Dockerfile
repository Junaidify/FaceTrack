# Use base image
FROM python:3.10-slim

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libboost-all-dev \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only the backend folder
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install \
    face_recognition \
    numpy \
    uvicorn \
    fastapi \
    pillow \
    python-multipart

# Run FastAPI server (note: subfolder path to encodeimg.py)
CMD ["uvicorn", "pythonscript.encodeimg:app", "--host", "0.0.0.0", "--port", "8000"]
