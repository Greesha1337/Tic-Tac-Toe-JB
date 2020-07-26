first = int(input())
i = 1
players = []
while i <= first:
    user_input = input()
    players.append(user_input.split())
    i += 1

winner = []
counter = 0
for player in players:
    for j in player:
        if j == 'win':
            counter += 1
            winner.append(player[0])

print(winner)
print(counter)