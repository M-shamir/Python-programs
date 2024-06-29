a = input("enter numbers enter in spaces").split()
a = [int(x)for x in a]
even = []
for x in a:
    if x%2 == 0 :
        even.append(x)
print(even)