def poisk(hod, sl):
    if str(type(sl)) == "<class 'str'>":
        print(f'Человек найден. Это {sl}')
        exit(0)
    print(answer[hod])
    ans = input()
    if ans not in sl:
        print('Такого человека не существует или данные введены некорректно')
        exit(0)
    poisk(hod + 1, sl[ans])



sete = {'python':{'smoke': {'2005': {'осень': {'blonde': {'blue': 'Яковлев Игорь', 'green': 'Вечеренко Анастасия'}, 'brown': 'Панин Дмитрий'}, 'лето': {'black': 'Закоурцев Андрей', 'blonde': 'Родионов Анатолий'}}},
                  'not smoke': {'2003': 'Малиновский Владимир', '2004': {'весна': {'brown' : 'Олойеде Джибрил', 'black': 'Олойеде Абдуллах Олувасеун'}}, '2005': {'лето': {'blonde': 'Зенин Данил', 'brown': {'brown': 'Савальский Матвей', 'green': 'Петрова Владислав'}}, 'весна': 'полина катунина'}}},
        'c++': {'smoke': 'Кармалитова Екатерина',
                'not smoke': {'2004': 'Седых София', '2005': {'зима': 'Селезнев Иван', 'лето': 'Зубов Алексей'}}}}

answer = ['На каком языке программирует? c++/python',
          'Курит? smoke/not smoke',
          'В каком году родился?',
          'В какое время года родился?',
          'Цвет волос? blonde/brown/black',
          'Цвет глаз? blue/green/brown/black']

print('Программа для поиска человека в группе. Ответьте на несколько вопросов')
poisk(0, sete)