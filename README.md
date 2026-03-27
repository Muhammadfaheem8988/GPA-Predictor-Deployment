# GPA Predictor (FastAPI + Docker)

An end-to-end machine learning web application built with **Python**, **FastAPI**, and **Docker** to predict student GPAs.

## Features

- FastAPI backend for GPA predictions
- Simple HTML frontend served at `/`
- Model training script included (`src/train_model.py`)
- Dockerized deployment (uses port **10000** by default)

## Project Structure

```text
.
├── data/
├── models/                 # Expected location for model file (gpa_model.pkl)
├── notebooks/
├── src/
│   ├── app.py              # FastAPI app (uvicorn src.app:app)
│   └── train_model.py      # Trains model
├── templates/
│   └── index.html
├── Dockerfile
├── requirements.txt
└── README.md
```

## Running Locally (without Docker)

### 1) Install dependencies

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
```

### 2) Train the model

```bash
python src/train_model.py
```

> Note: `src/app.py` expects the model at `models/gpa_model.pkl`.
> If `train_model.py` outputs `gpa_model.pkl` in the repo root, move it into `models/`:
>
> ```bash
> mkdir -p models
> mv gpa_model.pkl models/gpa_model.pkl
> ```

### 3) Start the API

```bash
uvicorn src.app:app --reload --port 10000
```

Open:
- App UI: `http://127.0.0.1:10000/`

## Run with Docker

### Build

```bash
docker build -t gpa-predictor .
```

### Run

```bash
docker run -p 10000:10000 gpa-predictor
```

Then open:
- App UI: `http://127.0.0.1:10000/`

## API Endpoints

- `GET /` → serves the HTML UI
- `POST /predict_gpa` → returns a predicted GPA

Example request:

```bash
curl -X POST "http://127.0.0.1:10000/predict_gpa" \
  -H "Content-Type: application/json" \
  -d '{"study_hours":10,"IQ":110,"attendance":85,"sleep_hours":7}'
```

## Screenshots

![Screenshot 1](Screenshots/1.png)
![Screenshot 2](Screenshots/2.png)

## License

This project includes a license file: see `LICENSE`.