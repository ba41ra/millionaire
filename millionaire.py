answer_one = int(input("""Вот твой первый вопрос:
Какой футболист выйграл золотой мяч 8 раз?
1. Криштьяну Роналду
2. Неймар Джуниор
3. Лионель Месси
4. Диего Марадона"""))
if answer_one == 3:
    print("Yes")
    answer_two = int(input("""Второй вопрос:
Какой футбольный клуб называют "сливочные"?
1. Барселона
2. Реал Мадрид
3. Манчестер Сити
4. Реал Сосьедат"""))
    if answer_two == 2:
        print("Yes")
        answer_three = int(input("""Третий вопрос:
Какой футбольный тренер выйграл лигу Чемпионов 2 раза подряд?
1. Хосеп Гвардиола
2. Юрген Клопп
3. Алекс Фергюсон
4. Зинедин Зидан"""))
        if answer_three == 4:
            print("Yes")
            answer_four = int(input("""Четвертый вопрос:
Какая команда выиграла Чемпионат мира по футболу 2022 года?
1. Аргентина
2. Франция
3. Бразилия
4. Хорватия"""))
            if answer_four == 1:
                print("Yes")
                answer_five = int(input("""Пятый вопрос:
Сколько длится футбольный матч?
1. 60 минут
2. 100 минут
3. 90 минут
4. 50 минут"""))
                if answer_five == 3:
                    print("Yes")
                    answer_six = int(input("""Шестой вопрос:
Красная карточка в футболе — это знак?
1. удаления игрока с поля   
2. предупреждения игрока
3. выражения благодарности
4. окончания матча"""))
                    if answer_six == 1:
                        print("Yes")
                        answer_seven = int(input("""Седьмой вопрос:
Сколько времени длится перерыв между первым и вторым таймом в футбольном матче?
1. 40 минут
2. 15 минут
3. 5 минут
4. 2 минуты"""))
                        if answer_seven == 2:
                            print("Yes")
                            answer_eight = int(input("""Восьмой вопрос:
Какой год считается датой рождения футбола?
1. 1812 год   
2. 1932 год
3. 1990 год
4. 1863 год"""))
                            if answer_eight == 4:
                                print("Yes")
                                answer_nine = int(input("""Девятый вопрос:
Организация, управляющая профессиональным футболом на мировом уровне, называется...
1. НБА
2. ФИФА   
3. НХЛ
4. МАГАТЭ"""))
                                if answer_nine == 2:
                                    print("Yes")
                                    answer_ten = int(input("""Последний вопрос:
Что означает предьявленная футбольным арбитром жёлтая карточка?
1. замечание
2. удаление
3. предупреждение
4. заменв"""))
                                    if answer_ten == 3:
                                        print("Вы победили, выигрыш составил 1.000к")
                                    else:
                                        print("Вы проиграли, Ваш выигрыш составил 700к")
                                else:
                                    print("Вы проиграли, Ваш выигрыш составил 700к")
                            else:
                                print("Вы проиграли, Ваш выигрыш составил 700к")
                        else:
                            print("Вы проиграли, Ваш выигрыш составил 300к")
                    else:
                        print("Вы проиграли, Ваш выигрыш составил 300к")
                else:
                     print("Вы проиграли, Ваш выигрыш составил 300к")
            else:
                print("Вы проиграли, Ваш выигрыш составил 300к")
        else:
             print("вы проиграли и ничего не выиграли")
    else:
         print("вы проиграли и ничего не выиграли")
else:
    print("вы проиграли и ничего не выиграли")
