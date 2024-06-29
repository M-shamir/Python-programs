a = input("enter numbers enter in spaces").split()
sum = 0
a = [int(x)for x in a]
for x in a:
    if x % 2 == 0:
        sum+=x
print(sum)