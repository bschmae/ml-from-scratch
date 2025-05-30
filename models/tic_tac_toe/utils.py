def check_if_winner(board):
    # Check horizontally
    for row in board:
        if row[0] != '' and row[0] == row[1] == row[2]:
            return True

    # Check vertically
    for col in range(3):
        if board[0][col] != '' and \
            board[0][col] == board[1][col] == board[2][col]:
            return True

    # Check diagonally
    center = board[1][1]
    if center != '':
        if center == board[0][0] == board[2][2]:
            return True
        if center == board[2][0] == board[0][2]:
            return True

    return False
