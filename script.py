def check_winner(array: list):
    empty = 0
    is_finished = False
    n_of_x, n_of_o = 0, 0
    n_of_winners = 0
    for i in array:
        for k in i:
            if k == "X":
                n_of_x += 1
            if k == "O":
                n_of_o += 1
            if '_' in k:
                empty += 1
    answer = ''
    for i in array:
        if all([k == "X" for k in i]) or all([k == "O" for k in i]) :
            return f"{i[0]} wins"
    for i, value in enumerate(array):
        if i + 1 < len(array) and i + 2 < len(array):
            if array[i][0] == array[i + 1][0] == array[i + 2][0] and array[i][0] != '_':
                if array[i][0] == "X" and array[i][0] == "X" and array[i][0] and "X":
                    answer = f"X wins"
                else:
                    answer = f"O wins"
                is_finished = True
                n_of_winners += 1
            elif array[i][1] == array[i + 1][1] == array[i + 2][1] and array[i][1] != '_':
                if array[i][0] == "X" and array[i + 1][1] == "X" and array[i + 2][1] and "X":
                    answer = f"X wins"
                else:
                    answer = f"O wins"
                is_finished = True
                n_of_winners += 1
            elif array[i][2] == array[i + 1][2] == array[i + 2][2] and array[i][2] != '_':
                if array[i][2] == "X" and array[i + 1][2] == "X" and array[i + 2][2] and "X":
                    answer = f"X wins"
                else:
                    answer = f"O wins"
                is_finished = True
                n_of_winners += 1
            elif array[i][0] == array[i + 1][1] == array[i + 2][2] and array[i][0] != '_':
                if array[i + 1][1] == "X":
                    answer = f"X wins"
                else:
                    answer = f"O wins"
                is_finished = True
                n_of_winners += 1
            elif array[i][2] == array[i + 1][1] == array[i + 2][0] and array[i][2] != '_':
                if array[i + 1][1] == "X":
                    answer = f"X wins"
                else:
                    answer = f"O wins"
                is_finished = True
                n_of_winners += 1
            elif empty == 0 and not is_finished:
                return "Draw"
            else:
                continue
    return answer



def check_input(cord, game_array, sign="X"):
    cord = cord.split(' ')
    if not cord[0].isdigit() or not cord[1].isdigit():
        return False, "You should enter numbers!"

    cord[0] = int(cord[0]) - 1
    cord[1] = int(cord[1]) - 1
    if int(cord[0]) > 2 or int(cord[1]) > 2:
        return False, "Coordinates should be from 1 to 3!"
    for i, value in enumerate(game_array):
        if i == int(cord[0]):
            for k, val in enumerate(value):
                if k == int(cord[1]):
                    if val == 'X' or val == 'O':
                        return False, "This cell is occupied! Choose another one!"
                    else:
                        value[k] = sign
                        return True, ""

symbols = "_________"
symbols_list = list(symbols)
game_array = []
print("---------")
for i in range(0, len(symbols_list), 3):
    game_array.append([symbols_list[i], symbols_list[i + 1], symbols_list[i + 2]])
    print("|", symbols_list[i], symbols_list[i + 1], symbols_list[i + 2], "|")
print("---------")

previous = 'O'
while True:
    coordinates = input("Enter the coordinates: ")

    if previous == 'X':
        previous = 'O'
        result, message = check_input(cord=coordinates, game_array=game_array, sign=previous)
        if message:
            previous = 'X'
    else:
        previous = 'X'
        result, message = check_input(cord=coordinates, game_array=game_array, sign=previous)
        if message:
            previous = 'O'

    if message:
        print(message)
    else:
        print("---------")
        for i, value in enumerate(game_array):
            if i + 1 < len(game_array) and i + 2 < len(game_array):
                print("| " + game_array[i][0], game_array[i][1], game_array[i][2] + " |")
                print("| " + game_array[i + 1][0], game_array[i + 1][1], game_array[i + 1][2] + " |")
                print("| " + game_array[i + 2][0], game_array[i + 2][1], game_array[i + 2][2] + " |")
        print("---------")
        result = check_winner(game_array)
        if result:
            print(result)
            break
