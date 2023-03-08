import sys
import io
import threading


class chessBoard:

    def __init__(self, p1=[], p2=[], turn=0, asAI=0):
        # turn represents the total number of turns taken
        # asAI represents the number of turns that p2 has taken while as an AI
        # this enables tracking turn numbers even when switching p2 between person and AI
        self.turn = turn
        self.asAI = asAI
        r1 = []
        r2 = []
        r3 = []
        r4 = []
        r5 = []
        r6 = []
        r7 = []
        r8 = []

        if len(p1) is 0:
            # default board
        else:
            # load existing board

        if len(p2) is 0:
            # default board

        else:
            # load existing board


def main():
    args = sys.argv[1:]
    if len(args) is 0:
        # default board
        board = chessBoard()

    elif len(args) is 66 or args[0] is 66:
        # random easter egg that probably no one will find unless they actually look at the code
        print("Execute Order 66")
        exit()

    else:
        # load existing board

    p1Win = False
    p2Win = False

    while p1Win is False and p2Win is False:


def minimaxDispatch():


def maxVal():


def minVal():
