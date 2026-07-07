import pandas as pd

# Sample student dataset
data = {
    "Study_Hours": [2, 4, 6, 8, 10],
    "Attendance": [60, 70, 80, 90, 95],
    "Marks": [45, 55, 70, 85, 95]
}

df = pd.DataFrame(data)

print("Student Performance Dataset")
print(df)

average_marks = df["Marks"].mean()

print("\nAverage Marks:", average_marks)

if average_marks >= 60:
    print("Prediction: Good Student Performance")
else:
    print("Prediction: Needs Improvement")
