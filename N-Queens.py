def check_threats(chess_board, square):
    """ board is a matrix containing the entire chessboard at this moment, every square with a 0 value is empty and
    every square with a 1 value has a queen on it.
    square is the coordinates of a target square on the board that we are trying to check the safety of, it's a list
    containing two integers as the row and column

    This function returns False if there are no queens threatening the one in square
    :param chess_board:
    :param square:
    :return bool:
    """

    row = square[0]
    column = square[1]
    for i in range(0, len(chess_board)):
        for j in range(0, len(chess_board)):
            if chess_board[i][j] == 1:
                if i == row or j == column or abs(i - row) == abs(j - column):
                    return True

    return False


def initialize_board(size):
    # Initializing the chessboard
    chess_board = []
    for i in range(size):
        tmp_board = [0] * size
        chess_board.append(tmp_board)

    # Chessboard initialized, all the squares are empty therefore equal to 0, once there's a queen inside they will
    # be shifted to 1

    return chess_board


result = []
board = initialize_board(4)


def n_queens(row=0, column=0):
    """
    This function uses a backtracking algorithm to solve the n-queens problem where we are given n queens and an n*n
    chessboard and are asked to place the queens in a way that none of them threaten each other.

    The function prints all possible answers in a list named result meaning every result[i]=j means that there's a queen
    in the i row and the j column.
    :param row:
    :param column:
    :return:
    """
    if row >= len(board) or column >= len(board):
        raise IndexError(board, row, column)

    if row == len(board) - 1 and not check_threats(board, [row, column]):
        result.append(column)
        result2 = []
        for i in result:
            result2.append(i+1)
        print(result2)
        result.pop()
        return

    if not check_threats(board, [row, column]):
        result.append(column)
        board[row][column] = 1
        n_queens(row + 1, 0)
        result.pop()
        board[row][column] = 0

    if column == len(board) - 1:
        return

    n_queens(row, column + 1)


n_queens()
