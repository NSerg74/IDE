from collections import deque
from collections import OrderedDict

temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]
#сортировка словаря по второму элементу в кортеже 
def check(temps):
    temps_sort = OrderedDict(sorted(temps, key=lambda x: x[1], reverse=True))
    return temps_sort

#работа с деком
#дек или очередь пользователей
users = [6, 18, 4, 7, 8, 8, 5, 18, 12, 17, 13, 15, 6, 7, 9, 17, 18, 8, 4, 11, 10, 8, 2, 10, 6, 10, 10, 9]
#создаме очередь из листа
users_deq = deque(users)
#извлекамем первого
user_one = users_deq.popleft()
print(user_one)
#пять пользователей перемещаем из начала в конец

users_deq.rotate(-5)
print(users_deq)
#теперь извлекаем последнего
user_end = users_deq.pop()
print(user_end)
#посмотрим сколько еще раз встречается извлеченный послений элемент
print(f'Элемент {user_end} в деке встречается: {users_deq.count(user_end)} раза')
