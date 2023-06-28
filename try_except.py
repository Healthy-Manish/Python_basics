try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invaid input")
# if i run my code now then it will not give a value error as we have handled it 
try:
    value = 10/0
# except ZeroDivisionError:
#     print("Divided by zero")
except ZeroDivisionError as err:
    print(err)
    