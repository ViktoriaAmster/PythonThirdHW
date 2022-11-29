# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

listOfNums = [3, 8, 11, 4, 3, 0, 1, 9, 6] #[21, 48, 99, 4, 0] [18, 72, 11, 0, 9]

def multipl (list_):
    multiplList = []
    if len(list_)%2 > 0:
        for i in range(int(len(list_)/2+1)):
            multiplList.append(list_[i]*list_[-1-i])
    else:
        for i in range(int(len(list_)/2)):
            multiplList.append(list_[i]*list_[-1-i])
    print(f'--> {multiplList}')

multipl(listOfNums)