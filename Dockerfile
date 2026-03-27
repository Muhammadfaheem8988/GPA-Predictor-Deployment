FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10000

# Train only if the model doesn't exist, then start the API
CMD ["sh", "-c", "test -f models/gpa_model.pkl || python src/train_model.py; uvicorn src.app:app --host 0.0.0.0 --port ${PORT:-10000}"]
