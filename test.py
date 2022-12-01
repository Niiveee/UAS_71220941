def volume_limas():
    print("Masukan panjang sisi alas dan tinggi limas")
    alas = float(input("masukan panjang sisi alas limas: "))
    tinggi = float(input("masukan tinggi limas: "))
    limas = 0.34 * (alas * tinggi) * tinggi
    print("volume limas tersebut adalah: ", limas)

def volume_bola():
    print("Masukan jari jari bola")
    r = float(input("masukan jari jari bola: "))
    volume = 4 / 3 * (3.14 * r**3)
    print("volume bola adalah: ", volume)

def volume_prisma_segitiga():
    print("Masukan alas dan tinggi!")
    panjang = float(input("masukan panjang sisi alas prisma: "))
    tinggi = float(input("masukan tinggi alas prisma: "))
    lebar = float(input("masukan tinggi prisma segiempat"))
    volume = panjang * tinggi * lebar
    print("volume prisma segiempat adalah: ", volume)


def volume_prisma_segiempat():
    print("Masukan alas dan tinggi!")
    alas = float(input("masukan panjang sisi alas prisma: "))
    tinggi = float(input("masukan tinggi alas prisma: "))
    segitiga = float(input("masukan tinggi prisma segitiga"))
    volume = (1/2 * (alas * tinggi)) * segitiga
    print("volume prisma segitiga adalah: ", volume)

def volume_prisma_segilima():
    print("Masukan alas dan tinggi!")
    panjang = float(input("masukan panjang sisi alas prisma: "))
    tinggi = float(input("masukan tinggi alas prisma: "))
    segitiga = float(input("masukan tinggi prisma segilimat"))
    volume = 1 / 2 * (5 *panjang * tinggi) * segitiga
    print("volume prisma segiempat adalah: ", volume)

def volume_kerucut():
    print("luas bola ready!")
    r = float(input("masukan jari jari: "))
    luas = 4 * 3.14 * (r**2)
    print("luas bola adalah: ", luas)

while True:
    userInput = int(input("pilih rumus yang akan di pakai \n1. Limas\n2. Bola\n3. Prisma\n4. Kerucut\n\n"))
    if(userInput == 1):
        volume_limas()
    elif(userInput == 2):
        volume_bola()
    elif(userInput == 3):
        userInput = int(input("tentukan pilihan anda \n1. prisma segitiga \n2 prisma segiempat \n3 prisma segilima\n\n"))
        if(userInput == 1):
            volume_prisma_segitiga()
        elif(userInput == 2):
            volume_prisma_segiempat()
        elif(userInput == 3):
            volume_prisma_segilima()
        else:
            break
    elif(userInput ==4):
        volume_kerucut()
    else:
        break

