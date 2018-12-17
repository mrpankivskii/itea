def task_2():
    """Cтворіть словник з трьома річками і регіонами, територією яких вони протікають.
    Одна з можливих пар «ключ: значення» - 'Amazon': 'South America'.
    Додайте ще дві пари «річка: регіон» у словник. Виведіть повідомлення із назвами річки і регіону - наприклад,
    «The Amazon runs through South America.» для усіх елементів словника, враховуючи те,
    що у повідомлення у відповідні місця підставляються назви річок і територій.
    ( використати створення функції і метод format )
"""
    dct = {'Amazon': 'South America', 'Dnipro':'Ukraine', 'Nil':'Egipt' }
    for x in dct:
        print("The {} runs throu {} ".format(x, dct[x]))

def task_3():
    """Створіть англо-німецький словник, який називається e2g, і виведіть його на екран.
    Слова для словника: stork / storch, hawk / falke, woodpecker / specht і owl / eule.
    Виведіть німецький варіант слова owl. Додайте у словник, на ваш вибір, ще два слова та їхній переклад.
    Виведіть окремо: словник; ключі і значення словника у вигляді списків.
"""
    e2g = {'strk': 'storch', 'hawk' : 'falke', 'woodpecker' : 'specht', 'owl': 'eule'}
    print(e2g)
    print(e2g['owl'])
    e2g['1'] = '1'
    e2g['2'] = '2'
    print(list(e2g.keys()))
    print(list(e2g.values()))

def task_4():
    """Є словник (продовження на наст слайді):  inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
Спробуйте зробити наступне:
     4a)    Додайте ключ до словника під назвою "pocket".
     4b)    Встановіть значення "pocket" як список, що складається з рядків 'seashell', 'strange berry', і  'lint’
     4с)    Відсортуйте ( .sort ()) елементи зі списку, що зберігаються під ключем  "backpack". ( і надрукуйте)
     4d)    Потім видаліть ("dagger") зі списку предметів, що зберігаються під ключем “backpack".
    4e)     Додайте 50 до числа, збереженого під "gold" ключем. І надрукуйте результат.

"""
    inventory = {
        'gold': 500,
        'pouch': ['flint', 'twine', 'gemstone'],
        'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
        'pocket': ['seashell', 'strange berry', 'lint']}
   # import ipdb; ipdb.set_trace()
    print(sorted(inventory['backpack']))


if __name__ == '__main__':
        task_4()