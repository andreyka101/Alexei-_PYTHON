import json

answer = 0
calculator_arr = []
with open("calculator.json") as file:
    calculator_arr = json.load(file)
print("Добро пожаловать в калькулятор!")
text = input("Введите start для начала работы калькулятора: ")
while ( text == "start"):
    number = int(input("Введите первое число: "))
    number_two = int(input("Введите второе число: "))
    action = input ("Действие: ")
    if action == "*":
        answer = number * number_two
        print ("Произведение чисел = ", answer)
    elif action == "/":
        answer = number / number_two
        print ("Частное чисел = ", answer)
    elif action == "-":
        answer = number - number_two
        print ("Разность чисел = ", answer)
    elif action == "+":
        answer = number + number_two
        print ("Сумма чисел = ", answer)
    with open("calculator.json" , "w") as file:
        calculator_arr.append(f"{number} {action} {number_two} = {answer}") 
        json.dump(calculator_arr , file) 
    text = input("Введите start для начала работы калькулятора: ")
