import numpy as np


#генерится квадрат со стороной а, внутри массив с чередованием 0 и 1, впереди всегда 0
def get_chess(a):
    #генерим нулевой массив а на а
    square = np.zeros((a, a), dtype=np.int8)
    #разворачиваем его в одномерный
    square.shape = (a**2)
    #c помщью среза берем каждое второе и меняем на 1
    square[1::2] = 1
    #из одномерного, делаем двумерный
    if a % 2 == 0:
        square.shape = (a,a)
        square[::2,::1] = 1
        
    else: 
        square.shape = (a,a)
    #меняем тип на float
    square = np.float16(square)
   
    return square

print(get_chess(8))
