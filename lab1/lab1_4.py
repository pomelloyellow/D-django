count = int(input("\n ������� ���������� ��������� � ������: "))

mas = []

for i in range(count):
    mas.append(int(input()))

maxElement = mas[0]

for i in range(count):
    if mas[i] > maxElement:
        maxElement = mas[i]

print("\n ������������ ������� �������: ")
print(maxElement)
