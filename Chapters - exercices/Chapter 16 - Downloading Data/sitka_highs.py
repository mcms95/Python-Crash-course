from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
# print(header_row)

# print header's index
# for index, header_name in enumerate(header_row):
#   print(f"{index} {header_name}")

# Extract high temperatures
dates, highs, lows = [], [], []

for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(date)
    high = int(row[4])
    highs.append(high)
    low = int(row[5])
    lows.append(low)

# Plot high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

# Format plot
ax.set_title("Daily High and Low Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
ax.set_ylabel('Temperature', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
