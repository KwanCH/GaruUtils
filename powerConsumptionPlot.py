import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a dataframe from the given data
data = {
    "Time": ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00"],
    "Garu": [100, 100, 99, 98, 97, 97, 96, 96, 95, 95, 94, 93, 92],
    "Samsung Health": [100, 98, 96, 94, 93, 91, 89, 87, 86, 84, 82, 81, 79]
}

df = pd.DataFrame(data)

# Convert time to a numeric format for plotting
time_numeric = np.arange(len(df))

# Fit a linear regression model for Garu
garu_fit = np.polyfit(time_numeric, df["Garu"], 1)
garu_poly = np.poly1d(garu_fit)

# Fit a linear regression model for Samsung Health
samsung_fit = np.polyfit(time_numeric, df["Samsung Health"], 1)
samsung_poly = np.poly1d(samsung_fit)

# Create extended time points to predict until battery reaches 0%
extended_time_numeric = np.arange(len(df) + 10)  # Extending beyond the given data points

# Create labels for the extended time (every 30 minutes up to the extended time)
extended_time_labels = [f"{i//2:02}:{(i%2)*30:02}" for i in extended_time_numeric]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_numeric, df["Garu"], marker='o', label="Garu")
plt.plot(time_numeric, df["Samsung Health"], marker='o', label="Samsung Health")

# Annotating the graph
plt.xlabel('Time (hours)')
plt.ylabel('Battery Percentage')
plt.title('Remaining Battery Percentage Over Time')
plt.xticks(time_numeric, df["Time"], rotation=45)

plt.yticks(np.arange(75, 101, 1))

plt.legend()
plt.grid(True)

# Show plot
plt.show()