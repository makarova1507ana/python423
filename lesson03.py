# #----------------------разбор задач-------------------------------#
# '''
# Из трехзначного числа x вычли его последнюю цифру.
# Когда результат разделили на 10, а к частному слева приписали последнюю цифру числа x,
# то получилось число 237. Найти число x.
# Ответ будет 372? + верно
# '''
# # ---- решение ----- #
# #
# x = int(input("Введите число: "))
# if x >= 100 and x < 1000:
#     #узнаем последнюю цифру
#     x3 = x % 10
#     # 1
#     x = x - x3
#     # 2
#     x = x // 10
#     #print(x, x3)
#     # 3
#     x3 = x3 * 100
#     x = x3 + x
#     print(x)
# else:
#     print("неудовлетворяет условию задачи")


# -----------------------Условные оперторы--------------------------- #
# -------------------------------Задача-------------------------------#
'''
Пользователь вводит номер дня недели, программа должна выводить информацию о наименовании дня недели.
'''

#------------классический вариант----------#
# num_of_day = input("Введите день недели: ")
# if num_of_day == '1':
#     print('понедельник')
# elif num_of_day == '2':
#     print('вторник')
# elif num_of_day == '3':
#     print('среда')
# elif num_of_day == '4':
#     print('четвeрг')
# elif num_of_day == '5':
#     print('пятница')
# elif num_of_day == '6':
#     print('суб')
# elif num_of_day == '7':
#     print('вск')
# else:
#     print('такого дня нет')
#------------альтернативный вариант----------#

'''
используем когда нужно заменить конструкции if elif  с точным сравнением (variable == value)
match variable:
    case value:
        ваше действие
    case value2:
        ваше действие
        
    ...
    
    case _:
        ваше действие при исключетльном варианте
'''
# num_of_day = input("Введите день недели: ")
# match num_of_day:
#     case '1': # num_of_day == '1':
#         print('понедельник')
#     case '2': # num_of_day == '2':
#         print('вторник')
#     case '3': # и т.д.
#         print('среда')
#     case '4':
#         print('четвeрг')
#     case '5':
#         print('пятница')
#     case '6':
#         print('суб')
#     case '7':
#         print('вск')
#     case _: # else
#         print('такого дня нет')



# #—------------------------------- Задача —--------------------------------#
# # Напишите программу, которая запрашивает у пользователя логин и пароль
# # и проверяет их корректность (например, логин: "admin", пароль: "1234").
# # Если данные введены верно, программа должна вывести "Доступ разрешен", иначе —
# # "Неверный логин или пароль".
#
# # узнать логин
# # узнать пароль
# # сравнить с "admin"
# # ...
#
# login = input("Ведите логин ")
# password = input("Введите пароль")
# if login == 'admin' and password == '1234':
#     print('вы вошли')
# else:
#     print("Errorr")
#
# # # как  это выглядит в реальной проверки авторизации
# # if login == 'admin':
# #     # инструкция по декодированию пароля
# #     if password == '1234':
# #         print('вы вошли')
# # else:
# #     print("Errorr")



# # #—------------------------------- Задача —--------------------------------#
# # # Ввести оценку студента.
# # # Если оценка больше 90, вывести "Отлично!",
# # # если от 70 до 89 – "Хорошо", иначе – "Попробуйте еще".
# #
# # # -------тесты--------- #
# # # 100
# # # 75
# # # 60
# # # граничные
# # # 69
# # # 70
# # # 71 !!! было бы неплохо
# # # 89
# # # 90
# # # 91 !!!  было бы неплохо
# grade = int(input("Введите оценку студента: "))
# if grade >= 90:
#     print("Отлично!")
# elif grade >= 70 and grade <= 89:
#     print("Хорошо")
# else:
#     print("Попробуйте еще")


#--------------для данной задачи не самый лучший вариант--------------------#
# # # -------тесты--------- #
# # # 100 # "попробуйте еще", хотя ждали "отлично"
# # # 75
# # # 60
# # # граничные
# # # 69
# # # 70
# # # 71 !!! было бы неплохо
# # # 89
# # # 90
# # # 91 !!!  было бы неплохо
# grad = input('введите оценку студента: ')
# if grad >= '90':
#     print('отлично')
# elif '70' <= grad <= '89':
#     print('хорошо')
# else:
#     print('попробуйте еще')



#—------------------------------- Задача —--------------------------------#
# Сделать CLI (command line interface - 'интерфейс командной строки (консоли)')
# для снятия наличных.
# --- команды ---
# ввод суммы снятия  -> информировать о сняти и остатке на счету
# выбор купюр (100, 500, 1000)
# поддерждение операции снятия (!!! прописать конретнее)
# просмотр текущего баланса

balance = 1257

command = input('''
Введите номер операции (ТОЛЬКО ЧИСЛО)
1. Посмотреть баланс 
2. снять деньги
''') #выбор команды пользователя

match command:
    case '1':
        print(f'Ваш баланс: {balance}')
    case '2':
        #пока не знаем какие будут операции
        pass # заглушка - ничего не делает
    case _:
        print('Неверная команда')
