a = 1
count =  0
if a > 1:
    for i in range(1,a+1):
        if (a%i)==0:
            count+=1
        if count == 2:
            print("Prime")
else:
    print("Not Prime")