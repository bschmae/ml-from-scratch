def check_if_winner(board):
    win_object = {
        'isWinner': False,
        'playerSymbol': None
    }

    # Check horizontally
    for row in board:
        if row[0] != '' and row[0] == row[1] == row[2]:
            win_object['isWinner'] = True
            win_object['playerSymbol'] = row[0]
            return win_object

    # Check vertically
    for col in range(3):
        if board[0][col] != '' and \
            board[0][col] == board[1][col] == board[2][col]:
            win_object['isWinner'] = True
            win_object['playerSymbol'] = board[0][col]
            return win_object

    # Check diagonally
    center = board[1][1]
    if center != '':
        if center == board[0][0] == board[2][2]:
            win_object['isWinner'] = True
            win_object['playerSymbol'] = center
            return win_object

        if center == board[2][0] == board[0][2]:
            win_object['isWinner'] = True
            win_object['playerSymbol'] = center
            return win_object

    return win_object


def check_if_draw(board):
    is_draw = True

    for row in board:
        for col in row:
            if col == '':
                is_draw = False
                break

    return is_draw
