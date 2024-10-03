#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes needed to reach total

    Args:
        coins (List[int]): List of available coins
        total (int): Total amount needed

    Returns:
        int: Number of coins needed to make the total
            or -1 if it's not possible
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    current_total = 0

    for coin in coins:
        while current_total < total:
            current_total += coin
            num_coins += 1

        if current_total == total:
            return num_coins

        current_total -= coin
        num_coins -= 1

    return -1
