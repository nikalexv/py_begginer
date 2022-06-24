from lesson3 import LevenshteinDistance

Strings = '''Агафья
Агнесса
Аида
Айгуль
Алина
Алла
Анжелика
Ассоль
'''.split('\n')

y = 'Алексей'

if __name__ == "__main__":
    for x in Strings:
        print(x, y, LevenshteinDistance(x,y))
