N = int(input())
room = []
for _ in range(N):
    room.append(int(input()))

ans = []

for i in range(N):
    move = 1
    move_list = []

    for j in range(i, N + i - 1):
        next = room[(j + 1) % N]
        move_list.append(next * move)
        move += 1

    ans.append(sum(move_list))

print(min(ans))


