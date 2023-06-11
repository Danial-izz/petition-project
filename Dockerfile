# Base image
FROM python:3.9.16

# Set working directory
WORKDIR /app

# Copy project files to the working directory
COPY . /app

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download nltk files 
RUN [ "python", "-c", "import nltk; nltk.download('all')" ]

# Set the entry point
CMD ["python", "main.py"]