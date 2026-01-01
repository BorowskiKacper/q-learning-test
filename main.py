import random

class Environment:
    def __init__(self):
        self.actions = [(-1, 0), (1,0), (0,-1), (0,1)]   # [up, down, left, right]
        self.board = [[-1, 1, -1], [-1, -10, 10]]   # [[empty, cheese, empty], [empty, poison, win_cheese]]
        self.state = (0, 0)

    def reset(self):
        self.actions = [(-1, 0), (1,0), (0,-1), (0,1)]   # [up, down, left, right]
        self.board = [[-1, 1, -1], [-1, -10, 10]]   # [[empty, cheese, empty], [empty, poison, win_cheese]]
        self.state = (0, 0)


    def take_action(self, action: int) -> tuple[int, tuple[int, int], bool]:
        """
        Docstring for take_action
        
        :param action: The action the mouse will take. 0 is up, 1 is down, 2 is left, 3 is right
        :type action: int
        :return: 
                int: Reward received (as an int)
                tuple[int, int]: New position/state 
                bool: False if episode has terminated, True if still active  
        :rtype: tuple[tuple[int, int], bool]
        """
        i, j = self.state
        r = i + self.actions[action][0]
        c = j + self.actions[action][1]
        if r < 0 or r >= len(self.board) or c < 0 or c >= len(self.board[0]):    # out of bounds
            self.state = (i, j)
            return (-5, (i, j), True)
        elif self.board[r][c] not in [-1, 1]:
            self.state = (r, c)
            return (self.board[r][c], (r, c), False)
        else:
            self.state = (r, c)
            return (self.board[r][c], (r, c), True)

class agent:
    def __init__(self, env: Environment):
        self.qtable = [[[0 for ac in env.actions] for cell in row] for row in env.board]
        self.env = env

    def choose_random_move(self) -> int:
        return random.randint(0, len(self.env.actions) - 1)
    
    def choose_optimal_move(self, state) -> int:
        i, j = state
        max_probability = max(self.qtable[i][j])
        return self.qtable[i][j].index(max_probability)

    
    def q_learning(self, num_episodes: int, alpha: float, discount_rate: float, min_epsilon: float, max_moves: int):
        """
        Docstring for q_learning
        
        :param self: Description
        :param num_episodes: Description
        :type num_episodes: int
        :param alpha: learning rate
        :type alpha: float


        """

        
        for _ in range(num_episodes):
            state = (0,0)
            epsilon = 1 - (_/num_episodes)*(1-min_epsilon)

            for __ in range(max_moves):
                # choose action a
                a = self.choose_random_move() if random.random() < epsilon else self.choose_optimal_move(state)
                r, new_state, alive = self.env.take_action(a)

                i, j = state
                ni, nj = new_state
                self.qtable[i][j][a] = self.qtable[i][j][a] + alpha*(r + discount_rate*max(self.qtable[ni][nj]) - self.qtable[i][j][a])

                state = new_state

                if not alive:
                    break

            print("-------------------------------------------------------------------------")
            print(env.state)
            print(mouse.qtable)
            self.env.reset()

    def play_episode(self, max_moves: int) -> bool:
        def print_game(state):
            i, j = state
            print("="*7)
            print("|" + ("m" if i == 0 and j == 0 else " ") + "|" + ("m" if i == 0 and j == 1 else " ") + "|" + ("m" if i == 0 and j == 2 else " ") + "|")
            print("-"*7)
            print("|" + ("m" if i == 1 and j == 0 else " ") + "|" + ("m" if i == 1 and j == 1 else " ") + "|" + ("m" if i == 1 and j == 2 else " ") + "|")
            print("="*7)

        state = (0,0)
        print("INITIAL")
        print_game(state)
        print()
        for move in range(max_moves):
            r, new_state, alive = self.env.take_action(self.choose_optimal_move(state))

            if not alive:
                print("EPISODE TERMINATED")
                print_game(new_state)
                self.env.reset()
                if new_state[0] == 1 and new_state[1] == 2:
                    return True
                else:
                    return False

            print(f"Move: {move + 1}")
            print_game(new_state)
            state = new_state

        self.env.reset()
        return False


env = Environment()


wins = 0
games = 500
for i in range(games):
    mouse = agent(env)
    mouse.q_learning(30, 0.1, 0.95, 0.03, 10)
    if mouse.play_episode(20):
        wins += 1

print(f"win/loss ratio: {wins/games} | wins: {wins}")




