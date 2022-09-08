from django.test import TestCase

# Create your tests here.
"""
    Программа для удаления стоп-слов
    из строки используя функцию filter()
"""

# Список стоп-слов
list_of_stop_words = ["в", "и", "по", "за"]

# Строка со стоп-словами
string_to_process = "Сервис по поиску работы и сотрудников HeadHunter опубликовал подборку высокооплачиваемых вакансий в России за август."

# lambda-функция, фильтрующая стоп-слова
split_str = string_to_process.split()
filtered_str = ' '.join((filter(lambda s: s not in list_of_stop_words, split_str)))

print("Отфильтрованная строка:a", filtered_str)