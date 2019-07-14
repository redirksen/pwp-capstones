# https://endlessgames.com/wp-content/uploads/Mancala_Instructions.pdf

# 48 pieces

# create empty board

board = {"A1": 0, "A2": 0, "A3": 0, "A4": 0, "A5": 0, "A6": 0, "A_main": 0, "B1": 0, "B2": 0, "B3": 0, "B4": 0, "B5": 0, "B6": 0, "B_main": 0}
board_spots = ["A1", "A2", "A3", "A4", "A5", "A6", "A_main", "B1", "B2", "B3", "B4", "B5", "B6", "B_main"]

# need to connect like A1 and B6

# Filling the board
def fill_board():
    for place in board:
        board[place] = 4
    board['A_main'] = 0
    board["B_main"] = 0

# Select Board Spot to move


def user_input():
    piece_spot = input("Which indent would you like to pull from?")
    return piece_spot

#get index of selected pieces

def make_move(piece_spot):
    game_not_over = True
    winner = "NO ONE"
    ending_board_key = "0"
    if  board.get(piece_spot) == 0:
        print ("there are no pieces to move select again")
        return
    pieces_to_move = board.get(piece_spot)

    move_index = board_spots.index(piece_spot)

    move_ending =  move_index + board.get(piece_spot)+1
    for index in range(move_index +1, move_ending):
        box = board_spots[index%14]
        board[box] += 1
        board[piece_spot] -= 1


    if board["A1"] == 0 and board["A2"] == 0 and board["A3"] == 0 and board["A4"] == 0 and board["A5"] == 0 and board["A6"] == 0:
        game_not_over = False
        board["B_main"] += board.get("B1") + board.get("B2") + board.get("B3") + board.get("B4") + board.get("B5") + board.get("B6")
        board["B1"] = 0
        board["B2"] = 0
        board["B3"] = 0
        board["B4"] = 0
        board["B5"] = 0
        board["B6"] = 0

    if board["B1"] == 0 and board["B2"] == 0 and board["B3"] == 0 and board["B4"] == 0 and board["B5"] == 0 and board["B6"] == 0:
        game_not_over = False
        board["A_main"] += board.get("A1") + board.get("A2") + board.get("A3") + board.get("A4") + board.get("A5") + board.get("A6")
        board["A1"] = 0
        board["A2"] = 0
        board["A3"] = 0
        board["A4"] = 0
        board["A5"] = 0
        board["A6"] = 0
    ending_board_key = box
    return ending_board_key

def is_game_over():
    game_not_over = True
    if board["A1"] == 0 and board["A2"] == 0 and board["A3"] == 0 and board["A4"] == 0 and board["A5"] == 0 and board[
        "A6"] == 0:
        game_not_over = False
        board["B_main"] += board.get("B1") + board.get("B2") + board.get("B3") + board.get("B4") + board.get(
            "B5") + board.get("B6")
        board["B1"] = 0
        board["B2"] = 0
        board["B3"] = 0
        board["B4"] = 0
        board["B5"] = 0
        board["B6"] = 0

    if board["B1"] == 0 and board["B2"] == 0 and board["B3"] == 0 and board["B4"] == 0 and board["B5"] == 0 and board[
        "B6"] == 0:
        game_not_over = False
        board["A_main"] += board.get("A1") + board.get("A2") + board.get("A3") + board.get("A4") + board.get(
            "A5") + board.get("A6")
        board["A1"] = 0
        board["A2"] = 0
        board["A3"] = 0
        board["A4"] = 0
        board["A5"] = 0
        board["A6"] = 0
    return game_not_over




def end_game():
    if board['A_main'] > board['B_main']:
        print("A is the winner!!")
    else:
        print("B is the winner!!")

def pull_across(ending_board_key):
    if board.get(ending_board_key) == 1:
        if ending_board_key == 'A1':
            board['A_main'] += board['A1']
            board['A_main'] += board['B6']
            board['A1'] = 0
            board['B6'] = 0
        elif ending_board_key == 'A2':
            board['A_main'] += board['A2']
            board['A_main'] += board['B5']
            board['A2'] = 0
            board['B5'] = 0
        elif ending_board_key == 'A3':
            board['A_main'] += board['A']
            board['A_main'] += board['B4']
            board['A3'] = 0
            board['B4'] = 0
        elif ending_board_key == 'A4':
            board['A_main'] += board['A4']
            board['A_main'] += board['B3']
            board['A4'] = 0
            board['B3'] = 0
        elif ending_board_key== 'A5':
            board['A_main'] += board['A5']
            board['A_main'] += board['B2']
            board['A5'] = 0
            board['B2'] = 0
        elif ending_board_key == 'A6':
            board['A_main'] += board['A6']
            board['A_main'] += board['B1']
            board['A6'] = 0
            board['B1'] = 0
        elif ending_board_key == 'B2':
            board['B_main'] += board['B2']
            board['B_main'] += board['A5']
            board['B2'] = 0
            board['A5'] = 0
        elif ending_board_key == 'B3':
            board['B_main'] += board['B3']
            board['B_main'] += board['A4']
            board['B3'] = 0
            board['A4'] = 0
        elif ending_board_key == 'B4':
            board['B_main'] += board['B4']
            board['B_main'] += board['A3']
            board['B4'] = 0
            board['A3'] = 0
        elif ending_board_key == 'B5':
            board['B_main'] += board['B5']
            board['B_main'] += board['A2']
            board['B5'] = 0
            board['A2'] = 0
        elif ending_board_key == 'B6':
            board['B_main'] += board['B6']
            board['B_main'] += board['A1']
            board['B6'] = 0
            board['A1'] = 0



def print_board():
    numberRow = "|    | {:2d} | {:2d} | {:2d} | {:2d} | {:2d} | {:2d} |    |"
    rowA = numberRow.format(board.get("A1"), board.get("A2"), board.get("A3"), board.get("A4"), board.get("A5"),board.get("A6"))
    rowB = numberRow.format(board.get("B6"), board.get("B5"), board.get("B4"), board.get("B3"), board.get("B2"),board.get("B1"))

    print("_________________________________________")
    print("|    | B6 | B5 | B4 | B3 | B2 | B1 |    |")
    print("|    |    |    |    |    |    |    |    |")
    print(rowB)
    print("|    | ----------------------------|    |")
    print("|    | A1 | A2 | A3 | A4 | A5 | A6 |    |")
    print("|    |    |    |    |    |    |    |    |")
    print(rowA)
    print("|____|____|____|____|____|____|____|____|")
