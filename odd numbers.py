x = int(input())
total_odd_num = 0
for i in range (x):
    y = int(input())
    if y % 2 != 0:
        total_odd_num += y
print(total_odd_num)

