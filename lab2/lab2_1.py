import random

myNumber = random.randint(0, 10)
userNumber = int(input("\n ������� ���� �����: "))

while not(userNumber <= myNumber):
    userNumber = int(input(" ���� ����� ��������� ������ ��� ����� ���������! ��������� �������: "))
