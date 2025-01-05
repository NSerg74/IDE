import numpy as np


#функция генерации массива номер от 0 до 100 в количестве=аргумент функции
def generation_list (len_list=100):
    return_list = []
    for i in range(len_list):
        return_list.append(np.random.randint(1,101))
        
    return return_list


#функция поиска числа, на входе сгенирированное число
#на выходе искомое число и количество циклов потраченное на поиск
def find_number(random_num):
    high = 100                  #вверхняя граница диапазона поиска
    low =0                      #нижняя граница диапазона поиска    
    A = (low+high)//2
    count_find = 0
    while True:
        count_find += 1         #один проход плюс один к счетчику
        A = (high+low)//2       #предпологаемое число, с двумя границами поиска
        if A > random_num:
            high = A - 1        #если предпологаемое число больше, уменьшаем вверхнюю граница поиска
        if A < random_num:
            low = A + 1         #если предпологаемое число меньше, увеличиваем нижнюю границу поиска
        if A == random_num:     #нашли, конец циклу
            break
        
    return count_find
    
    
         
total_count = 0                     #переменная для подсчета общего кол циклов подбора, 1 вариант подсчета
random_list = generation_list()     #получаем массив сгенерированных чисел

#пройдемся по нему циклом и поищем эти числа нашим алгоритмом
for num in random_list:
    value_find = find_number(num)
    total_count += value_find
    
#найдем сколько в среднем тратится проходов на поиск нужного числа
#для этого общее кол поисков разделим на количство "игр", или количество сгенерированных чисел
len_random_list = len(random_list)
mean_count = total_count / len_random_list
    
    
    
print (f'Всего было сыграно {len(random_list)} партий. Компьютер в среднем подобрал число за {(mean_count)} циклов')








