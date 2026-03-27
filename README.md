# GPA Predictor Deployment

An end-to-end machine learning web application built with **Python**, **FastAPI**, and **Docker** to predict students’ GPAs.

## Features

- GPA prediction using a trained machine learning model
- FastAPI backend for serving predictions
- Simple web UI
- Containerized deployment with Docker

## Tech Stack

- **Python**
- **FastAPI**
- **HTML/CSS**
- **Docker**

## Getting Started

### 1) Clone the repository

```bash
git clone https://github.com/Muhammadfaheem8988/GPA-Predictor-Deployment.git
cd GPA-Predictor-Deployment
```

### 2) Run locally (without Docker)

> Adjust commands/paths below to match the project structure if different.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Then open the API docs at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### 3) Run with Docker

```bash
docker build -t gpa-predictor .
docker run -p 8000:8000 gpa-predictor
```

## Usage

1. Start the app locally or via Docker.
2. Enter the required student information in the UI (or call the API).
3. Submit to get a predicted GPA.

## Project Structure

```text
.
├── app/            # FastAPI application code
├── templates/      # HTML templates
├── static/         # CSS/JS/assets
├── model/          # Trained model artifacts
├── requirements.txt
└── Dockerfile
```

> This structure is a typical layout; update it to reflect the actual folders in this repository.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request with your proposed changes.

## License

Add a license (MIT/Apache-2.0/etc.) if you plan to share or reuse this project publicly.
