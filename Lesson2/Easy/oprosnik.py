# написать программу, которая запрашивает у пользователя:
#         его имя(например, "What is your name?").
#         возраст          ("How old are you?")
#         место жительсва  ("Where are you live?")
# после программа выводит три строки:
#         "Your name is {имя}"
#         "Your age is {возраст}"
#         "You live in {место жительства}"
def home3():
    name = input("What is your name?")
    age = input("How old are you?")
    live = input("Where are you live?")
    return name, age, live

def home33():
    name, age, live = home3()

    print(f"This is your name: {name}")
    print(f"This is your age: {age}")
    print(f"You live in {live}")
    

while True:
    home33()
    break
