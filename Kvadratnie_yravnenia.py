
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
disc = b**2 - 4*a*c

def find_quadratic_equation_roots(a, b, c, disc):

 if (disc > 0):

  x1 = (-b + disc**0.5)/(2*a)
  x2 = (-b - disc**0.5)/(2*a)
  return x1, x2

 elif (disc == 0):

   return ("x = ", -b/(2*a))

 else:
     print("Корней нет")

print(find_quadratic_equation_roots(a, b, c, disc))

if __name__ == "main":
    a,b,c = map(int, input("Type a, b, c separate with spaces").split())







