n = int(input("Введите число от 3 до 20: "))
num = []
if n >= 3 and n <= 20:
    for i in range(1, n):
        for j in range(2, n):
            sum = i + j
            if n % sum == 0 and i != j:
                num.append(str(i)+str(j))
                #print(num)
else:
    print("Неверно! Введите число от 3 до 20: ")
number = ''.join(num)
print(number)
