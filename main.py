class environment:
    def __init__(self):
        self.actions = [(-1, 0), (1,0), (0,-1), (0,1)]   # [up, down, left, right]
        self.board = [[-1, -1, -1], [-1, -10, 10]]   # [[empty, empty, empty], [empty, poison, cheese]]
        self.state = (0, 0)

    def take_action(self, state: tuple[int, int], action: int) -> tuple[int, tuple[int, int], bool]:
        """
        Docstring for take_action
        
        :param state: The position (i, j) of mouse
        :type state: tuple[int, int]
        :param action: The action the mouse will take. 0 is up, 1 is down, 2 is left, 3 is right
        :type action: int
        :return: 
                int: Reward received (as an int)
                tuple[int, int]: New position/state 
                bool: False if episode has terminated, True if still active  
        :rtype: tuple[int, tuple[int, int], bool]
        """
        i, j = state
        r = i + self.actions[action][0]
        c = j + self.actions[action][1]
        if r < 0 or r >= len(self.board) or c < 0 or c >= len(self.board[0]):    # out of bounds
            self.state = (i, j)
            return (self.board[i][j], (i, j), True)
        elif self.board[r][c] != -1:
            self.state = (r, c)
            return (self.board[r][c], (r, c), False)
        else:
            self.state = (r, c)
            return (self.board[r][c], (r, c), True)



