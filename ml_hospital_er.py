import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, mean_absolute_error, mean_squared_error
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import numpy as np

# Load dataset
df = pd.read_csv("hospital_er_data.csv")

# ---------------------------
# FEATURE SELECTION
# ---------------------------
features = [
    "age",
    "emergency_level",
    "severity_score",
    "vitals_score",
    "doctors_available",
    "nurses_available",
    "current_queue_length",
    "occupancy_rate",
    "triage_duration",
    "registration_delay",
    "doctor_assignment_delay",
    "hour_of_day"
]

X = df[features]
y_class = df["wait_flag"]              # CLASSIFICATION TARGET
y_reg = df["actual_waiting_time"]      # REGRESSION TARGET

# ---------------------------
# TRAIN/TEST SPLIT
# ---------------------------
X_train, X_test, y_train_class, y_test_class = train_test_split(
    X, y_class, test_size=0.2, random_state=42
)
_, _, y_train_reg, y_test_reg = train_test_split(
    X, y_reg, test_size=0.2, random_state=42
)

# ---------------------------
# MODEL 1: CLASSIFICATION (RF)
# ---------------------------
clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X_train, y_train_class)

y_pred_class = clf.predict(X_test)
y_pred_prob = clf.predict_proba(X)[:,1]

print("\n📌 Classification Accuracy:", accuracy_score(y_test_class, y_pred_class))
print("\n📌 Classification Report:\n", classification_report(y_test_class, y_pred_class))

# ---------------------------
# MODEL 2: REGRESSION (RF)
# ---------------------------
reg = RandomForestRegressor(n_estimators=200, random_state=42)
reg.fit(X_train, y_train_reg)

y_pred_reg = reg.predict(X_test)

print("\n📌 Regression MAE:", mean_absolute_error(y_test_reg, y_pred_reg))
print("📌 Regression RMSE:", np.sqrt(mean_squared_error(y_test_reg, y_pred_reg)))

# Predict on full dataset
df["predicted_waiting_time"] = reg.predict(X)
df["delay_probability"] = y_pred_prob

# Save final dataset
df.to_csv("hospital_er_data_with_predictions.csv", index=False)

print("\n🎉 ML predictions saved: hospital_er_data_with_predictions.csv")
print(df.head())

print("\nClassification Feature Importances:")
for f, imp in zip(features, clf.feature_importances_):
    print(f"{f}: {imp:.4f}")

print("\nRegression Feature Importances:")
for f, imp in zip(features, reg.feature_importances_):
    print(f"{f}: {imp:.4f}")
