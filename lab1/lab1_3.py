count = int(input("\n ”кажите количество элементов в списке: "))

mas = []
sum = 0
for i in range(count):
    mas.append(int(input()))
    if(mas[i] > 10):
        sum += mas[i]

print("\n —умма всех чисел, больше 10: ")
print(sum)
