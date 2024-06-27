
num = 7

start_num = num


for i in range(4,0, -1):
   
    for j in range(start_num, start_num + i):
        print(j, end=" ")
    print()
   
    start_num -= (i - 1)
