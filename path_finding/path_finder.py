from path_finding.bfs_v2 import bfs


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
        print(path)
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
