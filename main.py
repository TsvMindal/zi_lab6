import matplotlib.pyplot as plt

# Определяем параметры кривой
a = 0
b = 7
p = 17

# Генерируем точки на кривой
x_range = range(p)
points = [(x, y) for x in x_range for y in x_range if (y * y) % p == (x * x * x + a * x + b) % p]

# Создаем пустой список для хранения результатов операций
results = []

# Создаем пустой список для хранения точек, полученных сложением
sum_points = []

# Визуализируем точки на кривой
plt.figure(figsize=(8, 8))

# Визуализируем точки на кривой черным цветом и добавляем метку в легенду
plt.scatter(*zip(*points), color='brown', s=10, label='Точки кривой')

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.xlim(-1, 20)
plt.ylim(-1, 20)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Точки на кривой")


# Определяем функцию для сложения двух точек на кривой
def plus_points(P, Q, a, p):
    if P == Q:
        slope = (3 * P[0] ** 2 + a) * pow(2 * P[1], p - 2, p)
    else:
        slope = ((Q[1] - P[1]) * pow(Q[0] - P[0], p - 2, p)) % p
    x = (slope ** 2 - P[0] - Q[0]) % p
    y = (slope * (P[0] - x) - P[1]) % p
    return (x, y)


# Определяем функцию для удвоения точки на кривой
def double_point(P, a, p):
    slope = (3 * P[0] ** 2 + a) * pow(2 * P[1], p - 2, p)
    x = (slope ** 2 - 2 * P[0]) % p
    y = (slope * (P[0] - x) - P[1]) % p
    return (x, y)


# Запрашиваем у пользователя выбор операции
while True:
    print("\nТочки на эллиптической кривой:\n", points)
    print("Выберите операцию:")
    print("1. Сложение точек на кривой")
    print("2. Удвоение точки на кривой")
    print("3. Сохранить график и выйти")

    choice = input("Введите номер операции (1/2/3): ")

    if choice == '1':
        # Выполняем сложение точек
        P_x = int(input("Введите x координату первой точки: "))
        P_y = int(input("Введите y координату первой точки: "))
        Q_x = int(input("Введите x координату второй точки: "))
        Q_y = int(input("Введите y координату второй точки: "))

        P = (P_x, P_y)
        Q = (Q_x, Q_y)

        R = plus_points(P, Q, a, p)
        print(f"Результат сложения точек {P} и {Q} равен {R}")

        # Добавляем результат в список результатов
        results.append(R)

        # Добавляем точку в список точек, полученных сложением
        sum_points.append(R)

        # Визуализируем точку фиолетовым цветом
        plt.scatter(*zip(*[R]), color='purple', s=25, label='Сумма точек')

    elif choice == '2':
        # Выполняем удвоение точки
        P_x = int(input("Введите x координату точки: "))
        P_y = int(input("Введите y координату точки: "))

        P = (P_x, P_y)

        Q = double_point(P, a, p)
        print(f"Удвоение точки {P} даёт точку {Q}")

        # Добавляем результат в список результатов
        results.append(Q)

        # Добавляем точку в список точек, полученных удвоением
        sum_points.append(Q)

        # Визуализируем точку розовым цветом
        plt.scatter(*zip(*[Q]), color='pink', s=25, label='Удвоение точки')

    elif choice == '3':
        # Сохраняем текущий график с выделенными точками и выходим из программы
        plt.legend(loc='upper right')
        plt.savefig("current_plot.png")
        print("Текущий график с выделенными точками сохранен в файл 'current_plot.png'.")
        break

    else:
        print("Некорректный выбор операции. Пожалуйста, выберите 1, 2 или 3.")

plt.show()
