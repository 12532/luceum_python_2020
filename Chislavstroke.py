#Функция, возварщающая числа из строки

string = input('Строка:')
a = string.split()

def stroka(a):

 c = [c for c in a if c.isdigit()]
 return c
         
 
print(stroka(a))



 
