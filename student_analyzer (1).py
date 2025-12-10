import pandas as pd
import numpy as np

# 1) LOAD DATA
df = pd.read_csv("students.csv")

# 2) TOTAL & AVERAGE MARKS PER STUDENT
df["total"] = df[["maths", "physics", "chemistry"]].sum(axis=1)
df["average"] = df["total"] / 3

# 3) CLASS AVERAGE PER SUBJECT
class_avg = df[["maths", "physics", "chemistry"]].mean()

# 4) TOPPER PER SUBJECT
topper_maths = df.loc[df["maths"].idxmax()]
topper_physics = df.loc[df["physics"].idxmax()]
topper_chemistry = df.loc[df["chemistry"].idxmax()]

# 5) OVERALL TOPPER
overall_topper = df.loc[df["total"].idxmax()]

# 6) PASS / FAIL STATUS (PASS = average >= 40)
df["status"] = np.where(df["average"] >= 40, "Pass", "Fail")

# 7) GRADE ALLOCATION
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"

df["grade"] = df["average"].apply(grade)

# 8) RANKING
df["rank"] = df["total"].rank(ascending=False, method="dense").astype(int)

# 9) PRINT REPORT
print("===== CLASS SUMMARY =====")
print("Class Average (Maths):", round(class_avg["maths"], 2))
print("Class Average (Physics):", round(class_avg["physics"], 2))
print("Class Average (Chemistry):", round(class_avg["chemistry"], 2))
print()

print("===== SUBJECT TOPPERS =====")
print("Maths Topper:", topper_maths["name"], topper_maths["maths"])
print("Physics Topper:", topper_physics["name"], topper_physics["physics"])
print("Chemistry Topper:", topper_chemistry["name"], topper_chemistry["chemistry"])
print()

print("===== OVERALL TOPPER =====")
print(overall_topper["name"], "with total =", overall_topper["total"])
print()

print("===== FAILING STUDENTS =====")
print(df[df["status"] == "Fail"][["roll_no", "name", "average"]])
print()

# 10) EXPORT FINAL REPORT
df.sort_values("rank").to_csv("final_student_report.csv", index=False)

print("Final report exported: final_student_report.csv")
