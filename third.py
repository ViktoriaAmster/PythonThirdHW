# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

listOfFloat = [3.23, 8.04, 11.001, 4.46, 3.34, 0.04] #0.459

def maxMinusMinFloat (list_):
    min_ = list_[0]%1
    max_ = list_[0]%1

    for i in list_:
        if i%1 > max_:
            max_ = i%1
        elif (i%1 < min_):
            min_ = i%1
    print(f'--> {round(max_ - min_, 3)}')

maxMinusMinFloat(listOfFloat)