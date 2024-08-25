def check_validity(choice: str) -> int:
    """
    Validates the player's choice and converts it to a corresponding number.

    Args:
        choice (str): The player's choice as a string ("rock", "scissors", or "paper").

    Returns:
        int: 2 for "rock", 1 for "scissors", 0 for "paper".

    Raises:
        ValueError: If the choice is not one of the expected strings.
    """
    choice = choice.lower();
    if choice == "rock":
        return 2;
    elif choice == "scissors":
        return 1;
    elif choice == "paper":
        return 0;
    else:
        raise ValueError("illegal choice");


def check_winner(player1_choice: int, player2_choice: int) -> int:
    """
    Determines the winner between two players based on their choices.

    Args:
        player1_choice (int): The first player's choice (0 for paper, 1 for scissors, 2 for rock).
        player2_choice (int): The second player's choice (0 for paper, 1 for scissors, 2 for rock).

    Returns:
        int: 1 if the first player won, 2 if the second player won, 0 if it's a tie.

    Raises:
        ValueError: If any of the choices is not 0, 1, or 2.
    """
    if player1_choice not in [0, 1, 2] or player2_choice not in [0, 1, 2]:
        raise ValueError("illegal game option");

    # Rock beats Scissors, Scissors beats Paper, Paper beats Rock
    if player1_choice == player2_choice:
        return 0;
    elif (player1_choice == 2 and player2_choice == 1) or \
            (player1_choice == 1 and player2_choice == 0) or \
            (player1_choice == 0 and player2_choice == 2):
        return 1;
    else:
        return 2;


def game_play() -> None:
    """
    Manages the game by getting player choices, determining the winner,
    and displaying the result. After each game, prompts the players to
    either play again or quit.
    """
    print("\nWelcome to Rock-Paper-Scissors!");

    while True:

        player1_input: str = input("Player 1, enter your choice (rock, paper, scissors): ").strip();
        player2_input: str = input("Player 2, enter your choice (rock, paper, scissors): ").strip();

        try:
            player1_choice: int = check_validity(player1_input);
            player2_choice: int = check_validity(player2_input);

            result: int = check_winner(player1_choice, player2_choice);

            if result == 0:
                print("It's a tie!");
            elif result == 1:
                print("Player 1 wins!");
            else:
                print("Player 2 wins!");
            break;
        except ValueError as e:
            print(e);

        # Prompt the players if they want to play again or quit
    play_again: str = input("Do you want to play again? (yes/no): ").strip().lower();
    if play_again != 'yes':
        print("Thank you for playing! Goodbye!");
    else:
        game_play();