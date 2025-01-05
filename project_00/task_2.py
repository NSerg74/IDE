def find_min_max (in_str):
    #функция предварительной поготовки строки
    def redaction_str(str_input):
        #заменим все запятые на точки
        str_input = str_input.replace(',', '.')
        #по пробелам разделим строку в список
        list_number = str_input.split(' ')
        #список, который будем возвращать
        float_number = []
        for element in list_number:
            if element.isalpha(): #если элемент тип стр, то пропускаем
                continue
            else:
                float_number.append(float(element)) #если нет, то добавляем в новый лист с преобразованием в тип флоат
        return float_number

    answer = redaction_str(in_str)
    return [min(answer), max(answer)]

input_string = input('Введите последовательность чисел: ')
lis_min_max = find_min_max(in_str=input_string)
print(f'Maximum: {lis_min_max[1]}')
print(f'Minimum: {lis_min_max[0]}')