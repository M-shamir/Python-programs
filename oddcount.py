a = input("enter the with spaces").split()
count = 0
a = [int(x)for x in a]
for x in a:
    if x % 2 != 0:
        count +=1
print(count)