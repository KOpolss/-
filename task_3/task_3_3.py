#3) Ввести строку. Если длина строки больше 10 символов, то создать
#  новую строку с 3 восклицательными знаками в конце  ('!!!')
#  и вывести на экран. Если меньше 10, то вывести на экран второй 
# символ строки 
a = [1,11,2,3,32,65]
if len(a) >= 10:
    print((a," !!!"))
else:
    print(a[-2])


