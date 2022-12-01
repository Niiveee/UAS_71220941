def suhu():
    celcius = float(input("masukan skala celcius: "))
    reamur = 4/5 * celcius
    fahrenheit = 9/5 * celcius + 32
    kelvin = celcius + 273
    print("suhu reamur: ", reamur)
    print("suhu fahrenheit: ", fahrenheit)
    print("suhu kelvin: ", kelvin)

suhu()