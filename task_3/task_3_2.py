#2) В семье N свадьба. Они решили выбрать заведение, где будут
#  праздновать в зависимости от количества людей, которое прибудет 
# к утру.  Если их будет больше 50 - закажут ресторан, если от 20 до 50
#  -то кафе, а если меньше 20 то отпраздную дома. Вывести "ресторан",
#  "кафе", "дом" в зависимости от количества гостей 
# (прочитать переменн с консоли) 
num_1 = int(input("введите число гостей: "))
#вы неуказали включая или нет 
if num_1 > 50: 
    print("пойдут в ресторан")
elif num_1 >= 20:
    print("пойдут в кафе")
elif num_1 < 20:
    print("пойдут домой")
        

    