import random

myNumber = random.randint(0, 10)
userNumber = int(input("\n Введите ваше число: "))

while not(userNumber <= myNumber):
    userNumber = int(input(" Ваше число оказалось больше или равно заданному! Повторите попытку: "))
