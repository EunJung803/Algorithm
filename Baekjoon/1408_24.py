## input
# 13:52:30
# 14:00:00

## output
# 00:07:30

curr_hour, curr_min, curr_sec = map(int, input().split(':'))
start_hour, start_min, start_sec = map(int, input().split(':'))

current_time = (curr_hour * 60 * 60) + (curr_min * 60) + curr_sec
finish = (start_hour * 60 * 60) + (start_min * 60) + start_sec

if(current_time > finish):
    finish += (24 * 60 * 60)

ans = finish - current_time

ans_hour = ans // 3600
ans_min = (ans % 3600) // 60
ans_sec = (ans % 3600) % 60

if(ans_hour < 10):
    ans_hour = '0' + str(ans_hour)
if(ans_min < 10):
    ans_min = '0' + str(ans_min)
if(ans_sec < 10):
    ans_sec = '0' + str(ans_sec)

print(str(ans_hour)+':'+str(ans_min)+':'+str(ans_sec))

# print("%.2d:" %(ans//3600), end = '')
# result = ans % 3600
# print("%.2d:" %(result//60), end = '')
# print("%.2d" %(result%60))

# if(int(start_time[2]) < int(curr_time[2])):
#     if(int(start_time[0]) == int(curr_time[0])):
#         start_time[0] = int(start_time[0]) + 24
#     if(int(start_time[1]) <= int(curr_time[1])):
#         start_time[0] = int(start_time[0]) - 1
#     if(start_time[1] == "00"):
#         start_time[1] = 60
#     start_time[1] -= 1
#
# if(start_time[2] == "00"):
#     start_time[2] = 60
#
# ans_sec = int(start_time[2]) - int(curr_time[2])
# ans_min = int(start_time[1]) - int(curr_time[1])
# ans_hour = abs(int(start_time[0]) - int(curr_time[0]))
#
# if(ans_hour < 10):
#     ans_hour = '0' + str(ans_hour)
# if(ans_min < 10):
#     ans_min = '0' + str(ans_min)
# if(ans_sec < 10):
#     ans_sec = '0' + str(ans_sec)
#
# print(str(ans_hour)+':'+str(ans_min)+':'+str(ans_sec))
