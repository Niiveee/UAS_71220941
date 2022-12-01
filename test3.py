def ascending():
    a = input("masukan bilangan pertama: ")
    b = input("masukan bilangan kedua: ")
    c = input("masukan bilangan ketiga: ")
    d = input("masukan bilangan keempat: ")
    sortir = (a,b,c,d)
    print(sorted(sortir))

def descending():
    a = input("masukan bilangan pertama: ")
    b = input("masukan bilangan kedua: ")
    c = input("masukan bilangan ketiga: ")
    d = input("masukan bilangan keempat: ")
    sortir = (a,b,c,d)
    print(sorted(sortir, reverse= True))

while True:
    userInput = int(input("tentukan pilihan anda\n\n1. ascending\n2. descending\n\nMasukan pilihan anda: "))
    if(userInput ==1):
        ascending()
    elif(userInput ==2):
        descending()
    else:
        wkkw
