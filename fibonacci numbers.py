q = int(input())
hub_1 = 1
hub_2 = 1
if q == 1:
    print(1)
else: # если коротко, то 4-6 для того что бы вывести 1, 1 вначале вывода чисел
    print(hub_1, hub_2, end=' ')
for i in range (2, q): # Так как 1, 1 мы уже вывели начинаем с 2
    x = hub_1 # Создаем подставную переменную для дальнейшего обмена чисел между хабами, в ней будет хранится предыдущее число цикла
    hub_1 = hub_2 # Присваиваем хаб 1 значение хаб 2 для того что бы в последующим сохранять последовательность
    hub_2 = hub_1 + x # В хаб два складываем хаб 1 и х для получения следующего числа
    print(hub_2, end=' ')