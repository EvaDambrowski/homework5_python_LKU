#Напишите функцию, которая принимает одно число и
#проверяет, является ли оно простым
#Напоминание: Простое число - это число, которое
#имеет 2 делителя: 1 и n(само число)

from math import sqrt
 
def Prime(number,itr):  
  if itr == 1:   
    return True
  if number % itr == 0:  
    return False
  if Prime(number,itr-1) == False:   
    return False
     
  return True
  
num = int(input('Введите число: '))
 
itr = int(sqrt(num)+1)
 
print(Prime(num,itr))