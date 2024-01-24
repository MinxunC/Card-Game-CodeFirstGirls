from scores import show_current_score 
from scores import save_score 
from scores import compare_score
from game import run


current_score = int(run())  # save my_score into the variable called current_score
show_current_score(current_score)
save_score(current_score)
compare_score(current_score)
continue_game = input(
    'Would you like to continue playing the game (please answer "y" or "n"): ').lower()  

# ask player whether you would like to continue the game. The game will not stop until user answer "n"
while continue_game == "y":
    current_score = int(run())
    show_current_score(current_score)
    save_score(current_score)
    compare_score(current_score)
    continue_game = input('Would you like to continue playing the game (please answer "y" or "n"): ')
else:
    print("Hope you have a good day")