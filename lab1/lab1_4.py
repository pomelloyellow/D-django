count = int(input("\n Укажите количество элементов в списке: "))

mas = []

for i in range(count):
    mas.append(int(input()))

maxElement = mas[0]

for i in range(count):
    if mas[i] > maxElement:
        maxElement = mas[i]

print("\n Максимальный элемент массива: ")
print(maxElement)
