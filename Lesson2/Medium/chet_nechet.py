# написать программу, которая будет выводить нечетные числа из списка 
# и  остановится, если встретит число 139.
a = [3, 5, 6, 3, 6, -12, 3, 78, 2333, 12, 5, -23, 17, 123, 139, 754, 5467, 12, -4, 7]

for i in a:
    if i == 139:
        break
    if i % 2 != 0:
        print(i)
