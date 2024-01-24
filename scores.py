import csv
from csv import writer

def show_current_score(score):
    print("\n")
    print("------------------------------------")
    print("Your current score is " + str(score) + ". (The total score is 10.)")

def save_score(score):
    append_score = [score]

    with open("highscore.csv", "a") as score_file:
        writer_object = writer(score_file)  # Pass this file object to csv.writer() and get a writer object
        writer_object.writerow(append_score)
        score_file.close()

def compare_score(score):  # read csv
    history_highest_score = 0
    with open("highscore.csv", "r") as score_file:

        reader_obj = csv.reader(score_file)

        for row in reader_obj:
            for history_score in row: #use for loop to find the highest record from all history data
                if int(history_score) > history_highest_score:
                    history_highest_score = int(history_score)

    if history_highest_score >= score:
        print("Your history highest score is: ", str(history_highest_score))
    else:
        print("This is your new highest record!")