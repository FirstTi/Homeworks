# написать функцию mounth_to_season(), которая принимает 1 аргумент - номер месяца
# и возвращает название сезона, к которому относится этот месяц. например, передаем 2,
# на выходе получаем "Зима".
mounth = 0

def mounth_to_season(mounth):
    mounth = int(input("Введите номер месяца: "))
    if 0 < mounth < 3 or mounth == 12:
        return("Сейчас зима")
    elif 2 < mounth < 6:
        return("Сейчас весна")
    elif 5 < mounth < 9:
        return("Сейчас лето")
    elif 8 < mounth < 12:
        return("Сейчас осень")
    else:
        return("Непонятно...")

print(mounth_to_season(mounth))
