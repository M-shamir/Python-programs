def getarray():
    size = int(input("enter the size"))
    arr=[]
    print("enter elements")
    for i in range(size):
        value = int(input(f"value({i+1}):"))
        arr.append(value)
    return arr
def displayarray(arr):
    print("values of the array are:")
    for value in arr:
        print(value,end="")
        print()
def main():
    arr = getarray()
    displayarray(arr)
if __name__ == "__main__":
    main()