N = input()

length = len(N)
front = list(map(int, N[:length//2]))
back = list(map(int, N[length//2:]))

if(sum(front) == sum(back)):
    print("LUCKY")
else:
    print("READY")