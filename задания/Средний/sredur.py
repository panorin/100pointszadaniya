f = open('sredur.txt') # Импортируем файл
a = [int(x) for x in f]
#С помощью генератора делаем из строк числа и помещаем их в список a
col = 0 #Создаём переменную в которой храним максимальное число вошедших в список чисел
chis = 0 #Создаём переменную в которую записываем число которое повторяется больше всего 
for i in range(1,21): # Цикл который будет перебирать числа (1 - 20)
    cl = a.count(i) # Переменная которая записывает количество числа i (1 - 20) в списке a
    if cl > col: # Сравниваем количесвто чисел i в списке с максимальным количеством уже проверенных чисел
        col = cl
        chis = i
print(chis, col) # Выводим число которое повторялось больше всего раз, и его количество в мешочке
    
    

    
