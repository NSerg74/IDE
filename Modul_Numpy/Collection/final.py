import numpy as np

#Задача №1
#генерится квадрат со стороной а, внутри массив с чередованием 0 и 1, в левом вверхнем углу всегда 0
def get_chess(a):
    if a % 2 == 0 and a > 2:
        #делаем все тоже самое, как и с нечетными числами
        # чтобы получить шахматную доску, мы все четные ряды переботаем
        square = np.zeros((a, a), dtype=np.int8)
        square.shape = (a**2)
        square[1::2] = 1
        square.shape = (a,a)
        #в этом цикле кадую вторую строчку мы обработаем
        for i in range(a):
             if i % 2:
                 #сначало ее обнулим, а потом через одну, поставим единицу, причем начнем с 1
                 square[i, :] = np.zeros(a, dtype=np.int8)
                 square[i, ::2] = 1
        else:
         square = np.zeros((a, a), dtype=np.int8)
         square.shape = (a**2)
         square[1::2] = 1
         square.shape = (a,a)    
    
    
    #меняем тип на float
    square = np.float16(square)
   
    return square


#Задача №2
#Для этого напишите функцию shuffle_seed(array), которая принимает на вход массив из чисел, 
#генерирует случайное число для seed в диапазоне от 0 до 2**32 - 1 (включительно) и возвращает кортеж: 
#перемешанный с данным seed массив (исходный массив должен оставаться без изменений), а также seed, с которым этот массив был получен.
def shuffle_seed(array):
    array_in = np.array(array)
    low, high = 0, 2**32 
    seed = np.random.randint(low,high, dtype=np.int64)
    #закладываем зерно
    np.random.seed(seed)
    #мешаем массив с новой копией
    array_per = np.random.permutation(array_in)
    #приведем к встроенному типу int
    seed = int(seed)
    #и возвращаем кортежем
    return array_per, seed
  
#array = [1, 2, 3, 4, 5]
#print (shuffle_seed(array))



#Задание №3

def min_max_dist(*vectors):
    #сколько всего векторов в кортеже
    value_vectors = len(vectors)
    #лист где хранятся все дистанции между векторами
    list_distance = []
    #общий цикл обхода кортежа
    for i in range(value_vectors):
        #берем n-ый вектор из кортежа, и сравниваем его с со всеми остальными
        vector_compare = vectors[i]
        for current_vector in vectors:
            #вычисляем расстояние между текущим вектором и вектором из общего цикла
            distance = float(np.linalg.norm(vector_compare - current_vector))
            #если растояние ноль, то это один и то же вектор
            if distance == 0:
                #пропускаем его
                continue
            #если нет, то дабавляем в лист, где хранятся все дистанции между векторами
            else:
                list_distance.append(distance)
    
    #под конец возращаем мин и макс растояние
    return min(list_distance), max(list_distance)
            
#vec1 = np.array([1,2,3])
#vec2 = np.array([4,5,6])
#vec3 = np.array([7, 8, 9])
#print(min_max_dist(vec1, vec2, vec3))    
#(5.196152422706632, 10.392304845413264)    



#Задание №4
#поиск ортогональности неограниченого кол векторов

def any_normal(*vectors):
    #сколько всего векторов в кортеже
    value_vectors = len(vectors)
    
    #общий цикл обхода кортежа
    for i in range(value_vectors):
        #берем n-ый вектор из кортежа, и сравниваем его с со всеми остальными
        vector_compare = vectors[i]
        for current_vector in vectors:
            #вычисляем расстояние между текущим вектором и вектором из общего цикла
            orto = np.dot(vector_compare,current_vector)
            #при ортогональности будет True
            if orto:
                return True
                
            
    #если не выскочили по True, тогда False
    return False

#vec1 = np.array([2, 1])
#vec2 = np.array([-1, 2])
#vec3 = np.array([3,4])
#print(any_normal(vec1, vec2, vec3))

#Задача №5
#генерит массив по заданным параметрам
def get_loto(num):
    array_loto = np.random.randint(1,101, size=(num,5,5))
    return array_loto    

#Задача №6
#сгенерить массив по заданным параметрам и чтобы цифы в полях не повторялись
def get_unique_loto(num):
    array_loto = []
    for i in range(num):
        numbers = np.random.choice(np.arange(1, 101), size=(25), replace=False)
        numbers.shape = (5,5)
        array_loto.append(numbers)
        
    result = np.array(array_loto)
    
    return result
    
    
    
    return numbers 

#print(get_unique_loto(10))  
simplelist = [19, 242, 14, 152, 142, 1000]
print(sum(simplelist)/len(simplelist))