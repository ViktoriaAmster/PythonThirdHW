# Напишите программу, которая будет преобразовывать десятичное число в двоичное

decimal = int(input("Введите число: "))

def decimalToBinary (dec: int):
    listOfBinary = []
    if dec != 0:
        while dec != 1:
            listOfBinary.append(str(dec%2))
            dec //= 2
        listOfBinary.append(str(dec))
        print(''.join(list(reversed(listOfBinary))))
    else:
        print(0)

decimalToBinary(decimal)