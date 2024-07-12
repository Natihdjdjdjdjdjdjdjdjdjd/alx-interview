#!/usr/bin/python3
""" Maria and Ben are playing a game.
"""


def isWinner(x, nums):
    """
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.
    """
    Ben = 0
    Maria = 0

    for round in range(x):
        num_play = [num for num in range(2, nums[round] + 1)]
        i = 0
        # Sieve prime numbers per round
        while (i < len(num_play)):
            current_prime = num_play[i]
            sieve_index = i + current_prime
            while(sieve_index < len(num_play)):
                num_play.pop(sieve_index)
                sieve_index += current_prime - 1
            i += 1
        # Determine winner - if number of primes is even player 1 wins
        prime_count = (len(num_play))
        if prime_count and prime_count % 2:
            Maria += 1
        else:
            Ben += 1

    if Ben == Maria:
        return None
    return 'Ben' if Ben > Maria else 'Maria'
