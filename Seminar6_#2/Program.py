#Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# с использованием List comprehension, lambda 

#************************
def fillList(n,l,r):
    import random
    resultList = [random.randint(l, r) for i in range(n)]
 
    return resultList

#************************
def listSumm(lst):

    resF = lambda a, b:  a + b
    sum = 0
    for i in range(1,len(lst),2):
        sum = resF(sum, lst[i])
    return sum

#************************
import os 
os.system('cls')

print("Программа задает список из нескольких чисел и находит сумму элементов списка, стоящих на нечётной позиции.")
listN = int(input("Введите размерность списка: "))
listL = int(input("Введите начало диапазона чисел для заполнения списка: "))
listR = int(input("Введите окончание диапазона чисел для заполнения списка: "))

lst = fillList(listN, listL, listR)
sum = listSumm(lst)

print(f"В списке {lst} сумма элементов списка, стоящих на нечётной позиции: {sum}")