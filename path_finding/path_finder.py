from path_finding.bfs_v2 import bfs
from cygni import util

class PathFinder:
    def __init__(self):
        pass

    def get_actions(self, environment, width, height):
        pass


class NaivePathFinder(PathFinder):
    def __init__(self):
        super(PathFinder, self).__init__()

    def get_actions(self, environment, width, height):
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        actions = []
        apple = [-1, -1]
        head = [-1, -1]
        for i in range(len(environment)):
            for j in range(len(environment[i])):
                if environment[i][j] >= 3.:
                    apple = [i, j]
                elif environment[i][j] >= 2.:
                    head = [i, j]

        diffX = apple[0] - head[0]
        diffY = apple[1] - head[1]

        print(diffX)
        print(diffY)

        if not diffX == 0:
            if diffX < 0:
                for i in range(int(abs(diffX))):
                    actions.append(UP)
            elif diffX > 0:
                for i in range(int(abs(diffX))):
                    actions.append(DOWN)

        if not diffY == 0:
            if diffY < 0:
                for i in range(int(abs(diffY))):
                    actions.append(LEFT)
            elif diffY > 0:
                for i in range(int(abs(diffY))):
                    actions.append(RIGHT)

        return actions


class BFS(PathFinder):
    def __init__(self):
        super(BFS, self).__init__()
        self.actions = [util.Direction.DOWN, util.Direction.LEFT, util.Direction.UP, util.Direction.RIGHT]
        self.last_action = 0

    def find_start_pos(self, environment) -> (int, int):
        for i in range(len(environment)):
            for j in range(len(environment[i])):
                if 1 < environment[i][j] < 3:
                    return j, i

    def get_actions(self, environment, width, height):

        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        actions = []

        start = self.find_start_pos(environment=environment)
        clear = 0.
        path = bfs.bfs(grid=environment, start=start, goal=3., width=width, height=height, wall=1.)
        if path is None:
            print("NO SOLUTION!")
            return []

        last_pos = start

        for i in range(1, len(path)):
            if path[i][0] > last_pos[0]:
                actions.append(RIGHT)
            elif path[i][0] < last_pos[0]:
                actions.append(LEFT)

            if path[i][1] > last_pos[1]:
                actions.append(DOWN)
            elif path[i][1] < last_pos[1]:
                actions.append(UP)

            last_pos = path[i]

        return actions

    def get_next_action(self, environment, width, height):
        current = self.find_start_pos(environment=environment)

        path = bfs.bfs(grid=environment, start=current, goal=3., width=width, height=height, wall=1.)
        if path is None:
            self.last_action+=1
            print("NO SOLUTION!")
            return self.actions[self.last_action%4]

        print(path[0][0])

        last_pos = current

        if path[1][0] > last_pos[0]:
            self.last_action = 2
            return util.Direction.RIGHT
        elif path[1][0] < last_pos[0]:
            self.last_action = 0
            return util.Direction.LEFT

        if path[1][1] > last_pos[1]:
            self.last_action = 3
            return util.Direction.DOWN
        elif path[1][1] < last_pos[1]:
            self.last_action = 1
            return util.Direction.UP
