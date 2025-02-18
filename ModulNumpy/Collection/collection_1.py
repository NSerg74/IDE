from collections import deque #дека, стек, рюкзак
from collections import OrderedDict #словарь с фиксированными индексами
from collections import Counter #счетчик
from collections import defaultdict

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
#print(user_one)
#пять пользователей перемещаем из начала в конец

users_deq.rotate(-5)
#print(users_deq)
#теперь извлекаем последнего
user_end = users_deq.pop()
#print(user_end)
#посмотрим сколько еще раз встречается извлеченный послений элемент
#print(f'Элемент {user_end} в деке встречается: {users_deq.count(user_end)} раза')

#работа со стеком, функция проверяет последовательность скобок (через костыль, работает)
def brackets(line):
    sub_str = str(line)
    stack = deque(line)
    #счетчик для контроля, первая скобка должна быть открывающаяся!
    count = 0 
    for simbol in sub_str:
      count += 1
      if simbol == '(':
          try:
            #поищем пару этой скобки и извлечем ее из стека
            index_find = stack.index(')')
            del stack[index_find]
          #здесь мы ловим ошибку если пары не нашлось, то возращаем False
          except ValueError: 
              return False
      #если у нас первая скобка не открывающася, то это не правильно!(костыль)
      elif simbol == ')' and count == 1:
          return False
      elif simbol == ')' and count != 1:
            try:
                #поищем пару и для этой скобки и извлечем ее из стека
                index_find = stack.index('(')
                del stack[index_find]
            #здесь мы ловим ошибку если пары не нашлось, то возращаем False
            except ValueError: 
              return False
      else: #если символы левые, то мы продолжим перебор  строки
          continue
    #по окончанию перебора, если все норм, стек должен быть пустой
    if len(stack) == 0:
        return True
    else:
        return False  
#посмотрим как работает наша функция
#print(brackets("(()())"))
# True
#print(brackets(""))
# True
#print(brackets("(()()))"))
# False
#print(brackets(')))((('))   
#False
#####################################################################################################################################################################
#Следующая задача, так понимаю на счетчики. Это типа списки с вложенными списками с продажами по дням        
center = [['Meat', 'Beer', 'Soap', 'Beer', 'Cheese', 'Cola', 'Milk', 'Soap', 'Cola', 'Meat', 'Bread', 'Chocolate', 'Chips'], 
          ['Soap', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Beer', 'Cheese', 'Cheese', 'Beer', 'Chips', 'Chocolate', 'Chips', 'Cheese', 'Bread', 'Cola', 'Cola', 'Beer'], 
          ['Cola', 'Soap', 'Bread', 'Milk', 'Beer', 'Meat', 'Bread', 'Bread'], ['Ketchup', 'Beer', 'Ketchup', 'Chocolate', 'Milk', 'Milk', 'Bread', 'Beer'], 
          ['Beer', 'Beer', 'Meat', 'Ketchup', 'Soap', 'Bread', 'Cola', 'Beer'], ['Meat', 'Bread', 'Milk', 'Cheese', 'Soap', 'Beer', 'Milk', 'Cheese', 'Cola', 'Beer', 'Chips', 'Bread', 'Ketchup', 'Chocolate', 'Bread', 'Milk'], 
          ['Yoghurt'], ['Beer', 'Milk', 'Chips', 'Soap', 'Chips', 'Milk', 'Beer', 'Chips', 'Bread', 'Meat', 'Milk'], ['Yoghurt', 'Beer', 'Cola', 'Cola', 'Beer', 'Soap', 'Cheese', 'Soap', 'Bread', 'Cola', 'Yoghurt', 'Ketchup', 'Beer', 'Milk'], 
          ['Milk', 'Cola', 'Bread', 'Cola', 'Bread', 'Beer', 'Beer', 'Beer'], ['Yoghurt', 'Cola'], 
          ['Bread', 'Yoghurt', 'Chips', 'Ketchup', 'Meat', 'Bread', 'Beer', 'Yoghurt', 'Cola', 'Cola'], 
          ['Chips', 'Chocolate', 'Chips', 'Meat', 'Bread', 'Cheese', 'Bread', 'Yoghurt'], ['Ketchup', 'Soap', 'Chocolate', 'Bread'], 
          ['Chips', 'Beer', 'Chips', 'Cola', 'Cheese', 'Soap', 'Ketchup', 'Meat', 'Cola', 'Chips', 'Beer', 'Chocolate', 'Beer', 'Milk', 'Bread', 'Ketchup', 'Chips', 'Cheese', 'Ketchup'], 
          ['Beer', 'Milk', 'Soap', 'Chips', 'Soap', 'Bread', 'Bread', 'Milk', 'Beer'], ['Cola', 'Chips', 'Meat', 'Cola', 'Beer', 'Chocolate', 'Bread', 'Bread', 'Chips', 'Soap', 'Chocolate', 'Chips', 'Beer'], 
          ['Meat', 'Cola', 'Chips', 'Bread', 'Chips', 'Chocolate', 'Bread', 'Meat', 'Bread', 'Yoghurt', 'Cheese', 'Bread', 'Chips', 'Cola'], 
          ['Chips', 'Cheese', 'Bread', 'Beer', 'Bread', 'Chips', 'Chocolate', 'Bread', 'Cola', 'Cola', 'Chocolate', 'Chocolate', 'Bread', 'Meat', 'Chips'], 
          ['Bread', 'Milk', 'Bread', 'Cheese', 'Bread', 'Cheese', 'Ketchup', 'Beer', 'Cheese', 'Cola', 'Milk', 'Milk', 'Bread', 'Beer', 'Bread', 'Chips'], ['Yoghurt'], 
          ['Bread', 'Bread', 'Chips', 'Cheese', 'Bread', 'Beer', 'Cola', 'Ketchup', 'Bread', 'Chips', 'Chocolate', 'Meat', 'Milk', 'Beer', 'Milk', 'Cheese', 'Bread', 'Meat', 'Bread', 'Cola'], 
          ['Bread', 'Meat', 'Meat', 'Milk', 'Chips', 'Soap', 'Yoghurt', 'Chips', 'Beer', 'Yoghurt'], ['Bread', 'Soap', 'Bread', 'Cola', 'Bread'], ['Cola', 'Bread', 'Meat', 'Cola', 'Meat', 'Chocolate', 'Chips', 'Meat', 'Chips'], 
          ['Chips', 'Cheese', 'Cheese', 'Meat'], ['Chips', 'Meat', 'Soap', 'Cheese', 'Bread', 'Cola', 'Bread', 'Beer', 'Meat', 'Cola', 'Bread', 'Cola', 'Ketchup', 'Bread'], 
          ['Chips', 'Cheese', 'Milk', 'Meat', 'Milk', 'Beer', 'Chocolate', 'Ketchup', 'Cola', 'Cheese', 'Beer'], 
          ['Beer', 'Ketchup', 'Yoghurt', 'Ketchup', 'Chocolate', 'Bread', 'Beer', 'Ketchup', 'Chocolate', 'Cola', 'Chocolate', 'Ketchup', 'Cola', 'Meat', 'Chips', 'Soap', 'Meat'], 
          ['Meat', 'Milk'], ['Cola', 'Beer', 'Yoghurt', 'Beer', 'Bread', 'Cola'], ['Chips', 'Meat', 'Cheese', 'Ketchup', 'Chips', 'Bread', 'Bread', 'Chips', 'Chips', 'Bread', 'Milk', 'Ketchup', 'Cola', 'Cola', 'Beer'], 
          ['Beer', 'Bread', 'Cheese', 'Bread', 'Cola', 'Cheese', 'Cheese', 'Beer', 'Milk', 'Bread', 'Chocolate', 'Cheese', 'Beer', 'Bread', 'Beer', 'Cola', 'Yoghurt', 'Beer', 'Beer', 'Chips'], 
          ['Bread', 'Chips', 'Bread', 'Cola', 'Chips', 'Chocolate', 'Cheese', 'Beer', 'Chips', 'Milk', 'Milk', 'Beer', 'Cola', 'Meat', 'Cola', 'Bread', 'Cola', 'Chocolate', 'Chocolate', 'Cola'], 
          ['Soap', 'Yoghurt', 'Chips', 'Beer', 'Chips', 'Milk', 'Cheese', 'Meat', 'Beer', 'Bread', 'Ketchup', 'Bread', 'Bread', 'Cheese', 'Milk', 'Beer', 'Beer', 'Soap', 'Bread'], 
          ['Cola', 'Bread', 'Cheese', 'Ketchup', 'Beer', 'Chips', 'Meat', 'Chocolate', 'Chips', 'Cola', 'Beer', 'Beer', 'Cola'], 
          ['Ketchup', 'Beer', 'Chocolate', 'Bread', 'Yoghurt', 'Beer', 'Cheese'], ['Bread', 'Chocolate', 'Bread', 'Milk'], ['Meat', 'Yoghurt', 'Bread', 'Yoghurt', 'Cola', 'Ketchup'], 
          ['Ketchup', 'Bread', 'Bread', 'Chocolate', 'Chocolate', 'Chocolate', 'Bread', 'Bread', 'Beer', 'Chocolate', 'Bread', 'Milk'], ['Bread', 'Cheese', 'Soap', 'Soap', 'Chips', 'Chips'], 
          ['Ketchup', 'Chocolate', 'Chips', 'Milk', 'Soap', 'Soap', 'Ketchup', 'Bread', 'Ketchup', 'Cola', 'Cheese', 'Beer', 'Ketchup', 'Bread'], 
          ['Bread', 'Milk', 'Beer', 'Yoghurt', 'Meat', 'Ketchup', 'Meat', 'Meat', 'Bread', 'Milk', 'Cheese', 'Beer', 'Yoghurt', 'Milk', 'Bread', 'Cola'], 
          ['Chips', 'Cola', 'Milk', 'Chocolate', 'Beer', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Bread', 'Beer', 'Ketchup', 'Milk', 'Yoghurt', 'Ketchup', 'Cola', 'Ketchup', 'Chips', 'Meat'], 
          ['Beer', 'Bread', 'Soap', 'Cheese', 'Meat', 'Soap'], ['Beer', 'Meat', 'Beer', 'Yoghurt', 'Soap', 'Chips', 'Meat', 'Cheese', 'Milk', 'Bread', 'Meat', 'Beer', 'Milk'], ['Chips', 'Meat', 'Bread'], 
          ['Chocolate', 'Soap', 'Bread', 'Chips', 'Chips', 'Yoghurt', 'Chips', 'Cola', 'Cola', 'Cola', 'Beer', 'Milk', 'Milk', 'Bread', 'Bread', 'Meat'], 
          ['Meat', 'Chocolate', 'Chips', 'Chips', 'Yoghurt', 'Yoghurt', 'Beer', 'Cola', 'Cheese', 'Milk', 'Beer'], ['Meat', 'Chocolate', 'Yoghurt', 'Cola', 'Cheese', 'Meat', 'Bread', 'Beer', 'Meat', 'Beer', 'Yoghurt', 'Cola', 'Bread']]
south = [['Cola', 'Meat', 'Cheese', 'Yoghurt', 'Beer', 'Milk', 'Milk', 'Meat', 'Cola', 'Cola', 'Cheese', 'Beer', 'Yoghurt', 'Beer', 'Bread', 'Bread', 'Milk', 'Cheese', 'Chocolate'], 
         ['Soap', 'Milk', 'Cola'], ['Milk', 'Bread', 'Yoghurt', 'Meat', 'Meat'], ['Bread', 'Milk', 'Beer'], ['Beer'], ['Chocolate', 'Meat', 'Chocolate', 'Cola', 'Cola', 'Cola', 'Cola', 'Yoghurt', 'Bread', 'Meat', 'Soap', 'Soap', 'Milk', 'Milk', 'Cola'], 
         ['Beer', 'Beer', 'Meat', 'Chips', 'Bread', 'Bread', 'Bread', 'Bread', 'Milk', 'Cola', 'Chocolate', 'Bread', 'Beer', 'Chips', 'Bread', 'Bread', 'Yoghurt'], ['Chips', 'Milk', 'Soap'], 
         ['Meat', 'Beer', 'Milk', 'Chocolate', 'Bread', 'Yoghurt'], ['Chips', 'Meat', 'Chocolate', 'Bread', 'Cola', 'Cola', 'Chocolate', 'Meat', 'Yoghurt', 'Milk'], 
         ['Bread', 'Soap', 'Bread', 'Meat', 'Beer', 'Yoghurt', 'Milk', 'Cola', 'Bread', 'Ketchup'], ['Meat', 'Milk'], ['Meat', 'Beer', 'Yoghurt'], ['Cola', 'Bread', 'Cola', 'Chocolate', 'Chips', 'Meat', 'Cheese'], 
         ['Milk', 'Milk', 'Cheese', 'Meat'], ['Chips', 'Yoghurt', 'Cheese', 'Soap', 'Ketchup', 'Cheese', 'Soap', 'Beer', 'Ketchup', 'Ketchup', 'Milk', 'Bread', 'Bread', 'Beer'], ['Meat'], 
         ['Ketchup', 'Bread', 'Beer', 'Milk', 'Bread', 'Meat', 'Ketchup', 'Cheese'], ['Meat', 'Chips', 'Bread', 'Meat', 'Milk', 'Soap', 'Chocolate', 'Meat', 'Chocolate', 'Chocolate', 'Bread', 'Cheese', 'Soap', 'Cola', 'Yoghurt'], 
         ['Cheese', 'Milk', 'Bread', 'Milk', 'Chips', 'Chips', 'Meat', 'Beer', 'Chocolate', 'Chocolate'], ['Ketchup', 'Beer', 'Cheese', 'Cola'], ['Chocolate', 'Cheese', 'Bread'], 
         ['Milk', 'Yoghurt', 'Ketchup', 'Beer', 'Meat', 'Chips', 'Yoghurt', 'Meat', 'Bread', 'Chips'], ['Yoghurt', 'Milk', 'Ketchup', 'Yoghurt', 'Beer', 'Cheese', 'Bread', 'Bread', 'Ketchup', 'Bread', 'Bread', 'Yoghurt', 'Meat'], 
         ['Soap', 'Meat', 'Bread', 'Beer', 'Milk'], ['Beer', 'Cola', 'Beer', 'Meat', 'Meat', 'Cheese', 'Meat', 'Chocolate', 'Bread', 'Ketchup', 'Milk', 'Soap'], 
         ['Cheese', 'Chocolate', 'Milk', 'Chocolate', 'Cola', 'Bread', 'Chips', 'Cheese', 'Soap', 'Ketchup', 'Cheese', 'Chips', 'Cheese', 'Cola', 'Chocolate', 'Beer'], 
         ['Bread', 'Bread', 'Cola', 'Ketchup', 'Cola', 'Bread', 'Meat', 'Yoghurt', 'Milk', 'Beer', 'Beer', 'Cheese', 'Meat', 'Bread', 'Cheese', 'Meat', 'Chocolate'], 
         ['Chocolate', 'Soap', 'Chips', 'Beer', 'Bread', 'Yoghurt', 'Chips', 'Chocolate', 'Beer', 'Cheese', 'Cola', 'Milk', 'Chips', 'Milk', 'Ketchup', 'Cola', 'Meat', 'Beer', 'Cheese', 'Yoghurt'], ['Soap'], 
         ['Meat', 'Beer', 'Milk', 'Bread', 'Beer', 'Cheese', 'Chocolate', 'Beer', 'Beer', 'Milk', 'Beer', 'Bread', 'Meat', 'Beer', 'Chocolate', 'Beer', 'Soap', 'Chips', 'Cola'], 
         ['Cola', 'Beer', 'Meat', 'Chips', 'Soap', 'Cola', 'Bread', 'Cola', 'Bread', 'Chips', 'Ketchup', 'Ketchup', 'Beer', 'Ketchup', 'Cola', 'Milk', 'Cheese'], 
         ['Cheese', 'Milk', 'Chips', 'Bread', 'Yoghurt', 'Soap', 'Beer', 'Chips', 'Ketchup', 'Chips', 'Beer', 'Yoghurt', 'Cola', 'Cheese', 'Chocolate', 'Beer'], ['Meat', 'Bread', 'Meat', 'Bread'], 
         ['Cola', 'Beer', 'Yoghurt'], ['Beer', 'Bread', 'Beer', 'Meat', 'Bread', 'Milk', 'Soap', 'Milk', 'Chocolate', 'Meat', 'Meat', 'Meat', 'Chips', 'Chocolate', 'Meat'], 
         ['Beer', 'Cola', 'Chocolate', 'Bread', 'Cheese', 'Cheese'], ['Milk', 'Chips', 'Cola', 'Milk', 'Bread', 'Bread', 'Beer', 'Milk', 'Cola', 'Chocolate', 'Chocolate', 'Meat', 'Cola', 'Cola', 'Beer', 'Cola', 'Chocolate', 'Bread', 'Bread', 'Cola'], 
         ['Chocolate', 'Chocolate', 'Beer', 'Beer', 'Bread', 'Yoghurt', 'Meat', 'Cola', 'Yoghurt'], ['Ketchup', 'Cola', 'Ketchup', 'Yoghurt', 'Chips', 'Soap', 'Soap', 'Chocolate', 'Chocolate', 'Bread', 'Beer', 'Meat'], 
         ['Bread', 'Meat', 'Soap', 'Cola', 'Bread', 'Cola', 'Yoghurt', 'Meat', 'Bread', 'Cola', 'Cola', 'Ketchup', 'Beer', 'Bread', 'Milk', 'Yoghurt', 'Meat'], ['Chocolate', 'Yoghurt', 'Bread'], 
         ['Meat', 'Bread', 'Bread', 'Bread'], ['Beer', 'Milk', 'Cola', 'Ketchup', 'Cola', 'Cheese', 'Meat', 'Chocolate'], ['Soap', 'Beer', 'Chocolate', 'Chocolate', 'Cola', 'Cola', 'Yoghurt', 'Ketchup', 'Milk'], 
         ['Meat', 'Yoghurt', 'Bread', 'Ketchup', 'Ketchup', 'Milk', 'Meat'], ['Ketchup', 'Soap', 'Chips', 'Ketchup', 'Bread', 'Chocolate', 'Milk', 'Bread', 'Bread', 'Ketchup', 'Cola', 'Meat', 'Milk', 'Bread', 'Cola'], 
         ['Meat', 'Beer', 'Yoghurt', 'Chips', 'Beer', 'Meat', 'Cola', 'Beer', 'Meat', 'Ketchup', 'Milk', 'Cola', 'Yoghurt', 'Beer', 'Meat', 'Bread', 'Bread'], 
         ['Meat', 'Soap', 'Cheese', 'Ketchup', 'Cola', 'Cola', 'Bread', 'Chips', 'Meat', 'Cola', 'Bread', 'Beer', 'Beer', 'Beer'], ['Meat', 'Yoghurt', 'Bread', 'Milk', 'Beer', 'Beer']]
north= [['Milk', 'Milk', 'Beer'], ['Chocolate', 'Bread', 'Chips'], ['Cola', 'Cola', 'Yoghurt', 'Soap', 'Beer', 'Chips', 'Milk'], ['Soap', 'Soap', 'Cola', 'Cola', 'Chips'], 
        ['Milk', 'Beer', 'Meat', 'Ketchup', 'Cola', 'Cola', 'Chips', 'Chips', 'Cola', 'Cola'], ['Beer', 'Bread', 'Bread', 'Beer', 'Beer', 'Beer', 'Bread', 'Cheese'], 
        ['Yoghurt', 'Beer', 'Chips', 'Milk', 'Soap', 'Cola', 'Cola', 'Cola', 'Beer', 'Cola', 'Cola', 'Cola', 'Beer', 'Ketchup', 'Beer', 'Beer', 'Beer', 'Soap'], 
        ['Milk', 'Cola', 'Cola', 'Beer', 'Beer', 'Bread', 'Bread', 'Soap', 'Cola', 'Cola', 'Beer', 'Meat', 'Bread', 'Chips'], 
        ['Beer', 'Beer', 'Beer', 'Chips', 'Milk', 'Cola', 'Chocolate', 'Beer', 'Chocolate', 'Beer', 'Beer', 'Cola', 'Meat', 'Yoghurt', 'Beer'], ['Bread'], 
        ['Chocolate', 'Beer', 'Meat', 'Yoghurt'], ['Cola', 'Beer', 'Beer', 'Beer', 'Chocolate', 'Beer', 'Soap', 'Beer', 'Chips', 'Soap', 'Chocolate', 'Bread', 'Chips', 'Cola', 'Bread', 'Beer', 'Cola', 'Bread'], 
        ['Chips', 'Cola', 'Beer', 'Chips', 'Cola', 'Cola', 'Beer', 'Soap', 'Yoghurt', 'Yoghurt', 'Cola', 'Bread', 'Beer', 'Chocolate', 'Chips', 'Bread', 'Beer', 'Bread'], 
        ['Cola', 'Chocolate'], ['Chocolate', 'Cola', 'Meat', 'Cola', 'Ketchup', 'Cola', 'Chocolate', 'Bread', 'Chocolate', 'Chocolate', 'Meat'], ['Bread', 'Milk', 'Chips', 'Ketchup', 'Cola', 'Cola', 'Cola', 'Beer', 'Beer', 'Soap', 'Beer', 'Cola'], 
        ['Yoghurt', 'Milk', 'Soap', 'Bread', 'Cola', 'Cola', 'Milk', 'Bread', 'Chips', 'Cheese', 'Milk', 'Yoghurt', 'Bread', 'Yoghurt'], ['Cola', 'Ketchup'], 
        ['Cola', 'Yoghurt', 'Bread', 'Cola', 'Cola', 'Chips', 'Yoghurt', 'Milk', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Cola', 'Bread', 'Beer', 'Beer', 'Cheese'], 
        ['Beer', 'Cheese', 'Ketchup', 'Beer'], ['Beer', 'Beer', 'Beer'], ['Soap', 'Beer', 'Beer', 'Chocolate', 'Cola', 'Chocolate', 'Bread', 'Beer', 'Milk', 'Bread', 'Beer', 'Chocolate', 'Bread', 'Cola', 'Cola', 'Cheese', 'Beer', 'Cola', 'Soap', 'Yoghurt'], 
        ['Beer', 'Chocolate'], ['Cola', 'Beer'], ['Yoghurt', 'Beer', 'Yoghurt', 'Yoghurt', 'Chips', 'Meat', 'Beer', 'Chocolate', 'Cola', 'Cola', 'Chips', 'Bread'], 
        ['Cola', 'Cola', 'Cola', 'Cola', 'Cola', 'Bread', 'Chips', 'Soap', 'Cola', 'Chocolate', 'Beer', 'Beer'], ['Beer', 'Cola', 'Cola', 'Bread', 'Soap', 'Beer', 'Meat', 'Beer', 'Beer', 'Beer', 'Cola', 'Chips', 'Beer', 'Cola', 'Cola', 'Bread', 'Cheese', 'Beer'], 
        ['Cola', 'Cola', 'Ketchup', 'Beer', 'Yoghurt', 'Bread'], ['Chips', 'Yoghurt', 'Cola', 'Cola', 'Cola', 'Chocolate', 'Chips', 'Bread', 'Chocolate', 'Yoghurt', 'Chocolate', 'Milk', 'Bread', 'Bread', 'Soap', 'Milk', 'Soap', 'Cola', 'Bread', 'Beer'], 
        ['Beer', 'Beer', 'Ketchup', 'Cola', 'Beer', 'Bread', 'Beer', 'Cola', 'Beer', 'Chocolate'], 
        ['Beer', 'Chocolate', 'Cola', 'Beer', 'Yoghurt', 'Milk', 'Bread', 'Cheese', 'Yoghurt', 'Beer', 'Cola', 'Yoghurt', 'Cola', 'Soap', 'Beer', 'Bread', 'Meat', 'Bread', 'Cola'], ['Beer', 'Cola', 'Chips', 'Cola'], 
        ['Cola', 'Cola', 'Beer', 'Cheese'], ['Bread', 'Soap', 'Ketchup', 'Chocolate', 'Beer', 'Cola', 'Chocolate', 'Cola', 'Cola', 'Yoghurt', 'Beer', 'Bread', 'Cola', 'Ketchup', 'Beer'], ['Bread'], 
        ['Bread', 'Beer', 'Yoghurt', 'Yoghurt', 'Bread', 'Milk', 'Soap', 'Meat', 'Bread', 'Beer', 'Cola', 'Milk', 'Milk', 'Bread', 'Beer', 'Cola', 'Ketchup', 'Cola'], 
        ['Bread', 'Beer', 'Bread', 'Yoghurt', 'Beer', 'Bread', 'Cola', 'Cola', 'Cola', 'Beer', 'Bread', 'Milk', 'Chips', 'Cola', 'Beer', 'Bread', 'Soap', 'Bread', 'Yoghurt', 'Bread'], 
        ['Yoghurt', 'Beer', 'Cola', 'Beer', 'Beer', 'Beer'], ['Chips', 'Chocolate', 'Soap', 'Chocolate', 'Cola', 'Bread', 'Beer', 'Cola', 'Beer', 'Ketchup', 'Chocolate', 'Ketchup', 'Ketchup', 'Cheese', 'Chips', 'Beer', 'Chips', 'Chocolate'], 
        ['Bread', 'Cola', 'Cola', 'Beer', 'Bread', 'Bread', 'Beer', 'Chocolate', 'Bread', 'Cola', 'Milk', 'Chips', 'Meat', 'Beer', 'Beer', 'Soap', 'Bread'], 
        ['Beer', 'Beer', 'Bread', 'Chips', 'Beer', 'Bread', 'Bread', 'Chips', 'Beer'], ['Yoghurt', 'Bread', 'Cola', 'Bread', 'Cola', 'Bread', 'Meat', 'Cola', 'Bread', 'Beer', 'Soap', 'Chips'], ['Bread', 'Beer'], 
        ['Milk', 'Beer', 'Meat', 'Cola', 'Beer', 'Cola', 'Cola'], ['Beer', 'Chips', 'Yoghurt', 'Beer', 'Cola', 'Beer', 'Cola', 'Cola', 'Soap', 'Cola'], ['Bread', 'Cola', 'Cola', 'Meat'], 
        ['Cola', 'Chocolate', 'Meat', 'Beer', 'Cola', 'Bread', 'Chips', 'Beer', 'Chips', 'Chips', 'Cola'], 
        ['Bread', 'Cola', 'Cola', 'Cola', 'Beer', 'Cola', 'Yoghurt', 'Beer', 'Chips', 'Cola', 'Chocolate', 'Chips', 'Cola', 'Cola', 'Cola', 'Cola', 'Bread', 'Cola'], ['Cola', 'Soap', 'Cola'], 
        ['Soap', 'Chips', 'Cola', 'Beer', 'Bread', 'Soap', 'Cheese', 'Bread', 'Beer', 'Chocolate']]


#делаем из списка счетчик с сумированием
def packing_and_counting(shop_list):
    sales_count = Counter()
    for sale in shop_list:         
        sales_count += Counter(sale)
    #sales_count = sorted(sales_count.items(), key=lambda item: item[1], reverse=True)    
    return sales_count

#поиск аномально популярной позиции в одном из магазинов (отлично работает)
#аномалия, это когда продажи позиции в одном магазине, превышают сумарные продажи в двух других 
def find_anomaly (count_a, count_b, count_c):
    
    #сюда мы будем запихивать аномальные позиции
    list_anomaly = []

    #поищемс сначало относительно А
    for name in count_a:
        #поиск такой позиции на двух других складах, если хотя бы на одном нет, пропуск
        #если значение в счетчике нет, то будет ноль, пропускааем ход
        if count_b[name] == 0 or count_c[name] == 0:
            continue
        else:
            sum = count_b[name] + count_c[name]
        #встретили аномалию, воткнули в лист
        if count_a[name] > sum:
           x = (name, count_a[name], 'center')
           list_anomaly.append(x)
    #поищем относительно B
    for name in count_b:
        #поиск такой позиции на двух других складах, если хотя бы на одном нет, пропуск
        #если значение в счетчике нет, то будет ноль, пропускааем ход
        if count_a[name] == 0 or count_c[name] == 0:
            continue
        else:
            sum = count_a[name] + count_c[name]
        #встретили аномалию, воткнули в лист
        if count_b[name] > sum:
           x = (name, count_b[name], 'south')
           list_anomaly.append(x)
    #поищемс сначало относительно C
    for name in count_c:
        #поиск такой позиции на двух других складах, если хотя бы на одном нет, пропуск
        #если значение в счетчике нет, то будет ноль, пропускааем ход
        if count_a[name] == 0 or count_b[name] == 0:
            continue
        else:
            sum = count_a[name] + count_b[name]
        #встретили аномалию, воткнули в лист
        if count_c[name] > sum:
           x = (name, count_c[name], 'north')
           list_anomaly.append(x)
            
    return list_anomaly
    

#def summ(shop_dict):
#    sum = 0
#    for element in shop_dict:
#       sum += shop_dict[element]
#    return sum
        
dict_shop_center = packing_and_counting (center)
#print(dict_shop_center)
#print(summ(dict_shop_center))
dict_shop_south = packing_and_counting (south)
#print(dict_shop_south)
#print(summ(dict_shop_south))
dict_shop_north = packing_and_counting (north)
#print(dict_shop_north)
#print(summ(dict_shop_north))
#print(f'Разность двух счечиков:\n{dict_shop_center - dict_shop_north}')
anomaly_position = find_anomaly(dict_shop_center, dict_shop_south, dict_shop_north)
#print(f'Обнаружена аномальная продажа товара {anomaly_position[0][0]}, по складу {anomaly_position[0][2]}, сумма выручки {anomaly_position[0][1]}')
total_count_sale = dict_shop_center + dict_shop_north + dict_shop_south
#print(f'Общий сумарный обьем продаж {total_count_sale}')

#####################################################################################################################################################################
#тут мы повторяем сортировку и исп обьект OrderedDict из Collection
ratings = [
    ('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
    ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
    ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)
    ]

cafe_rating = sorted(ratings, key=lambda x: (-x[1], x[0]))
dict_cafe = OrderedDict(cafe_rating)
#print(dict_cafe)
#OrderedDict({'WokAndRice': 4.9, 'WokToWork': 4.9, 'General Foods': 4.8, 'New Age': 4.6, 
# 'Belissimo': 4.5, 'CakeAndCoffee': 4.2, 'CakeOClock': 4.2, 'CakeTime': 4.1, 'Nice Cakes': 3.9, 
# 'Old Gold': 3.3, 'Old Wine Cellar': 3.3, 'Old York': 3.3})     

#####################################################################################################################################################################
#новое задание, на тему дека, распределения задач по серверам в зависимости от очереди и приоритета

#на выходе список кортежей с задачами
#(<номер задачи>, <название сервера>, <высокий приоритет задачи>)
def task_manager(tasks):
    #этот словарь мы вернем из функции
    server_dict = defaultdict(deque)
    #создаем очередь к серверу
    deq_server = deque()
    
    #пробегаемся по списку с распаковкой каждого кортежа
    for element in tasks:
        num_task, name_server, priority = element
        
        #берем в словаре очередь по ключу-серверу (если его нет автоматом создаться)
        deq_server = server_dict[name_server]        
        #и, смотрим приоретит, если высокий в начало очереди, низкий-конец
        if priority:
            deq_server.appendleft(num_task)     #ставим задачу в начало очереди
        else:
            deq_server.append(num_task)         #ставим задачу в конец очереди
        
        #сохранили в словаре по ключу очередь
        server_dict[name_server] = deq_server
        #конец цикла, переходим на следующую интерацию    
    
    
    #вернули словарь
    return server_dict    
    
    

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})
