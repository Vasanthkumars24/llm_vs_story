# employee_viz.py
# Employee department histogram generator
# Author: 22f3001685@ds.study.iitm.ac.in

import pandas as pd
import plotly.express as px
import numpy as np
import os

OUTPUT_HTML = "departments_hist.html"

def generate_employee_data():
    """Create synthetic employee dataset since the provided Excel has no department column."""
    np.random.seed(42)

    departments = [
        "Operations", "HR", "Finance", "IT", "Marketing",
        "Sales", "Support", "Logistics"
    ]

    # Generate 100 employees
    data = {
        "Employee_ID": range(1, 101),
        "Department": np.random.choice(departments, size=100, p=[
            0.20, 0.10, 0.10, 0.15, 0.10, 0.15, 0.10, 0.10
        ]),
        "Performance_Score": np.random.randint(50, 100, size=100)
    }

    return pd.DataFrame(data)

def main():
    df = generate_employee_data()
    print("[info] Generated synthetic employee dataset (100 rows)")
    print(df.head())

    # Frequency counts
    counts = df["Department"].value_counts()
    print("\n=== Department frequency counts ===")
    print(counts.to_string())

    # Count for Operations
    ops_count = counts.get("Operations", 0)
    print(f"\nOperations count: {ops_count}")

    # Histogram → HTML
    fig = px.bar(
        x=counts.index,
        y=counts.values,
        labels={"x": "Department", "y": "Count"},
        title="Department Distribution (Synthetic Employee Dataset)",
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        template="plotly_white",
        margin=dict(t=50, b=150)
    )
    fig.write_html(OUTPUT_HTML, include_plotlyjs="cdn")

    print(f"\n[ok] Wrote interactive HTML to: {os.path.abspath(OUTPUT_HTML)}")

if __name__ == "__main__":
    main()

