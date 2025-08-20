# employee_performance.py
# Author: 24f2001915@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

# ---- Step 1: Load dataset ----
# You can replace this with your actual CSV file
data = {
    "EmployeeID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Department": [
        "Operations", "HR", "IT", "Finance", "Operations",
        "Operations", "HR", "IT", "Finance", "Operations"
    ],
    "Region": ["East", "West", "North", "South", "East", "West", "North", "South", "East", "West"],
    "PerformanceScore": [80, 72, 91, 65, 87, 93, 70, 88, 77, 85]
}

df = pd.DataFrame(data)

# ---- Step 2: Frequency count for Operations ----
operations_count = df[df["Department"] == "Operations"].shape[0]
print("Frequency count for Operations Department:", operations_count)

# ---- Step 3: Histogram of department distribution ----
plt.figure(figsize=(8, 6))
df["Department"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")

plt.title("Department Distribution of Employees")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.tight_layout()

# Save as HTML (embedding the PNG inside)
html_output = "employee_distribution.html"
png_file = "department_hist.png"
plt.savefig(png_file)

with open(html_output, "w") as f:
    f.write(f"""
    <html>
    <head><title>Employee Performance Visualization</title></head>
    <body>
    <h2>Department Distribution of Employees</h2>
    <p>Email for verification: 24f2001915@ds.study.iitm.ac.in</p>
    <p>Frequency count for Operations Department: {operations_count}</p>
    <img src="{png_file}" alt="Histogram">
    </body>
    </html>
    """)

print(f"HTML file saved as: {html_output}")
