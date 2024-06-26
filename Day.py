day_number = int(input("Enter the choice: "))
days ={
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"    
}
day = days.get(day_number,"invalid entry")
print(day)
