print("Ты барашек которой живет около леса")
print("Попробуй выжить)")
from random import randint
import random


class rassa:
    type = ['Медведь', 'Лис', 'Волк']
    evil = random.choice(type)


ev = rassa()


class lamb:
    hp = 100  # здоровье
    d = 10  # размер домика
    w = 30  # вес
    r = 20  # уважение


p = lamb()


class evil:
    hp = randint(30, 130)
    damage = randint(5, 10)


e = evil()


def menu(p):
    while True:
        print(" нажми, |1| для того чтобы пойти в бой")
        print(" нажми, |2| для того чтобы пойти покушать")
        print(" нажми, |3| для того чтобы пойти улучшить домик")
        print(" нажми, |4| для просмотра своих характеристик")
        try:
            n = int(input("Введите число: "))
            if n == 1:
                menu_fight(p)
            if n == 4:
                menu_stats(p)
            if n == 2:
                manu_eat(p)
            if n == 3:
                menu_bild(p)
            else:
                print("Эх, чем бы сегодня заняться? Боже насколько скучна моя жизнь...")

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")


def menu_stats(p):
    print(" ")
    print("Статистика игрока")
    print("*********************************************************")
    print(f"Здоровье {p.hp}")
    print(f"Репутация {p.r}")
    print(f"Вес {p.w}")
    print(f"Домик улучшен на {p.d}")
    input("Нажмите Enter для продолжения.")


def manu_eat(p):
    print(" ")
    print("Выбери какую травку ты хочешь покушать")
    print("*********************************************************")
    print(" нажми, |1| покушать жухлой травки")
    print(" нажми, |2| покушать зеленой травки")
    n = int(input("Введите число: "))
    if n == 1:
        p.hp += 10
        p.w += 15
        print(f"Ты покушал и увеличил свое здоровье {p.hp} и увеличили вес {p.w} ")

        print("*********************************************************")

    if n == 2 and p.r >= 30:
        p.hp += 30
        p.w += 30
        print(f"Ты покушал и увеличил свое здоровье {p.hp} и увеличили вес {p.w} ")
    if n == 2 and p.r < 30:
        print("Увы, нехватает уважения")
        print(f"Ваши хп {p.hp}")
        print("*********************************************************")
    input("Нажмите Enter для продолжения.")


def menu_bild(p):
    print(" ")
    print("*Улучшаем домик*")
    print("*********************************************************")
    print("нажми, |1| улучшить домик интенсивно")
    print("нажми, |2| улучшить домик лениво")
    n = int(input())
    if n != 1:
        p.hp -= 30
        p.d += 5
    if n != 2:
        p.hp -= 10
        p.d += 2
    else:
        print("Эх, работать не хочется...")

    input("Нажмите Enter для продолжения.")


def menu_fight(p):
    print(f"Вы hp: {p.hp} ")
    print(f"{ev.evil} hp: {e.hp} damage: {e.damage}")
    print("*********************************************************")
    print("нажми, |1| чтобы ударить")
    print("нажми, |2|  чтобы немного подлечится")
    n = int(input())
    if n == 1:
        while True:

            if p.hp > 0:
                if e.hp > 0:
                    # Здоровье врага отнимает от вашего дамага.
                    e.hp -= randint(15, 35)
                    print(f"Вы ударили противника, у него осталось {e.hp} hp")
                    # Здоровье игрока отнимает от дамага врага.
                    p.hp -= e.damage
                    print(f"Противник ударил вас, у вас осталось {p.hp} hp")

                    print("*********************")
                if e.hp < 0:
                    print("Вы победили")
                    p.r += 35
                    menu(p)
    if n == 2:
        p.hp += randint(0, 5)
        print(f"Ваше здоровье {p.hp}")
    if n > 3:
        print("Противник внимательно изучает вас, его лицо искровляется удивлением от ваших нелепых попыток "
              "нажать на кнопку")


input("Нажмите Enter для продолжения.")

menu(p)
