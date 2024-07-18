pah1 = open('pah.txt') 
van1 = open('van.txt')
# Импортируем файлы в питон
pah = [int(x) for x in pah1]
van = [int(x) for x in van1]
# С помощью генератора делаем из строк числа и помещаем их в списки
p = pah[7]
v = van[7]
# Создаём переменные, в которых храняться данные о 8 - ом забрасывании бумажек
sumpa = sum(pah) - p
sumva = sum(van) - v
# Определяем сумму всех заброшенных чисел и отнимаем от суммы 8 - ое забрасывание
if sumpa > sumva:
    print(sumpa, p)
else:
    print(sumva, v)
# Сравниваем суммы и выводим ответ
