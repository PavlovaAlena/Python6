 #Задача 2 Семинара 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N 
 # с использованием lambda.

#************************
def composition(n):
    resultList = []
    resF = lambda a, b:  a * b
    res = 1
    for i in range(1, n + 1, 1):
        res = resF(res,i)
        resultList.append(res)    
    return resultList

#************************
import os 
os.system('cls')

print("Программа принимает на вход число N и выдает набор произведений чисел от 1 до N.")
digit = int(input("Введите число: "))

lst = composition(digit)

print(f"Набор произведений чисел от 1 до {digit}: {lst}")