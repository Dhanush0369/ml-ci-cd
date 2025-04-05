FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Accept the model version at build time
ARG MODEL_VERSION
ENV MODEL_VERSION=${MODEL_VERSION}

# Only copy the specific model version into the image
COPY models/${MODEL_VERSION} /app/models/${MODEL_VERSION}

COPY . .

EXPOSE 8000
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
