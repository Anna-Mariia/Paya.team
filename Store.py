a = int(input('How many items will you buy?: '))
if a < 10:
    b = a * 12
    print("You will need to pay:",b,"dollars")
elif a >= 10 and a <= 99:
    b = a * 10
    print("You will need to pay:",b,"dollars")
elif a >= 100:
    b = a * 7
    print("You will need to pay:",b,"dollars")
    
