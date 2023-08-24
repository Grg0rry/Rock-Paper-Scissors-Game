#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0
        self.lastmove = ""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        def get_input():
            response = input('Rock, paper, scissors? > ').lower()
            if response not in moves:
                return get_input()
            return response
        return get_input()


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()

    def learn(self, my_move, their_move):
        self.lastmove = their_move

    def move(self):
        if self.lastmove == "":
            return RandomPlayer().move()
        else:
            return self.lastmove


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()

    def learn(self, my_move, their_move):
        self.lastmove = my_move

    def move(self):
        if self.lastmove == "":
            return RandomPlayer().move()
        else:
            try:
                return moves[moves.index(self.lastmove) + 1]
            except IndexError:
                return moves[0]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if move1 == move2:
            print('** TIE **')
        elif beats(move1, move2):
            print('** PLAYER ONE WINS **')
            self.p1.score += 1
        else:
            print('** PLAYER TWO WINS **')
            self.p2.score += 1
        print(f'Score: Player One {self.p1.score}, Player Two {self.p2.score}')

    def play_game(self):
        print("Game start!")
        print("First to three points win! \nRock Paper Scissors, Go!")
        round = 0
        while (self.p1.score < 3) and (self.p2.score < 3):
            round += 1
            print(f"\nRound {round}: --")
            self.play_round()
        print("\nGame over!")
        print('Final Score: \n'
              f'Player One: {self.p1.score} points\n'
              f'Player Two: {self.p2.score} points')
        if self.p1.score == 3:
            print("** Player One has won **")
        elif self.p2.score == 3:
            print("** Player Two has won **")
        print("Thanks for playing!")


if __name__ == '__main__':
    game = Game(CyclePlayer(), RandomPlayer())
    game.play_game()
