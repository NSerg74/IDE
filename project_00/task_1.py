input_string1 = input('Введите 1-ую последовательность идентификаторов: ')
input_string2 = input('Введите 2-ую последовательность идентификаторов: ')


# мой код

# основная функция
def pure_intersection(str1, str2):
    
    # фунция редактирования преобразования текста в список цифр
    def redaction_str(str_input):
        str_input = str_input.replace(' ', '')      #уберем лшний пробелы
        lst_num = str_input.split(',')
        return lst_num

    # функция на поиск обшибки ввода(должны быть только цифры), если ошибки есть, от возвращаем True
    # если нет -False
    def find_erros(lst):
        # отлов будем делать черз конструкцию try-except
        try:
            for num in lst:  # пробегаемся по листу и "вручную" приводим к типу int
                num = int(num)
                # приведение строковой переменной к типу int вызовет ошибку
                # тип ошибки будет ValueError, вот ее и отловим
        except ValueError as num:
            return True

    # приведем строковыю переменную "в порядок"
    list_num1 = redaction_str(str1)
    list_num2 = redaction_str(str2)
    #print(f'Лист №1 {list_num1}')
    #print(f'Лист №2 {list_num2}')
    
    #посмотри на ошибки, если их нет найдем пересечение
    if find_erros(list_num1) or find_erros(list_num2):
        print('Некорректный ввод')
        return None
    else:
        #приведем к типу int
        list_num1 = list(map(int,list_num1))
        list_num2 = list(map(int,list_num2))
        
        #print(list_num1)
        #print(list_num2)
        #найдем пересечения двух множеств
        set_intersection = set(list_num1).intersection(set(list_num2))   #итоговое множество, это пересечение двух множеств str1 и str2
    return list(set_intersection)

print('Вывод:')
print(pure_intersection(str1=input_string1, str2=input_string2))