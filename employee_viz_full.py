# employee_viz_full.py
# Verification email: 22f3001685@ds.study.iitm.ac.in
#
# This script:
# - Generates a synthetic employee dataset (100 rows)
# - Prints the frequency count for the "IT" department
# - Creates a department distribution histogram and saves it as "department_distribution.png"

import random
import pandas as pd
import matplotlib.pyplot as plt

# Reproducible random seed
random.seed(42)

# Departments and regions used to synthesize the dataset
departments = ["Sales", "Marketing", "Operations", "R&D", "IT", "HR", "Finance"]
regions = ["Europe", "Latin America", "North America", "Asia Pacific", "Africa"]

# Generate 100 synthetic employee rows
rows = []
for i in range(1, 101):
    emp_id = f"EMP{i:03d}"
    # Use weighted choices so distribution isn't uniform
    dept = random.choices(departments, weights=[20, 15, 15, 10, 12, 8, 20], k=1)[0]
    region = random.choice(regions)
    # performance_score: slightly higher on average for R&D (example bias)
    perf = round(random.uniform(60, 95) + (5 if dept == "R&D" else 0), 2)
    years = random.randint(1, 20)
    satisfaction = round(random.uniform(2.5, 5.0), 1)
    rows.append([emp_id, dept, region, perf, years, satisfaction])

# Create DataFrame
df = pd.DataFrame(
    rows,
    columns=[
        "employee_id",
        "department",
        "region",
        "performance_score",
        "years_experience",
        "satisfaction_rating",
    ],
)

# Calculate frequency count for the "IT" department and print it
it_count = (df["department"] == "IT").sum()
print(f'Frequency count for the "IT" department: {it_count}')

# Save a CSV copy if you want
df.to_csv("employee_data_sample.csv", index=False)
print("Saved synthetic dataset to employee_data_sample.csv")

# Create and save a histogram (bar chart) for the department distribution
fig, ax = plt.subplots(figsize=(10, 6))
dept_counts = df["department"].value_counts().sort_index()
bars = ax.bar(dept_counts.index, dept_counts.values)
ax.set_title("Department Distribution (n=100)", fontsize=14)
ax.set_xlabel("Department", fontsize=12)
ax.set_ylabel("Count", fontsize=12)
ax.grid(axis="y", linestyle="--", linewidth=0.5, alpha=0.7)

# Optionally annotate bars with counts
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f"{int(height)}",
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 6),
        textcoords="offset points",
        ha="center",
        va="bottom",
        fontsize=10,
    )

plt.tight_layout()
plt.savefig("department_distribution.png", bbox_inches="tight")
print('Saved plot to "department_distribution.png"')

# If you also want to open the plot automatically (uncomment the following):
# plt.show()
