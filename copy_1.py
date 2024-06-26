size = int(input("enter the size"))
array1=[]
print("Enter the values of Array 1")
for i in range(size):
    element = int(input(""))
    array1.append(element)
print("Array 1:", array1)
print("Array 2 : Copy of Array 1")
array2 = array1.copy()
print(f"Array 2:{array2}+add elements")
array2.append(30)
print(f"Array 1[{array1}]")
print(f"Array 2[{array2}]")

