import numpy as np

def gen (len_list=1):
    return_list = []
    for i in range(len_list):
        return_list.append(np.random.randint(1,101))
        
    return return_list

if __name__ == '__main__':
    gen()

        

number = np.random.randint(1,101)   #загадываем число от 1 до 100
total_count = 0                     #переменная для подсчета общего кол циклов подбора, 1 вариант подсчета
list_count = []                     #список, где элементы это кол за циклов за каждый проход цикла игры
value_interation = 1
#value_interation = int(input ('Сколь раз, вы бы хотели, чтобы сыграл копмьютер сам с собой:'))

for i in range (value_interation):
    count = 0                       #подсчет за сколько проходов мы подобрали число, именно в этой интерации
    while True:
        searh_number = np.random.randint(1,101) #генерация числа
        count += 1
        if searh_number == number:              #если совпадает, то прерываем цикл
            break                   
    list_count.append(count)                    #список для подсчета среднего (второй вариант)
    total_count += count                        #переменная для подсчета среднего (первый вариант)
    

mean_total = total_count/value_interation       #считаем по первому варианту, всего кол на кол раз игры
mean = np.mean(list_count)                      #считаем по втрому варианту, медиана из списка
    
#print ('Первый вариант подсчета:')
#print (f'Total_count: {total_count}, Value_interation: {value_interation}')
#print (f'Всего было сыграно {value_interation} партий. Компьютер в среднем подобрал число за {(mean_total)} циклов')

#print ('Второй вариант подсчета:')
#print (f'Длина списка=кол игр: {len(list_count)}, медиана списка: {mean}')
#print (f'Всего было сыграно {value_interation} партий. Компьютер в среднем подобрал число за {(mean)} циклов')









