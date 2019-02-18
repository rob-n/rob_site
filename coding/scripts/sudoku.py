

class SudokuGrid:
    def __init__(self, starting_nums):
        """Class to display the grid in a nice format.

        :param starting_nums: starting values in Sudoku puzzle.
        """
        self.rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.cols = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.row_defs, self.col_defs = self.get_row_column_defs()
        self.grid_values = [a + b for a in self.rows for b in self.cols]
        self.peer_squares = self.get_peer_squares()
        self.puzzle_values = {}
        for idx, value in enumerate(starting_nums):
            self.puzzle_values[self.grid_values[idx]] = value

    def __str__(self):
        values = []
        for key, value in self.puzzle_values.items():
            values.append(value)
        grid = ''
        grid += ' ===+===+===++===+===+===++===+===+===\n'
        index = 0
        for i in range(9):
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    grid += '|| '
                else:
                    grid += '| '
                grid += f'{values[j + index]} '
            grid += '|\n'
            if (i + 1) % 3 == 0:
                grid += ' ===+===+===++===+===+===++===+===+===\n'
            else:
                grid += '|___|___|___||___|___|___||___|___|___|\n'
            index += 9

        return grid

    @staticmethod
    def get_row_column_defs():
        """Gets all possible rows and columns.

        :return: rows, columns
        """
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        cols = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        row_list = []
        for idx, _ in enumerate(rows):
            row_def = []
            for col in cols:
                row_def.append(rows[idx] + col)
            row_list.append(row_def)

        col_list = []
        for idx, _ in enumerate(cols):
            col_def = []
            for row in rows:
                col_def.append(row + cols[idx])
            col_list.append(col_def)

        return row_list, col_list

    @staticmethod
    def get_peer_squares():
        """
        Gets all possible values for each peer square.
        :return: list of peer squares.
        """
        peer_rows = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        peer_cols = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        peers = []
        for idx, _ in enumerate(peer_rows):
            for x in range(3):
                peers.append([a + b for a in peer_rows[idx] for b in peer_cols[x]])
        return peers


class SudokuSolver:
    def __init__(self, grid: SudokuGrid):
        """
        Solves Sudoku puzzles.

        :param grid: SudokuGrid
        """
        self.grid = grid
        self.possible_nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        self.rows = []
        self.squares = self.get_all_squares()
        self.row_index = self.get_row_index()
        self.col_index = self.get_col_index()
        self.peer_index = self.get_peer_index()
        self.columns = []
        self.peers = []
        self.get_values()
        self.solved = False
        self.count = 0
        self.possible = self.check_possible()

    def check_possible(self):
        """
        Makes sure the puzzle is possible to complete.
        :return: False if impossible, true if possible.
        """
        for row in self.rows:
            if len(row) != len(set(row)):
                return False
        for col in self.columns:
            if len(col) != len(set(col)):
                return False
        for peer in self.peers:
            if len(peer) != len(set(peer)):
                return False
        return True

    def solve_puzzle(self):
        """
        Recurses through each square in grid checking for each possible value.

        :return: False if not solved or no more possible values for square.
        """
        if self.possible is False:
            return False
        if self.solved:
            return True
        for square in self.grid.grid_values:  # loops through each square
            value = self.grid.puzzle_values[square]
            if value == '-':
                possible = self.possible_square_values(square)
                if len(possible) == 0:
                    return False
                for val in possible:  # set possible value as square, then call self function to recurse.
                    self.count += 1
                    self.rows[self.row_index[square]].append(val)
                    self.columns[self.col_index[square]].append(val)
                    self.peers[self.peer_index[square]].append(val)
                    self.grid.puzzle_values[square] = val
                    if self.solve_puzzle() is False and not self.solved:
                        self.rows[self.row_index[square]].remove(val)
                        self.columns[self.col_index[square]].remove(val)
                        self.peers[self.peer_index[square]].remove(val)
                        self.grid.puzzle_values[square] = '-'
                    else:
                        break
                if self.puzzle_solved():
                    self.solved = True
                return False

    def possible_square_values(self, square):
        """Takes numbers 1 through 9 and attempts to remove them from the row, column, and peer.

        :param square: Square to check possible numbers of.
        :return: list of remaining numbers (possibly empty list).
        """
        possible_nums = list(self.possible_nums)
        for num in self.rows[self.row_index[square]]:
            if num in possible_nums:
                possible_nums.remove(num)
        for num in self.columns[self.col_index[square]]:
            if num in possible_nums:
                possible_nums.remove(num)
        for num in self.peers[self.peer_index[square]]:
            if num in possible_nums:
                possible_nums.remove(num)
        return possible_nums

    def puzzle_solved(self):
        """Checks that all rows, columns, and peers contain numbers 1-9"""
        for row in self.rows:
            for num in self.possible_nums:
                if num not in row:
                    return False
        for col in self.columns:
            for num in self.possible_nums:
                if num not in col:
                    return False
        for peer in self.peers:
            for num in self.possible_nums:
                if num not in peer:
                    return False
        return True

    def get_all_squares(self):
        """
        Gets all the sudoku squares.
        :return: List of all squares in a sudoku puzzle
        """
        return [a + b for a in self.grid.rows for b in self.grid.cols]

    def get_row_index(self):
        """
        Creates dictionary of squares with the row index they belong to.
        :return: dictionary of row indexes.
        """
        row_indexes = {}
        for square in self.squares:
            for idx, row in enumerate(self.grid.row_defs):
                if square in row:
                    row_indexes[square] = idx
        return row_indexes

    def get_col_index(self):
        """
        Creates dictionary of squares with the peer index they belong to.
        :return: dictionary of peer indexes.
        """
        col_indexes = {}
        for square in self.squares:
            for idx, col in enumerate(self.grid.col_defs):
                if square in col:
                    col_indexes[square] = idx
        return col_indexes

    def get_peer_index(self):
        """
        Creates dictionary of squares with the peer index they belong to.
        :return: dictionary of peer indexes.
        """
        peer_indexes = {}
        for square in self.squares:
            for idx, peer in enumerate(self.grid.peer_squares):
                if square in peer:
                    peer_indexes[square] = idx
        return peer_indexes

    def get_values(self):
        """
        Sets the base values for each row, column, and peer.
        """
        row_values = []
        for row in self.grid.rows:
            row_list = []
            for col in self.grid.cols:
                row_list.append(self.grid.puzzle_values[f"{row}{col}"])
                try:
                    row_list.remove('-')
                except ValueError:
                    pass
            row_values.append(row_list)
        self.rows = row_values

        col_values = []
        for col in self.grid.cols:
            col_list = []
            for row in self.grid.rows:
                col_list.append(self.grid.puzzle_values[f"{row}{col}"])
                try:
                    col_list.remove('-')
                except ValueError:
                    pass
            col_values.append(col_list)
        self.columns = col_values

        peer_rows = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        peer_cols = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        peer_values = []
        for idx in range(3):
            for idx2 in range(3):
                peer_list = []
                for i in range(3):
                    for j in range(3):
                        peer_list.append(
                            self.grid.puzzle_values[f"{peer_rows[idx][i]}{peer_cols[idx2][j]}"]
                        )
                        try:
                            peer_list.remove('-')
                        except ValueError:
                            pass
                peer_values.append(peer_list)
        self.peers = peer_values


