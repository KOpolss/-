#1) Введите число. Если это число делиться на 1000 без остатка, 
# то выведите на экран "millennium" 
a = int(input("Введите число: "))
if a % 1000 == 0:
    print("millennium")
else:
    print ("mistake")