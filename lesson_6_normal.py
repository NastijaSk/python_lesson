#coding:utf-8
__author__ = 'ASUS'

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _new_health(self,  uron):
        if self.armor < uron:
            self.health = self.health - uron
        else:
            print('Урон не насен, тк броня больше урона')

    def attack(self):
        self.damage = random.randint(5,10)


class Games:
    def __init__(self, name_games, p, e):
        self.name_game = name_games
        print('Игроки:', p.name, e.name)

    def _play(self, p, e): # один ход одного игрока
        p.attack()
        uron = p.damage
        print(p.name, 'пытается нанести:', uron)
        e._new_health(uron)
        print(e.name, 'новое здоровье:', e.health)

    def start_game(self, p, e ):
        while p.health > 0 and e.health > 0:
            player_go = random.randint(0,1)
            print('\nНовая партия, ходит:', player_go)
            if player_go == 0:
                self._play(p, e)
                if p.health < 0 or e.health < 0:
                    print('Игра окончена')
                    break
                self._play(e, p)
                if p.health < 0 or e.health < 0:
                    print('Игра окончена')
                    break
            else:
                self._play(e, p)
                if p.health < 0 or e.health < 0:
                    print('Игра окончена')
                    break
                self._play(p, e)
                if p.health < 0 or e.health < 0:
                    print('Игра окончена')
                    break


if __name__ =='__main__':
    player = Person('Player', 50, 8, 7)
    enemy = Person('Enemy', 60, 8, 7)

    game_1 = Games('games-1', player, enemy)
    game_1.start_game(player, enemy)