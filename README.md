# Employee Performance Visualization

Author / Contact: 22f3001685@ds.study.iitm.ac.in

This repository contains a simple analysis and interactive visualization of employee department frequencies.

Files:
- employee_viz.py — loads the dataset, prints department counts (Operations included), and writes an interactive HTML bar chart departments_hist.html
- departments_hist.html — generated interactive visualization (bar chart)

How to run (locally):
1. Install dependencies: pip install pandas plotly openpyxl
2. Run: python employee_viz.py
3. Open departments_hist.html in a browser.

Notes:
- The script expects a dataset with a "Department" column (or similar).
- For grader evaluation, DATA_PATH in employee_viz.py points to the uploaded dataset path: /mnt/data/q-excel-correlation-heatmap.xlsx
- This work used LLM assistance (ChatGPT/Codex) for coding support: https://chatgpt.com/codex/tasks
