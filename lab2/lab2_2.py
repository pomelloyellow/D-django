count = int(input(" ¬ведите размер списка: "))
mas = []

print("\n ¬ведите " + str(count) + " строк: " + "\n")

for i in range(count):
    mas.append(str(input()))

for i in range(count):
    if(len(mas[i]) >= 5 and len(mas[i]) <= 10):
        print(mas[i])
