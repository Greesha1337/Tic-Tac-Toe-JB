user_list = []

while True:
    user_input = input('Enter cells: ')
    if len(user_input) == 9:
        for el in user_input:
            if el == 'O' or el == 'X' or el == '_':
                user_list.append(el)
                continue
            else:
                print('Value error')
                break
        break
    else:
        print('Value error')
        break

print('---------')
print('| ' + ' '.join(user_list[:3]), end=' |\n')
print('| ' + ' '.join(user_list[3:6]), end=' |\n')
print('| ' + ' '.join(user_list[6:]), end=' |\n')
print('---------')

