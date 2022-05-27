# создать произвольный список.
# добавить новый элемент типа str в конец списка
# добавить новый элемент типа int в конец списка
# добавить новый элемент типа list в конец списка
# добавить новый элемент типа tuple в конец списка
# получить элемент по индексу

lst = []

a = "some_text"
b = 4

lst.append(a)
lst.append(b)
lst.append("second_text")

tpl = (1, 4, 6)
lst.append(tpl)

print(lst)
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
