import math

print(" ������� �������� a:")
a = float(input())
print(" ������� �������� b:")
b = float(input())
print(" ������� �������� c:")
c = float(input())
print(" ������� �������� k:")
k = float(input())

if(b == 0 or a == 0):
    print("\n ��� ���������� ���������� ������� �� ����!")
else:
    temp = (a+b+c*((k-a)/math.pow(b, 3)))

    if(temp == 0):
        print("\n ��� ���������� ���������� ������� �� ����!")
    else:
        result = (math.pow(a, 2)/math.pow(b, 2) + math.pow(c,2)*math.pow(a, 2))/temp + c + (k/b - k/a)*c

        if(result < 0):
            result *= -1

        print("\n ��������� ����������: ")
        print(result)
