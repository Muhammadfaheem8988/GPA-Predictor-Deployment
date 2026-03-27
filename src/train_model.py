import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib


np.random.seed(42)
data = pd.DataFrame({
    'study_hours': np.random.randint(5, 40, 100),
    'IQ': np.random.randint(80, 160, 100),
    'attendance': np.random.randint(50, 100, 100),
    'sleep_hours': np.random.randint(4, 10, 100)
})

# Creating GPA with noise
data['GPA'] = (
    0.02 * data['study_hours'] +
    0.01 * data['IQ'] +
    0.03 * data['attendance'] -
    0.01 * data['sleep_hours'] +
    np.random.normal(0, 0.5, 100)
)

# Clip GPA to 0-4 range (ensures model learns correct bounds)
data['GPA'] = data['GPA'].clip(0, 4)

# =========================
# Step 2: Train model
# =========================
X = data[['study_hours', 'IQ', 'attendance', 'sleep_hours']]
y = data['GPA']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# =========================
# Step 3: Save model
# =========================
joblib.dump(model, 'gpa_model.pkl')
print("Model trained and saved as gpa_model.pkl")
