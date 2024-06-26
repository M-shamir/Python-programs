input_str = input("enter string")
input_str = input_str.replace(" ","").lower()

start = 0
end = len(input_str)-1
is_palidrome = True
while start < end:
    if input_str[start] != input_str[end]:
        is_palidrome = False
        break
    start +=1
    end -=1
if is_palidrome:
    print("palidrome")
else:
    print("not palidrome")