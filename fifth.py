k = 8
listOfFibo = []

def fibo (num: int):
    count = 1
    if num == 0:
        return 0
    elif num in (1, 2):
        return 1
    elif num > 2:
        count = (fibo(num - 1) + fibo(num - 2))
        return count
    else:
        count = (fibo(num + 2) - fibo(num + 1))
        return count

for i in range(k+1):
    listOfFibo.append(fibo(i))

for l in range(-1,-k-1, -1):
    listOfFibo.insert(0,fibo(l))
print(listOfFibo)
