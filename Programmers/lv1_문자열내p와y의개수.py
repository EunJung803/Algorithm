def solution(s):
    answer = True

    num_p = 0
    num_y = 0

    for i in s:
        if (i == 'p' or i == 'P'):
            num_p += 1
        if (i == 'y' or i == 'Y'):
            num_y += 1

    if (num_p != num_y):
        return False

    return True