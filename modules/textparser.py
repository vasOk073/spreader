def parser(filename: str): # объявляем функцию parser
    file = open(filename,encoding="utf-8", mode="r+") # открываем файл со строчным типом данных,кодировкой utf-8 и режимом r+
    slovar = list(file.readlines()) # создаём словарь
    file.close() # закрываем файл
    itog = list() # создаём лист
    for line in slovar: # Пример работы функции for line,читающей словарь построчно
        itog.append(line.split()) # добавялем в лист наши строки
    return itog # возвращаем список

