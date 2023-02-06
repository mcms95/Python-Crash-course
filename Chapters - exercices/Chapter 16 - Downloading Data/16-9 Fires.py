from pathlib import Path
from datetime import datetime
import csv
import plotly.express as px

path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


# for index, header_name in enumerate(header_row):
#    print(f"{index} {header_name}")

lats, lons, brights, dates = [], [], [], []
for row in reader:
    lats.append(float(row[0]))
    lons.append(float(row[1]))
    brights.append(float(row[2]))
    dates.append(datetime.strptime(row[5], '%Y-%m-%d'))


title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons,
                     color=brights,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Brightness'},
                     projection='natural earth')
fig.show()
