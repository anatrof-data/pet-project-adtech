# 1. Use official lightweight Python image
FROM python:3.10-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Install system-level dependencies required by ML libraries
RUN apt-get update && apt-get install -y \
    build-essential \        # compilers for numpy, pandas, etc.
    git \                    # version control (optional, for MLflow or future usage)
    curl \                   # useful for network tools (optional)
    libglib2.0-0 \           # for matplotlib and rendering
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*  # clean up to reduce image size

# 4. Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy only required files/folders
COPY main.py ./                   # main entrypoint
COPY src/ ./src/                  # your source modules
COPY data/ ./data/                # input dataset folder (if needed)
COPY models/ ./models/            # to save output model

# 6. Make sure expected directories exist
RUN mkdir -p /app/data /app/models

# 7. Run the training script when container starts
CMD ["python", "main.py"]
