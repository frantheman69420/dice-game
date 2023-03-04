import csv
import random

# Define function to roll secret die
def roll_dice():
    return random.randint(1, 6)

# Define function for player 1 to input guess
def player1_guessinput():
    guess = int(input("Enter your guess player 1 between 1 and 6: "))
    return guess

# Define function for player 2 to input guess
def player2_guessinput():
    guess = int(input("Enter your guess player 2 between 1 and 6: "))
    return guess

# Define function to check if guess is correct and return score
def check_guess(guess, secret):
    if guess == secret:
        return 1
    else:
        return 0

# Define main function to control game flow
def main():
    # Set round number
    round_number = 0

    # Open a CSV file to store scores
    with open('score.csv', 'w', newline='') as csvfile:
        # Define column names for CSV file
        fieldnames = ['Round', 'Player 1 Score', 'Player 2 Score', 'Computer Score','Computer1 Score','Computer2 Score',]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write column names to CSV file
        writer.writeheader()

        # Start game loop
        while True:
            # Display game menu
            print("Welcome to the dice game!")
            print("1. Play against a friend")
            print("2. Play against the computer")
            print("3. Quit")
            print("4. Automate")
            mode = input("Select a game mode: ")

            # Handle game mode selection
            if mode == "1":
                # Set player scores
                player1_score = 0
                player2_score = 0
                
                # Play rounds until someone wins
                while True:
                    # Roll secret die
                    secret = roll_dice()
                    
                    # Get player guesses
                    player1_guess = player1_guessinput()
                    player2_guess = player2_guessinput()

                    # Check player guess and update scores
                    player1_score += check_guess(player1_guess, secret)
                    player2_score += check_guess(player2_guess, secret)

                    # Increment round number
                    round_number += 1

                    # Write scores to CSV file
                    writer.writerow({'Round': round_number, 'Player 1 Score': player1_score, 'Player 2 Score': player2_score})
                    # Print scores for the round
                    print(f"Round {round_number}: Player 1 score: {player1_score}, Player 2 score: {player2_score}")

                    # Check if someone has won
                    if player1_score == 3:
                        print("Player 1 wins!")
                        break
                    elif player2_score == 3:
                        print("Player 2 wins!")
                        break
            elif mode == "2":
                # Set player and computer score
                player_score = 0
                computer_score = 0

                # Play rounds until someone wins
                while True:
                    # Roll secret die
                    secret = roll_dice()

                    # Get player guess
                    player_guess = player1_guessinput()

                    # Roll dice to generate computer guess
                    computer_roll = roll_dice()

                    # Check player and computer guesses and update scores
                    player_score += check_guess(player_guess, secret)
                    computer_score += check_guess(computer_roll, secret)

                    # Increment round number
                    round_number += 1

                    # Write scores to CSV file
                    writer.writerow({'Round': round_number, 'Player 1 Score': player_score, 'Computer score': computer_score})

                    # Print scores for the round
                    print(f"Round {round_number}: Player score: {player_score}, Computer score: {computer_score}")

                    # Check if someone has won
                    if player_score == 3:
                        print("Player wins!")
                        break
                    elif computer_score == 3:
                        print("Computer wins!")
                        break

            elif mode == "3":
                # Quit game
                break
            elif mode == "4":
    # Set the number of games to play
                num_games = int(input("Enter the number of games to play: "))

    # Set scores for the two computers
    computer1_wins = 0
    computer2_wins = 0

    # Play the specified number of games
    for i in range(num_games):
        # Set scores for this game
        computer1_score = 0
        computer2_score = 0

        # Play the game until a computer wins
        while computer1_score == computer2_score:
            # Play a round
            # Roll secret die
            secret = roll_dice()

            # Roll dice to generate guesses for the two computers
            computer1_guess = roll_dice()
            computer2_guess = roll_dice()

            # Check computer guesses and update scores
            computer1_score += check_guess(computer1_guess, secret)
            computer2_score += check_guess(computer2_guess, secret)

        # Check who won the game
        if computer1_score > computer2_score:
            computer1_score += 1
            print(f"Game {i+1}: Computer 1 wins!")
        else:
            computer2_score += 1
            print(f"Game {i+1}: Computer 2 wins!")
            # Write scores to CSV file
            writer.writerow({'Round': round_number, 'Computer1 score': computer1_score, 'Computer2 score': computer2_score})

            # Print scores for the round
            print(f"Round {round_number}:Computer1 score: {computer1_score}, Computer2 score: {computer2_score}")
        
    else:
        print("Invalid input. Please try again.")
            

if __name__ == '__main__':
    main()
