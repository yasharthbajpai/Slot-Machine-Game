import random

def roll():
    max_val = 6
    min_val = 1
    return random.randint(min_val, max_val)

while True:
    players = input("Enter number of players(2 to 4 only): ")
    if players.isdigit() and 2 <= int(players) <= 4:
        players = int(players)
        break
    else:
        print("Invalid input. Try again.")



while True:
    max_score = input("Enter the score to win: ")
    if max_score.isdigit() and int(max_score) > 0:
        max_score = int(max_score)
        break
    else:
        print("Invalid input. Try again.")
	


player_scores = [0] * players
player_names = []
for i in range(players):
    player_names.append(input(f"Enter name of player {i+1}: "))




while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_names[player_idx]}'s turn")
        print(f"Current score: {player_scores[player_idx]}")
        turn_score = 0
        while True:
            choice = input("Roll or Hold? (r/h): ")
            if choice == "r":
                roll_val = roll()
                print(f"Roll: {roll_val}")
                if roll_val == 1:
                    turn_score = 0
                    break
                else:
                    turn_score += roll_val
                    print(f"Turn score: {turn_score}")
            elif choice == "h":
                break
            else:
                print("Invalid input. Try again.")

        player_scores[player_idx] += turn_score
        print(f"Turn score: {turn_score}")
        print(f"Total score: {player_scores[player_idx]}")

        if player_scores[player_idx] >= max_score:
            print(f"\nPlayer {player_names[player_idx]} wins!")
            print("Woohoo! ❗❗❗❗❗❗❗❗❗❗❗❗❗")
            exit()  