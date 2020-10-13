class PathFinder:
    def __init__(self):
        pass

    def get_actions(self, environment):
        pass


class NaivePathFinder(PathFinder):
    def __init__(self):
        super(PathFinder, self).__init__()

    def get_actions(self, environment):
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

    def get_actions(self, environment):
        return []
