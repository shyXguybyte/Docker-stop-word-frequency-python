# base image 
FROM python:3

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir nltk

# Download NLTK stopwords
RUN python -m nltk.downloader stopwords

# Run the Python script
CMD ["python", "python.py"]
