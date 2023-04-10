#!/usr/bin/python3
"""
Define isWinner function, Prime Game problem
"""

def isPrimes(num):
    """Return list of prime numbers between  and num inclusive
        Args:
        num (int): End of range
    """
    prime_num = []
    fill = [True] * (num + 1)
    for x in range(2, num + 1):
        if (fill[x]):
            prime_num.append(x)
            for y in range(x, num + 1, x):
                fill[y] = False
    return prime_num

def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
         return None
    Maria  = 0
    Ben = 0
    for a in range(x):
        prime = isPrimes(nums[a])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None