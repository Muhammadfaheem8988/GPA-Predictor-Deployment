from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
from pathlib import Path


# Paths
BASE_DIR = Path(__file__).resolve().parent.parent  # repo root
DATA_PATH = BASE_DIR / "data" / "mock_gpa.csv"
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "gpa_model.pkl"


# Load existing dataset
# Expected columns: study_hours, IQ, attendance, sleep_hours, GPA
if not DATA_PATH.exists():
    raise FileNotFoundError(f"Dataset not found at: {DATA_PATH}")

data = pd.read_csv(DATA_PATH)

required_cols = {"study_hours", "IQ", "attendance", "sleep_hours", "GPA"}
missing = required_cols - set(data.columns)
if missing:
    raise ValueError(
        f"Dataset is missing required columns: {sorted(missing)}. "
        f"Found columns: {list(data.columns)}"
    )

# Step 2: Train model
X = data[["study_hours", "IQ", "attendance", "sleep_hours"]]
y = data["GPA"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Step 3: Save model (where the API expects it)
MODEL_DIR.mkdir(parents=True, exist_ok=True)
joblib.dump(model, MODEL_PATH)

print(f"Model trained and saved as {MODEL_PATH}")
