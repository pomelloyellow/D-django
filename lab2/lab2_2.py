count = int(input(" ������� ������ ������: "))
mas = []

print("\n ������� " + str(count) + " �����: " + "\n")

for i in range(count):
    mas.append(str(input()))

for i in range(count):
    if(len(mas[i]) >= 5 and len(mas[i]) <= 10):
        print(mas[i])
