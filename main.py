# Top Trumps - Group 2 #

import random

# View > Tool Windows > Terminal and type 'pip install requests' to install the requests library #

import requests

# Retrieve Pokemon API and Access Stats Info to Define for Run Sequence #

def random_pokemon():
    which_pokemon = (random.randint(1, 151))
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(which_pokemon)
    response = requests.get(url)
    pokemon = response.json()
    return {
    'name': pokemon['name'],
    'id': pokemon['id'],
    'height': pokemon['height'],
    'weight': pokemon['weight'],
    'xp' : pokemon['base_experience'],
    }

# Run User Input and Print Outcome #
def run():

    my_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))
    stat_choice = input('Which stat do you want to use? (id, height, weight, xp) ')
    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))

    player_score = my_pokemon[stat_choice]
    opponent_score = opponent_pokemon[stat_choice]
    if player_score > opponent_score:
        print('You are the winner!')
    elif player_score < opponent_score:
        print('You have lost :(')
    else:
        print('It was a draw!')

run()