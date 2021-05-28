def inch_v_centimeters():
    return x/2.54
def centimeters_v_inch():
    return x*2.54
def milli_v_kilometers():
    return x*1.609
def kilometers_v_milli():
    return x/1.609
def lbs_v_kilograms():
    return x/2.205
def kilograms_v_lbs():
    return x*2.205
def oz_v_grams():
    return x/28.35
def grams_v_oz():
    return x*28.35
def gallons_v_liters():
    return x*3.785
def liters_v_gallons():
    return x/3.785
def pins_v_liters():
    return x/2.113
def liters_v_pins():
    return x*2.113
choice = int(input('''
выберице что будем переводить:
1 дюймы в сантиметры
2 сантиметры в дюймы
3 мили в километры
4 километры в мили
5 фунты в килограмм
6 килограммы в фунты
7 унции в граммы
8 граммы в унции
9 галлоны в литры
10 литры в галлоны
11 пинты в литры
12 литры в пинты
введите число от одного до 12: '''))
x = int(input("введите значение: "))
while True:

    if choice == 1:
        inch_v_centimeters()
    elif choice == 2:
        centimeters_v_inch()
    elif choice == 3:
        milli_v_kilometers()
    elif choice == 4:
        kilometers_v_milli()
    elif choice == 5:
        lbs_v_kilograms()
    elif choice == 6:
        kilograms_v_lbs()
    elif choice == 7:
        oz_v_grams()
    elif choice == 8:
        grams_v_oz()
    elif choice == 9:
        gallons_v_liters()
    elif choice == 10:
        liters_v_gallons()
    elif choice == 11:
        pins_v_liters()
    elif choice == 12:
        liters_v_pins()
    elif choice >= 13:
        break