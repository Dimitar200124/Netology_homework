try:
    number = int(input("Введите шестизначное число: "))
    if 100000 <= number <= 999999:
        # Преобразуем число в строку для получения цифр
        number2 = str(number)
        # Сумма первых трех цифр
        first_3 = int(number2[0]) + int(number2[1]) + int(number2[2])
        # Сумма последних трех цифр
        last_3 = int(number2[3]) + int(number2[4]) + int(number2[5])
        if first_3==last_3:
          print("Ваш билет счастливый!") 
        if first_3 !=last_3:
          print("Несчастливый билет!Возможно, в другой раз вам повезёт!")
    else:
        print("Ошибка! Введите число от 100000 до 999999.")
except ValueError:
    print("Ошибка! Введите только цифры.")