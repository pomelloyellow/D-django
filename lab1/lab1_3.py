count = int(input("\n ������� ���������� ��������� � ������: "))

mas = []
sum = 0
for i in range(count):
    mas.append(int(input()))
    if(mas[i] > 10):
        sum += mas[i]

print("\n ����� ���� �����, ������ 10: ")
print(sum)
