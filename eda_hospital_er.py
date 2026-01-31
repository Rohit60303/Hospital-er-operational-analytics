import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("hospital_er_data.csv")

print("\n📌 Dataset Preview:")
print(df.head())

print("\n📌 Statistical Summary:")
print(df.describe())

# ----------------------------
# 1. Distribution of Waiting Time
# ----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df['actual_waiting_time'], kde=True, color="blue")
plt.title("Distribution of ER Waiting Time")
plt.xlabel("Waiting Time (minutes)")
plt.ylabel("Frequency")
plt.show()

# ----------------------------
# 2. Wait Time by Day of Week
# ----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x="day_of_week", y="actual_waiting_time", data=df)
plt.title("Waiting Time by Day of Week")
plt.xticks(rotation=45)
plt.show()

# ----------------------------
# 3. Wait Time by Hour of Day
# ----------------------------
plt.figure(figsize=(8,5))
sns.lineplot(x="hour_of_day", y="actual_waiting_time",
             data=df, estimator="mean")
plt.title("Average Waiting Time by Hour of Day")
plt.show()

# ----------------------------
# 4. Queue Length vs Waiting Time
# ----------------------------
plt.figure(figsize=(7,5))
sns.scatterplot(x="current_queue_length", y="actual_waiting_time", data=df)
plt.title("Queue Length vs Waiting Time")
plt.xlabel("Queue Length")
plt.ylabel("Waiting Time")
plt.show()

# ----------------------------
# 5. Emergency Level vs Waiting Time
# ----------------------------
plt.figure(figsize=(7,5))
sns.boxplot(x="emergency_level", y="actual_waiting_time", data=df)
plt.title("Emergency Level vs Waiting Time")
plt.xlabel("Emergency Level (1 = low, 5 = highest priority)")
plt.show()

# ----------------------------
# 6. Severity vs Waiting Time (scatter)
# ----------------------------
plt.figure(figsize=(7,5))
sns.scatterplot(x="severity_score", y="actual_waiting_time", data=df)
plt.title("Severity Score vs Waiting Time")
plt.show()

# ----------------------------
# 7. Mode of Arrival Impact
# ----------------------------
plt.figure(figsize=(7,5))
sns.boxplot(x="arrival_mode", y="actual_waiting_time", data=df)
plt.title("Walk-In vs Ambulance Waiting Time")
plt.show()

# ----------------------------
# 8. Occupancy Rate vs Waiting Time
# ----------------------------
plt.figure(figsize=(7,5))
sns.scatterplot(x="occupancy_rate", y="actual_waiting_time", data=df)
plt.title("Hospital Occupancy vs Waiting Time")
plt.show()

# ----------------------------
# 9. Correlation Heatmap
# ----------------------------
plt.figure(figsize=(9,6))
sns.heatmap(df.corr(), cmap="coolwarm", annot=True)
plt.title("Correlation Heatmap")
plt.show()
