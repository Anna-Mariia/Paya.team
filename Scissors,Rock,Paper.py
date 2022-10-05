from random import randint
choice = ["Камінь","Ножниці","Папір"]
print("Давайте пограємо!")
for i in range (3):
    print (i, choice[i])

game = "y"
while game!="n":
    comp = randint (0,2)
    x = int(input ("Щo обираєте (0-1-2)->"))
    your_choice = choice[x]
    comp_choice = choice[comp]
    print ("Kомп'ютер вибрав",comp_choice)
    print ("Baш вибiр",your_choice)
    #Якщо комп'ютер вибрав КАМІНЬ
    if comp == 0:
        if x == 0:
            print("НІЧИЯ" )
        if x == 1:
            print ("Bиграв компютер")
        if x == 2:
            print("Ви виграли")
    #Якщо комп'ютер вибрав НОЖНИЦІ
    if comp == 1:
        if x == 1:
            print("НІЧИЯ")
        if x == 2:
            print ("Bиграв комп'ютер")
        if x == 0:
            print("Ви виграли")
    #Якщо комп'ютер вибрав ПАПІР
    if comp == 2:
        if x == 2:
            print("НІЧИЯ")
        if x == 0:
            print ("Bиграв комп'ютep")
        if x == 1:
            print("Bи виграли" )
    print('Дякую за гру!')
    game = input('Бажаєте продовжити? (y/n)')
