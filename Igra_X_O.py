shapka = (["  ",[0],[1],[2]])
stroka_1 = ([[0], ["-"], ["-"], ["-"]])
stroka_2 = ([[1], ["-"], ["-"], ["-"]])
stroka_3 = ([[2], ["-"], ["-"], ["-"]])

#########################################################################################
#Всего 9 комбинаций                                                                    ##
#Игрок_1 - Х (всего 5 ходов)                                                           ##
#Игрок_2 - О (Всего 4 хода)                                                            ##
#Чередовать запросы между Х и О и после ответа делать вывод картинки для удобства      ##
##############                                                                         ##
##############                                                                         ##
##  Правила игры для пользователя!                                                     ##
## Сначала вводится строка а затем столбец.                                            ##
## Ввод в запрос чисел 1 , 2 или 3.                                                    ##
## Количество ходов ограниченно 9 ходами. Выбирать нужно строго свободные яцейки.      ##
##############                                                                         ##
##############                                                                         ##
##############                                                                         ##
##############                                                                         ##
##############                                                                         ##
## Возможные улучшения !                                                               ##
## Исключить ошибки через try / except                                                 ##
## Можно сделать цикл запроса выбора другой ячейки,если игрок выбирает занятую ячейку. ##
#########################################################################################


##Функция записи хода Игрока_1
def player_1_answear(player_1_ask_col_input,player_1_ask_row_input):
    if player_1_ask_col_input == 1:
        stroka_1[player_1_ask_row_input] = "X"
    elif player_1_ask_col_input == 2:
        stroka_2[player_1_ask_row_input] = "X"
    elif player_1_ask_col_input == 3:
        stroka_3[player_1_ask_row_input] = "X"



##Функция записи хода Игрока_2
def player_2_answear(player_2_ask_col_input,player_2_ask_row_input):
    if player_2_ask_col_input == 1:
        stroka_1[player_2_ask_row_input] = "O"
    elif player_2_ask_col_input == 2:
        stroka_2[player_2_ask_row_input] = "O"
    elif player_2_ask_col_input == 3:
        stroka_3[player_2_ask_row_input] = "O"

#Счетчик ходов для Игрока_1 и Игрока_2
count_X = 0
count_O = 0

while count_X <= 5 and count_O < 4:
##Игрок_1
    player_1_ask_col_input = int(input("Игрок_1, введите номер строки чтобы поставить Х: "))
    player_1_ask_row_input = int(input("Игрок_1, номер столбца,чтобы поставить Х: "))
    player_1_answear(player_1_ask_col_input,player_1_ask_row_input)
    print(shapka)
    print(stroka_1)
    print(stroka_2)
    print(stroka_3)
    count_X += 1
##Игрок_2
    player_2_ask_col_input = int(input("Игрок_2, введите номер строки чтобы поставить O: "))
    player_2_ask_row_input = int(input("Игрок_2, номер столбца,чтобы поставить O: "))
    player_2_answear(player_2_ask_col_input,player_2_ask_row_input)
    print(shapka)
    print(stroka_1)
    print(stroka_2)
    print(stroka_3)
    count_O += 1
##   Последний ход Игрока_1
    if count_X == 4:
            player_1_ask_col_input = int(input("Игрок_1, введите номер строки чтобы поставить Х: "))
            player_1_ask_row_input = int(input("Игрок_1, номер столбца,чтобы поставить Х: "))
            player_1_answear(player_1_ask_col_input,player_1_ask_row_input)
            print(shapka)
            print(stroka_1)
            print(stroka_2)
            print(stroka_3)
            print("Победил игрок,у которого Х или О стоят в ряд или по диагонали, в ином случае - ничья")






