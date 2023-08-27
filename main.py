myname = input("whats your name  ") 

myage = input("whats your age  ")
print(f"my name is {myname} and i am {myage} years old")

first_number = int(input("first_number "))
second_number = int(input("second_number "))
operation = input("enter an operation")
if operation == "+":
    print(first_number+second_number)
elif operation == "-":
    print(first_number-second_number)
elif operation == "*":
    print(first_number*second_number)
elif operation == "/":
    print(first_number/second_number)
else:
    print("no operation is not valid")

bus_capasity=30
inside_bus = int(input('how many people are in the bus'))
outside_bus = int(input("how many people are still outside the bus"))
empty_bus = bus_capasity - inside_bus 

if empty_seats>=outside_bus:
    print(f"there ara {empty_seats}")
else:
    print(f"there are no{empty_seats}")
