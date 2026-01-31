import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# -----------------------------
# CONFIG
# -----------------------------
NUM_RECORDS = 5000
np.random.seed(42)

# -----------------------------
# Helper functions
# -----------------------------

def random_datetime():
    """Generate random arrival timestamp within last 60 days."""
    start = datetime.now() - timedelta(days=60)
    random_minutes = random.randint(0, 60*24*60)
    return start + timedelta(minutes=random_minutes)

def severity_from_emergency(level):
    """Higher emergency level → higher severity score."""
    return np.clip(np.random.normal(level * 2, 2), 1, 10)

def vitals_from_severity(sev):
    """Vitals score increases if severity is high."""
    base = sev + np.random.normal(0, 1.5)
    return np.clip(base, 1, 10)

def calculate_wait_time(queue, doctors, severity, occupancy):
    """
    Realistic model:
    - More queue → higher wait
    - More doctors → lower wait
    - Higher severity → lower wait (prioritized)
    - Higher occupancy → higher wait
    """
    base_wait = queue * np.random.uniform(1.5, 3.5)
    doctor_effect = 40 / (doctors + 1)
    severity_effect = max(1, 15 - severity)   # severe cases wait less
    occupancy_effect = occupancy * 0.4

    wait = base_wait + doctor_effect + severity_effect + occupancy_effect
    wait = np.clip(wait, 2, 300)  # cap at 5 hours
    return round(wait, 1)

# -----------------------------
# GENERATE DATA
# -----------------------------
records = []

symptoms_list = [
    "Chest Pain", "Breathing Issue", "Fever", "Head Injury",
    "Abdominal Pain", "Fracture", "Vomiting", "Unconscious",
    "Burns", "Seizure", "Accident Trauma", "Bleeding"
]

for i in range(NUM_RECORDS):

    arrival = random_datetime()
    day_of_week = arrival.strftime("%A")
    hour_of_day = arrival.hour

    age = np.random.randint(1, 95)
    gender = random.choice(["Male", "Female"])

    arrival_mode = random.choice(["Walk-in", "Ambulance"])
    emergency_level = np.random.randint(1, 6)

    severity = severity_from_emergency(emergency_level)
    vitals = vitals_from_severity(severity)

    symptoms = random.choice(symptoms_list)

    doctors_available = np.random.randint(1, 10)
    nurses_available = np.random.randint(2, 20)
    current_queue = np.random.randint(0, 30)

    occupancy_rate = np.random.randint(30, 100)

    triage_duration = np.random.randint(2, 15)
    registration_delay = np.random.randint(1, 10)
    doctor_assignment_delay = np.random.randint(1, 15)

    # Predict final waiting time
    actual_wait = calculate_wait_time(
        current_queue,
        doctors_available,
        severity,
        occupancy_rate
    )

    wait_flag = 1 if actual_wait > 60 else 0  # more than 1 hour = delayed

    records.append([
        i + 1,
        arrival,
        day_of_week,
        hour_of_day,
        age,
        gender,
        arrival_mode,
        emergency_level,
        round(severity, 1),
        round(vitals, 1),
        symptoms,
        doctors_available,
        nurses_available,
        current_queue,
        occupancy_rate,
        triage_duration,
        registration_delay,
        doctor_assignment_delay,
        actual_wait,
        wait_flag
    ])

# -----------------------------
# SAVE CSV
# -----------------------------
columns = [
    "patient_id",
    "arrival_time",
    "day_of_week",
    "hour_of_day",
    "age",
    "gender",
    "arrival_mode",
    "emergency_level",
    "severity_score",
    "vitals_score",
    "symptoms_category",
    "doctors_available",
    "nurses_available",
    "current_queue_length",
    "occupancy_rate",
    "triage_duration",
    "registration_delay",
    "doctor_assignment_delay",
    "actual_waiting_time",
    "wait_flag"
]

df = pd.DataFrame(records, columns=columns)
df.to_csv("hospital_er_data.csv", index=False)

print("\n🎉 Dataset generated successfully: hospital_er_data.csv")
print(df.head())
