# coding: utf-8
__author__ = 'ASUS'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

#способ 1
ls=["яблоко", "банан", "киви", "арбуз", "груша"]
for i in range(len(ls)):
    print('{} {:>15}'.format(str(i+1)+'.', ls[i]))

#способ 2
max_ls = 0
for i in range(len(ls)):
    if len(ls[i])> max_ls:
        max_ls = len(ls[i])
print(max_ls)
#max_ls = len (max(ls, key = len))

for i in range(len(ls)):
    # print(ls[i].rjust(max_ls+1, ' '))
    print('{}{}'.format(str(i+1)+'.', ls[i].rjust(max_ls+1, ' ')))

#или
for index, item in enumerate(ls, start=1):
    print(index, item)

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

b = ['a', 'b', 'c', 'd', '1', '2']
a = ['b', 'd', '2', '5']
с = []
for i in b:
    if i in a: #while лучше если есть повторы
      a.remove(i)

print('из a убрали элементы b = {}'.format(a))


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
a = [1, 2, 3, 4, 12, 7, 19, 2, 10]
b = []
for i in a:
    if i%2==0:
        b.append(i/4)
    else:
        b.append(i*2)
print(b)