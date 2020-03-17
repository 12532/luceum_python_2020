#Функция проверки на палиндромность
string = str(input("Введите сообщение: "))

def pal(string):
    
 a = string[::-1]
 if string == a:
     print("Это палиндром")
     
 else:
     print("Это не палиндром")
     
print(pal(string))
