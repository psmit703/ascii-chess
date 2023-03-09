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
        self.board =
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

        # does not currently support non-standard moves

        # r0 and c0 need to be correct - does not check those for full validity


def isValidMove(init: chessBoard, piece: str, r0: int, c0: str, r1: int, c1: str):
    if r0 > 8 or r0 < 0 or c0 > 8 or c0 < 0 or r1 > 8 or r1 < 0 or c1 > 8 or c1 < 0
    # ERROR MEESSAGE - OUT OF CHESSBOARD BOUNDS
    # print here
    print("PLACEHOLDER")
    elif not chessBoard.board[r0][c0] is piece:
        # ERROR MESSAGE - PIECE NOT AT SPECIFIED LOCATION
        pieceName = getPiece(piece)
        print("Error: " + pieceName +
              " (" + piece + ") is not at position " + POSITIONPLACEHOLDER)
        print("Please enter a valid position")
        print(
            "For a list of valid moves, enter \"-moveList [piece]\" or \"-moveList\" for valid moves for all pieces")

    if (chessBoard.board[r0][c0].isupper() and not chessBoard[r1][c1].isuppercase()) or (not chessBoard.board[r0][c0].isupper() and chessBoard.board[r1][c2].isupper()):
        # success IFF valid move position-wise
    elif chessBoard.board[r1][c1] is "":
        # ditto
    else:
        # fail


def getPiece(piece: str):
    res = []

    match piece:
        case "p":
            res = "White Pawn"
        case "r":
            res = "White Rook"
        case "n":
            res = "White Knight"
        case "b":
            res = "White Bishop"
        case "k":
            res = "White King"
        case "q":
            res = "White Queen"
        case "P":
            res = "Black Pawn"
        case "R":
            res = "Black Rook":
        case "N":
            res = "Black Knight"
        case "B":
            res = "Black Bishop":
        case "K":
            res = "Black King"
        case "Q":
            res = "Black Queen"
        case _:
            # ERROR
            res = "PLACEHOLDER"

    return res


def minimaxDispatch():


def maxVal():


def minVal():
