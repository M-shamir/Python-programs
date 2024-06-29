a = input("enter numbers")
for i in a:
    a = []
sorted_list = sorted(a,reverse=True)
second_largest = sorted_list[1]
print(second_largest)