print("������� 2")
#��� ����� ������ ������� �������� ������ ������
n = int(input("���������� ��������� ������ = "))
i = n
result = ""
arr = []
while i > 0:   
 i=i-1 
 a = input("������� ��������� ������� ������: ")
 try:
     a = int(a)
     #���� ������������ ������ ���-�� ����� �����,
     #��� ������ ������ ����� ����������� ������
 except ValueError:
         continue
 #������������ ������ �����
 arr.append(a)
 if a%2 == 0:
     #������������ ������ ������ �����
     result = result + str(a) + " "
print("�����: ",arr)
print("������: ",result)