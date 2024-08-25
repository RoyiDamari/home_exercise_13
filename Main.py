import Rock_Scissors_Paper_Game as rps


if __name__ == "__main__":
    try:
        rps.game_play();

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting.");

