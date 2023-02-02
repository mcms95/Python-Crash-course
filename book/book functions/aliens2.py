# store the aliens
aliens = []

# generate the alliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'spped': 'low'}
    aliens.append(new_alien)

# changing aliens along the game
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# show first 5 aliens
for alien in aliens[:5]:
    print(alien)
