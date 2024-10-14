import random


class Cell():

    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole():

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]

        #   shuffle mines
        all_pairs = [(i, j) for i in range(self.N) for j in range(self.N)]
        all_mines = [
            mine_pair for mine_pair in random.sample(all_pairs, self.M)]
        """
        i_around и j_around — это переменные, которые используются в циклах для 
        перебора индексов ячеек, окружающих текущую ячейку с миной.
        
        i и j — это координаты ячейки, где размещена мина.
        """
        for (i, j) in all_mines:
            """
            мы проходим циклом не по всем сочетаниям, 
            а только по сочетаниям с минами
            """
            self.pole[i][j].mine = True
            for i_around in range(i - 1, i + 2):
                for j_around in range(j - 1, j + 2):
                    if (i_around >= 0 and i_around < self.N and j_around >= 0
                            and j_around < self.N and not (i_around == i
                                                           and j_around == j)):
                        self.pole[i_around][j_around].around_mines += 1

    def show(self):
        for row in self.pole:
            for element in row:
                if not element.fl_open:
                    if element.mine:
                        print("*", end=" ")
                    else:
                        if element.around_mines > 0:
                            print(element.around_mines, end=" ")
                        else:
                            print(" ", end=" ")
                else:
                    print("#", end=" ")
            print()


#   исполняемый код
pole_game = GamePole(10, 12)
pole_game.show()
