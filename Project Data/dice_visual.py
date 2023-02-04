import plotly.express as px
from dice import Dice

dice1 = Dice()
dice2 = Dice()
dice3 = Dice()

results = []
for i in range(10_000):
    result = dice1.roll() + dice2.roll() + dice3.roll()
    results.append(result)

frequencies = []
max_result = dice1.num_sides + dice2.num_sides + dice3.num_sides
possible_results = range(3, max_result+1)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize
title = "Results of D6 and D10 rollerd 10_000 times!"
labels = {'x': 'Result', 'y': 'Frequency'}
graph = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
graph.show()

graph.write_html('dice_visual_d6d10.html')
