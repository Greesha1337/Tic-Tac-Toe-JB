user_input = [int(n) for n in input()]
print([sum(user_input[0:i+1]) for i in range(len(user_input))])


