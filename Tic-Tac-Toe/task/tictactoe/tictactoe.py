cells = []
letters_list = ['X', 'O', '_']

while True:
    user_input = input('Enter cells: ')
    if len(user_input) == 9:
        for el in user_input:
            if el in letters_list:
                cells.append(el)
                continue
            else:
                print('Value error')
                break
        break
    else:
        print('Value error')
        break

#moves = input('Enter cells: ')


print("---------")
print("|", cells[0], cells[1], cells[2], "|")
print("|", cells[3], cells[4], cells[5], "|")
print("|", cells[6], cells[7], cells[8], "|")
print("---------")

row_0 = [cells[0], cells[1], cells[2]]
row_1 = [cells[3], cells[4], cells[5]]
row_2 = [cells[6], cells[7], cells[8]]

col_0 = [cells[0], cells[3], cells[6]]
col_1 = [cells[1], cells[4], cells[7]]
col_2 = [cells[2], cells[5], cells[8]]

dia_0 = [cells[0], cells[4], cells[8]]
dia_1 = [cells[2], cells[4], cells[6]]

combinations = [row_0, row_1, row_2, col_0, col_1, col_2, dia_0, dia_1]

win_count_x = 0
win_count_o = 0
blanks_count = 0
x_count = 0
o_count = 0

for el in cells:
    if el == 'X':
        x_count += 1
    elif el == 'O':
        o_count += 1
    elif el == '_' or el == ' ':
        blanks_count += 1

for combination in combinations:
    if combination[0] == combination[1] == combination[2] == "X":
        win_count_x += 1
        print('X wins')
    elif combination[0] == combination[1] == combination[2] == "O":
        win_count_o += 1
        print('O wins')
    else:
        continue

if ((x_count - o_count) > 1) or ((o_count - x_count) > 1) or (win_count_x == 1 and win_count_o == 1):
    print('Impossible')
elif (win_count_x == 0 and win_count_o == 0) and (blanks_count >= 1 and x_count >= 3 and o_count >= 3):
    print('Game not finished')
elif (win_count_x == win_count_o == 0):
    print('Draw')


# elif (cells[0] in letters_list) and (win_count_x == 1 and win_count_o == 0):
#     print('X wins')
# elif (cells[0] in letters_list) and (win_count_o == 1 and win_count_x == 0):
#     print('O wins')

# print('---------')
# print('| ' + ' '.join(user_list[:3]), end=' |\n')
# print('| ' + ' '.join(user_list[3:6]), end=' |\n')
# print('| ' + ' '.join(user_list[6:]), end=' |\n')
# print('---------')
