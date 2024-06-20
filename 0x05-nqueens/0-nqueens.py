#!/usr/bin/python3
"""
cheass Solution  that takes to the nqueens problem
"""
import sys


def solve_backtrack(row, new, col, postive, negtive, board):
    """
    balets bakc it thae soltion and solution
    """
    if row == new:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(new):
        if c in col or (row + c) in postive or (row - c) in negtive:
            continue

        col.add(c)
        postive.add(row + c)
        negtive.add(row - c)
        board[row][c] = 1

        solve_backtrack(row+1, new, col, postive, negtive, board)

        col.remove(c)
        postive.remove(row + c)
        negtive.remove(row - c)
        board[row][c] = 0


def new_queens(new):
    """
    Solution to nqueens proble
    """
    col = set()
    postive_d = set()
    negtive_d = set()
    board = [[0] * new for i in range(new)]

    solve_backtrack(0, new, col, postive_d, negtive_d, board)


if __name__ == "__main__":
    new = sys.argv
    if len(new) != 2:
        print("Usage: new_queens N")
        sys.exit(1)
    try:
        n_n = int(new[1])
        if n_n < 4:
            print("N must be at least 4")
            sys.exit(1)
        new_queens(n_n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
