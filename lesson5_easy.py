#coding:utf-8
__author__ = 'ASUS'

import sys
import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def new_dir_n(path_file = os.getcwd()):
    for i in range(1,10):
        name = os.path.join(path_file, 'dir_'+str(i))
        try:
            os.mkdir(name)
            print(name, 'Директория создана')
        except FileExistsError:
            print(name, 'Директория уже есть')

def del_dir_n(path_file = os.getcwd()):
    for i in range(1,10):
        name = os.path.join(path_file, 'dir_'+str(i))
        try:
            os.rmdir(name)
            print(name, 'Директория удалена')
        except FileExistsError:
            print(name, 'Не удалось удалить')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def dir_list():
    print([i for i in os.listdir() if os.path.isdir(i)])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file():
    shutil.copy(sys.argv[0], 'copy.py')

#Для NORMAL 2. Просмотреть содержимое текущей папки
def info_dir():
    for i in os.listdir(path="."):
        print(i)

# 4. создать папку
def new_dir(name_dir):
    try:
        os.mkdir(name_dir)
        print(os.path.isdir(name_dir))
        if os.path.isdir(name_dir) :
            print('Папка создана')
        else:
            print('Папки не было, и не создана')
    except FileExistsError:
        print('Папка уже есть')

#3. удаление папки
def remove_dir( name_dir ):
    try:
        os.rmdir(name_dir)
        # shutil.rmtree(name_dir)
        if os.path.isdir(name_dir) is False:
            print('Папка удалена')
        else:
            print('Папка была, но почему-то не удалилась')
    except FileNotFoundError:
        print('Папки для удаления нет')


if __name__ == '__main__':
    print(os.getcwd())
    new_dir_n()
    del_dir_n()
    dir_list()
    copy_file()

