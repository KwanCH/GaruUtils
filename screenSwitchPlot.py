import matplotlib.pyplot as plt
import pandas as pd

# File path
file_path = 'SST.txt'

# Initialize data structure
data = {
    "Switch": [],
    "Screen": [],
    "Duration_ms": []
}

# Read from file and parse data
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(": ")
        switch_number = int(parts[0].split(" ")[1])
        screen = parts[1].split(" ")[2]
        duration = float(parts[2].split(" ")[0])
        data["Switch"].append(switch_number)
        data["Screen"].append(screen)
        data["Duration_ms"].append(duration)

# Convert to DataFrame
df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots(figsize=(15, 7))
colors = {'friends': 'blue', 'home': 'green', 'history': 'red'}  # Define colors for each screen

# Averages and Text Display
average_durations = []  # To store average durations for display

for screen in df["Screen"].unique():
    subset = df[df["Screen"] == screen]
    avg_duration = subset["Duration_ms"].mean()  # Calculate average duration
    ax.plot(subset["Switch"], subset["Duration_ms"], label=f'Navigation to {screen}', marker='o', color=colors[screen])
    average_durations.append(f"{screen.capitalize()} avg: {avg_duration:.3f} ms")

# Prepare text for display
avg_text = "\n".join(average_durations)
# Adjust the text position to be above the legend in the bottom right corner, add more vertical padding
plt.text(0.95, 0.23, avg_text, transform=ax.transAxes, fontsize=9, verticalalignment='top', horizontalalignment='right', color='black')


ax.set_title('Navigation Duration for Different Screens')
ax.set_ylabel('Duration (ms)')
ax.set_xlabel('Screen Switches')

legend = ax.legend(loc='lower right')
plt.show()
