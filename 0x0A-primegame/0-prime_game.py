#!/usr/bin/python3

"""Maria and Ben game module"""


def primer(n):
    """Checking is number is a prime number
      args:
          n: number to check
      return: True, if number is a prime number
              False, if not
    """
    isPrime = True
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break
        else:
            isPrime = True
    return isPrime


def isWinner(x, nums):
    """Module to play Maria and Bens game
      args:
          x: number of games to play
          nums: list containing the games to play
      return: the winner of the game"""
    if x == 0 or x < len(nums):
        return
    players = [0, 0]
    for i in nums:
        curList = []
        play = 0
        for c in range(2, i + 1):
            if primer(c) is True:
                curList.append(c)
        for j in range(len(curList)):
            if len(curList) == 0:
                players[1] = players[1] + 1
                break
            else:
                playerPlay = curList.pop(0)
                for k in curList:
                    if k % playerPlay == 0:
                        curList.remove(k)
            play = play + 1
        if play % 2 == 0:
            players[1] = players[1] + 1
        else:
            players[0] = players[0] + 1
    if players[0] > players[1]:
        return "Maria"
    elif players[1] > players[0]:
        return "Ben"
    elif players[0] == players[1]:
        return None
