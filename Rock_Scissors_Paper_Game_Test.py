import Rock_Scissors_Paper_Game as rps
import pytest


def test_check_validity_rock():
    # Arrange
    x: str = "rock";
    expected: int = 2;

    # Act
    actual: int = rps.check_validity(x);

    # Assert
    assert actual == expected;


def test_check_validity_scissors():
    # Arrange
    x: str = "scissors";
    expected: int = 1;

    # Act
    actual: int = rps.check_validity(x);

    # Assert
    assert actual == expected;


def test_check_validity_paper():
    # Arrange
    x: str = "paper";
    expected: int = 0;

    # Act
    actual: int = rps.check_validity(x);

    # Assert
    assert actual == expected;


def test_check_validity_latter():
    # Arrange
    x: list[str] = ['ROCK', 'SCISSORS', 'PAPER', 'rock', 'scissors', 'paper'];
    expected: list[int] = [2, 1, 0, 2, 1, 0];

    # Act
    actual: list[int] = [];
    for item in x:
        actual.append(rps.check_validity(item));

    # Assert
    assert actual == expected;


def test_check_validity_error():
    # Arrange
    x: str = "p";

    # Act
    with pytest.raises(ValueError) as ex:
        actual: int = rps.check_validity(x)

    # Assert
    assert str(ex.value) == "illegal choice";


def test_check_winner():
    # Arrange
    x: list[list[str]] = [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'],
                          ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'],
                          ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']];

    expected: list[int] = [0, 2, 1, 1, 0, 2, 2, 1, 0];

    # Act
    actual: list[int] = [];
    for item in x:
        player1_choice: int = rps.check_validity(item[0]);
        player2_choice: int = rps.check_validity(item[1]);
        actual.append(rps.check_winner(player1_choice, player2_choice));

    # Assert
    assert actual == expected;


def test_check_winner_error():
    # Arrange
    x: int = 5;
    y: int = 2;

    # Act
    with pytest.raises(ValueError) as ex:
        actual: int = rps.check_winner(x, y);

    # Assert
    assert str(ex.value) == "illegal game option";
