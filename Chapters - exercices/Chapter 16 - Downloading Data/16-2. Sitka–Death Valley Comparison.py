from datetime import datetime
import csv
import matplotlib.pyplot as plt


def get_weather(filename, date, high, low, date_index, high_index, low_index):
    # Open file to extraction
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Data missing from day {date}")
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)


# Deathvalley
filename = 'weather_data/death_valley_2021_simple.csv'
dates, highs, lows = [], [], []
get_weather(filename, dates, highs, lows, date_index=2, high_index=3,
            low_index=4)

# Plot valley data
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

# Sitka
filename = 'weather_data/sitka_weather_2021_simple.csv'
dates, highs, lows = [], [], []
get_weather(filename, dates, highs, lows, date_index=2, high_index=4,
            low_index=5)

# plot Sitka data
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)


# Format plot
ax.set_title("Daily High and Low Temperatures Valley and Sitka", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
