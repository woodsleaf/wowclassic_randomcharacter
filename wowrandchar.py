# Алгоритм создания случайного персонажа в World Warcraft для режима Hardcore
import random

prof = ['Горное дело', 'Снятие шкур', 'Травничество', 'Кузнечное дело', 'Инженерное дело', 'Ювелирное дело', 'Кожевничество', 'Алхимия', 'Портняжное дело', 'Наложение чар']
#             0              1               2               3                  4                  5                6             7               8                 9

fractions = ['Альянс', 'Орда']
#                0        1

all_cls   = ['Воин', 'Паладин', 'Рога', 'Прист', 'Маг', 'Чернокнижник', 'Охотник', 'Друид', 'Шаман']
#              0         1         2       3       4           5            6         7        8

cls_prof = [
    [3,4,5,7,9],   #0 warrior
    [3,4,5,7,9],   #1 paladin
    [3,4,5,6,7,9], #2 rogue
    [3,4,5,7,8,9], #3 priest
    [3,4,5,7,8,9], #4 mage
    [3,4,5,7,8,9], #5 loc
    [3,4,5,6,7,9], #6 hunter
    [3,4,5,6,7,9], #7 druid
    [3,4,5,6,7,9], #8 shaman
]


all_races = ['Человек', 'Дварф', 'Ночной эльф', 'Гном', 'Высший эльф', 'Орк', 'Нежить', 'Таурен', 'Тролль', 'Гоблин']
#                0         1           2           3          4          5       6          7         8         9     

race_cls =  [
    [0,1,2,3,4,5,6], #0 human
    [0,1,6,2,3,4],   #1 dwarf
    [0,6,2,3,7],     #2 night elf
    [0,2,4,5,6],     #3 gnome
    [0,6,2,3,4,1],   #4 high elf
    [0,6,2,8,5,4],   #5 orc
    [0,2,3,4,5,6],   #6 undead
    [0,6,8,7],       #7 tauren
    [0,6,2,3,8,4,5], #8 troll
    [0,6,2,4,5]      #9 goblin
]

race_fraction = [
    [0, 1, 2, 3, 4], #0 alliance
    [5, 6, 7, 8, 9]  #1 orda
]


# Только для рандомизации внешнего вида и выбора созвездия на серверах Sirus
def rnd(x, y):
    return(random.randint(x,y))


def rndc(arr):
    return random.choice(arr)


#Выбор рассы
chosen_r = rndc(all_races)
#print(chosen_r)
raceid = all_races.index(chosen_r)
#print(raceid)


#Выбор класса
chosen_cid = rndc(race_cls[raceid])
chosen_c = all_cls[chosen_cid]
#print(chosen_c)
classid = all_cls.index(chosen_c)
#print(classid)


#Определение фракции
def ask_fraction(chosen_r):
    for items in race_fraction:
        #print(items)
        for item in items:
            if  raceid == item:
                return race_fraction.index(items)


#Выбор первой профессии
listprof = cls_prof[classid]
chosen_pid = rndc(listprof)
chosen_p = prof[chosen_pid]
#print(chosen_p)


# Начало вычислений случайного персонажа
chosen_f = fractions[ask_fraction(chosen_r)]


print(' ' + chosen_f)
print(' ' + chosen_r)
print(' ' + chosen_c)
print(' ' + 'Крутим гачу на вид персонажа: ' + str(rnd(0,20)) + ' раз(а)')
print(' ' + 'Созвездие для WOTLK: ' + str(rnd(-8,8)))
print(' ' + 'Первая профессия: ' + chosen_p + '. Вторую выбираем под первую')
