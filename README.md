# 🏥 Hospital Operational Insights & ER Delay Forecasting  
### Power BI + Machine Learning Project

This project delivers an end-to-end analytical and predictive system for **Emergency Room (ER) operations**, combining **Power BI dashboards** with **Machine Learning models** to analyze patient traffic, predict waiting times, and identify operational bottlenecks.

Designed specifically for recruiters and hiring managers, this project demonstrates expertise in:

✔ Data Engineering  
✔ Data Visualization (Power BI)  
✔ Machine Learning (Classification + Regression)  
✔ Operational Analytics  
✔ End-to-end project ownership  

---

# 📌 Project Overview

Emergency Rooms (ER) frequently deal with unpredictable patient flow, staffing constraints, and fluctuating wait times.  
This project simulates a real-world ER scenario by:

- Generating a **synthetic hospital dataset** (1,000+ patient records)
- Creating **predictive models** to estimate:
  - ER Waiting Time (Regression)
  - Probability of Delay (Classification)
- Building a **professional Power BI dashboard** showing:
  - Operational insights  
  - Queue patterns  
  - Peak hours  
  - Delay-risk patient segments  
  - Feature importance (ML interpretability)

This mirrors the type of analytics used by modern hospitals for optimization.

---

# 🧠 Machine Learning Models Used

This project uses two ML models:

### **1️⃣ Random Forest Classifier**
- Predicts whether a patient is likely to face **significant delay**
- Output: `delay_probability`
- Accuracy: **94.4%**
- Key Features Influencing Delays:
  - `current_queue_length`
  - `occupancy_rate`
  - `doctors_available`
  - `age`

### **2️⃣ Random Forest Regressor**
- Predicts **exact waiting time (in minutes)**
- MAE: **7.81**
- RMSE: **10.51**

These predictions are imported into Power BI for visualization.

---

# 🗂 Dataset Description

The dataset contains over **20 operational variables**, including:

| Column | Description |
|--------|-------------|
| age | Patient age |
| emergency_level | Triage category (1–5) |
| severity_score | Computed condition severity |
| vitals_score | Vital signs stability metric |
| doctors_available | Number of active doctors |
| nurses_available | Number of active nurses |
| current_queue_length | Patients waiting |
| occupancy_rate | Overall ER capacity usage |
| arrival_mode | Walk-in or Ambulance |
| actual_waiting_time | True time (in minutes) |
| predicted_waiting_time | ML output |
| delay_probability | Classification model output |

---

# 📊 Power BI Dashboards

## **📍 Page 1 — Operational Analytics Overview**
Includes:
- Avg waiting time  
- Queue length & occupancy rate  
- Trend analysis  
- Walk-in vs ambulance comparison  
- Queue length vs waiting time  
- Peak day/hour patterns  



---

## **📍 Page 2 — ML Predictions & Risk Insights**
Includes:
- High/Medium/Low delay-risk segmentation  
- Actual vs predicted wait time scatter plot  
- Delay probability distribution  
- Delay by symptoms  
- Feature importance from ML model  

---

# 🔧 Tech Stack

| Layer | Tools Used |
|-------|------------|
| **Data Generation** | Python, NumPy, Pandas |
| **Machine Learning** | Scikit-learn (Random Forest) |
| **Visualization** | Microsoft Power BI |
| **Model Export** | CSV integration |
| **Version Control** | Git + GitHub |

---

# 🏗 Project Architecture

┌──────────────────────────┐
│ 1. Synthetic Data Engine │
└───────────┬──────────────┘
▼
┌──────────────────────────┐
│ 2. ML Model Training │
│ - Classification │
│ - Regression │
└───────────┬──────────────┘
▼
┌──────────────────────────┐
│ 3. Export Predictions │
│ hospital_er_data_with_predictions.csv
└───────────┬──────────────┘
▼
┌──────────────────────────┐
│ 4. Power BI Dashboard │
│ - Operational Insights│
│ - Delay Forecasting │
│ - Feature Importance │
└──────────────────────────┘


---

# 📈 Key Insights

### ✔ Queue length is the strongest predictor of ER delays  
Patients arriving during high queue periods wait significantly longer.

### ✔ Occupancy rate directly impacts predicted wait time  
High occupancy → longer processing times → extended waits.

### ✔ Walk-in patients typically experience higher delays  
Ambulance patients get priority.

### ✔ ML alignment with real data  
Strong correlation between **predicted** vs **actual** wait times shows good model performance.

---

# 🚀 How to Run the Project

## **1️⃣ Clone the repository**
```bash
git clone https://github.com/your_username/hospital-er-delay-forecasting.git
cd hospital-er-delay-forecasting

2.Run the ML script now:

"python ml_hospital_er.py"


This will generate:

"hospital_er_data_with_predictions.csv"
"classification_feature_importances.csv"
"regression_feature_importances.csv"

3.Open Power BI file

Open hospital_ER_dashboard.pbix

Refresh data to load predictions


Future Improvements

Deploy ML model as a real-time API

Connect Power BI to a live database

Add patient-level forecasting

Add shift-optimization recommendations

Replace synthetic data with real hospital dataset (if available)



👤 Author

Rohit Varma