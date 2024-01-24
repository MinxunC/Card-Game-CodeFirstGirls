from pickPokemon import random_pokemon

def run():
    current_round = 0
    total_rounds = int(input('How many rounds would you like to play? '))  # Allow player to choose the number of rounds
    my_wins = 0
    opponent_wins = 0
    while current_round < total_rounds:
        current_round += 1
        print('ROUND {}\n'.format(current_round))
        my_pokemon = random_pokemon()
        print('You were given {}'.format(my_pokemon['name']))
        stat_choice = input('Which stat do you want to use? (id, height, weight) ').lower() # in case user enter upcase letter
        opponent_pokemon = random_pokemon()
        print('The opponent chose {}\n'.format(opponent_pokemon['name']))
        my_stat = my_pokemon[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]

        # Inform player of chosen stat values
        print("Your pokemons {}  is {}".format(stat_choice, my_pokemon[stat_choice]))
        print("Opponent's {} is {}".format(stat_choice, opponent_pokemon[stat_choice]))

        if my_stat > opponent_stat:
            print('You Win!\n\n')
            my_wins += 1  # store win score in a variable
        elif my_stat < opponent_stat:
            print('You Lose!\n\n')
            opponent_wins += 1
        else:
            print('Draw!\n\n')

    else:
        print('GAME OVER')
        my_score = (my_wins / total_rounds) * 10
        if my_wins > opponent_wins:
            print('You win, with {} out of {} games, congrats!'.format(my_wins, total_rounds))
        elif my_wins < opponent_wins:
            print('The opponent wins, with {} out of {} games'.format(opponent_wins, total_rounds))
        else:
            print("It's a tie!")
        return my_score