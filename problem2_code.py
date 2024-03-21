

def main():
    # Example usage:
    game_state = [
        [0, 2, 2],
        [0, 2, 0],
        [2, 2, 0]
    ]

    try:
        determine_board_state(game_state)
    except Exception as e:
        print(e)


def determine_board_state(input_list):
    # Check if input_list is of the correct type and shape
    if not isinstance(input_list, list) or len(input_list) != 3 or not all(isinstance(row, list) and len(row) == 3 for row in input_list):
        raise Exception("Input must be a list containing 3 inner lists of length 3")

    # Check if the values in the inner lists are integers
    if not all(isinstance(cell, int) for row in input_list for cell in row):
        raise Exception("Values in the input list must be integers")

    # Check rows, columns, and diagonals for a win condition
    for row in input_list:
        if row[0] == row[1] == row[2] != 0:
            if row[0] == 1:
                print("Player 1 wins")
            else:
                print("Player 2 wins")
            return True

    for col in range(3):
        if input_list[0][col] == input_list[1][col] == input_list[2][col] != 0:
            if input_list[0][col] == 1:
                print("Player 1 wins")
            else:
                print("Player 2 wins")
            return True

    if input_list[0][0] == input_list[1][1] == input_list[2][2] != 0:
        if input_list[0][0] == 1:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        return True

    if input_list[0][2] == input_list[1][1] == input_list[2][0] != 0:
        if input_list[0][2] == 1:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        return True

    print("No winner")
    return False


if __name__ == "__main__":
    main()
