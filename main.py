actions = [(-1, 0), (1,0), (0,-1), (0,1)]   # [up, down, left, right]
board = [[-1, -1, -1], [-1, -10, 10]]   # [[empty, empty, empty], [empty, poison, cheese]]

def take_action(state: tuple[int, int], action: int) -> tuple[int, tuple[int, int]]:
    """
    Docstring for take_action
    
    :param state: The position (i, j) of mouse
    :type state: tuple[int, int]
    :param action: The action the mouse will take. 0 is up, 1 is down, 2 is left, 3 is right
    :type action: int
    :return: Reward received (as an int) and new position/state 
    :rtype: tuple[int, tuple[int, int]]
    """
    
