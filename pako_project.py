# количество коробок
xs = 10
s = 5
m = 3
l = 1

while xs > 0 or s > 0 or m > 0 or l > 0:

    print(f"\nВ наличии: xs={xs}, s={s}, m={m}, l={l}")
    select_box = input("Выберите размер коробки (xs, s, m, l): ").lower()

    if select_box == "xs":
        if xs > 0:
            xs -= 1
            print(f"Вы выбрали XS. Осталось: {xs}")
        else:
            print("XS закончились!")

    elif select_box == "s":
        if s > 0:
            s -= 1
            print(f"Вы выбрали S. Осталось: {s}")
        else:
            print("S закончились!")

    elif select_box == "m":
        if m > 0:
            m -= 1
            print(f"Вы выбрали M. Осталось: {m}")
        else:
            print("M закончились!")

    elif select_box == "l":
        if l > 0:
            l -= 1
            print(f"Вы выбрали L. Осталось: {l}")
        else:
            print("L закончились!")

    else:
        print("Ошибка! Введите один из размеров: xs, s, m, l.")

print("\nСвободных коробок НЕТ. Все коробки закончились.")
