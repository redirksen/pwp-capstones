import Mancala


def set_up_game():
    print("Setting up board.")
    Mancala.fill_board()
    Mancala.print_board()


def play_game():
    print("player A goes first")
    whos_turn = "A"
    game_not_over = True

    while (True):
        repeat_turn = False
        if whos_turn == "A":

            while True:
                try:
                    number1 = input("Please input the number of the bin you want to use.(A1 - A6)")

                    if number1 not in ["A1", "A2", "A3", "A4", "A5", "A6"] or (Mancala.board.get(number1) == 0):
                        raise ValueError  # this will send it to the print message and back to the input option
                    user_input = number1
                    break
                except ValueError:
                    print("Invalid input.Please input a valid amount")

        else:
            while True:
                try:
                    number1 = input("Please input the number of the bin you want to use.(B1 - B6)")
                    if number1 not in ["B1", "B2", "B3", "B4", "B5", "B6"] or (Mancala.board.get(number1) == 0):
                        raise ValueError  # this will send it to the print message and back to the input option
                    user_input = number1
                    break
                except ValueError:
                    print("Invalid input.Please input a valid amount")

        ending_board_key = Mancala.make_move(user_input)


        if (whos_turn == "A" and ending_board_key[0] == "A"):
            Mancala.pull_across(ending_board_key)

        if (whos_turn == "B" and ending_board_key[0] == "B"):
            Mancala.pull_across(ending_board_key)

        if (whos_turn == "A" and ending_board_key == "A_main"):
            repeat_turn = True
        if (whos_turn == "B" and ending_board_key == "B_main"):
            repeat_turn = True

        game_not_over = Mancala.is_game_over()
        print(Mancala.print_board())
        if (not game_not_over):
            Mancala.end_game()
            break

    # End Game
        if repeat_turn == True:
            continue
        else:
            if whos_turn == "A":
                whos_turn = "B"
            else:
                whos_turn = "A"



if __name__ == "__main__":
    set_up_game()


    play_game()

