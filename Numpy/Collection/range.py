import numpy as np
import matplotlib.pyplot as plt

#1 В simple сохраните случайное число в диапазоне от 0 до 1
#2 Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их в переменную randoms
#3 Получите массив из случайных целых чисел от 1 до 100 (включительно) из 3 строк и 2 столбцов. Сохраните результат в table
#4 В переменную even сохраните четные числа от 2 до 16 (включительно)
#5 Скопируйте even в переменную mix. Перемешайте числа в mix так, чтобы массив изменился
#6 Получите из even 3 числа без повторений. Сохраните их в переменную select
#7 Получите переменную triplet, которая должна содержать перемешанные значения из массива select (сам select измениться не должен)

#задаем зерно для кореектности проверки 
np.random.seed(2021)

#1 
simple = np.random.rand()
#2
randoms = np.random.uniform(-150, 2022, size=120)
#3
table = np.random.randint(1, 101, size=(3, 2))
#4
even = np.arange(2, 17, 2)
#5
mix = np.random.permutation(even)
#6
select = np.random.choice(even, size=3, replace=False)
#7
triplet = np.random.permutation(select)
