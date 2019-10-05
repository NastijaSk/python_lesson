import random

class Card():
    def __init__(self, name):
        self.name = name
        self._card = self.set_card()
        # print(self._card)
        
    def get_card(self):
        return self._card

    def set_card(self):
        # список из 15 разных чисел и 12 пустых значений ''
        number_1_90 = [i for i in range(1,91)]
        number_1_5 = [number_1_90.pop(random.randint(0, len(number_1_90)-1)) for i in range(5)]
        number_1_5.sort()
        number_2_5 = [number_1_90.pop(random.randint(0, len(number_1_90)-1)) for i in range(5)]
        number_2_5.sort()
        number_3_5 = [number_1_90.pop(random.randint(0, len(number_1_90)-1)) for i in range(5)]
        number_3_5.sort()
        for i in range(4):
            number_1_5.insert(random.randint(0,len(number_1_5)),' ')
            number_2_5.insert(random.randint(0,len(number_2_5)),' ')
            number_3_5.insert(random.randint(0,len(number_3_5)),' ')
        
        crd = []
        crd.insert(0, number_1_5)
        crd.insert(1,number_2_5)
        crd.insert(2,number_3_5)
        return crd
        
    def __str__(self):
        
        st = '{:-^27}'.format(self.name)
        st = st + '\n'
        for i in self._card:
            for j in i:
                st  =st + str(j).rjust(3)
            st  =st +  '\n'
        st = st + '{:-^27}'.format('')
        
        return st
        
        #поиск числа в карточке и его зачеркивание 
    def play(self, number_find):
        for i in range(len(self._card)):
            for j in range(len(self._card[i])):
                if str(number_find) == str(self._card[i][j]):
                    self._card[i][j] = '-'
                    return True # удалось Зачеркнуть
        
        return False # такого числа нет
            
    def count_number_in_card(self):
        cnt = 0
        for i in self._card:
                for j in i:
                    if isinstance(j, int):
                        cnt = cnt + 1
        return cnt


class Game():
    def __init__(self, name, igrok1,igrok2):
        self.name = name
        self.igrok1 = igrok1
        self.igrok2 = igrok2
        
    def play(self):

        number_1_90 = [i for i in range(1,91)]
        
        end = 0 
        
        # for i in range(len(self.igrok1._card)):
        #     for j in range(len(self.igrok1._card[i])):
        #         self.igrok1._card[i][j] = '-'
        # self.igrok1._card[0][0] = 1
        
        while end == 0:
            barr = number_1_90.pop(random.randint(0, len(number_1_90)-1))
            # barr = 1
            while 1 == 1 :
                 
                print('бочонок №', barr)
                print(self.igrok1)
                print(self.igrok2)
                answ = input('del number , y/n ')
                # answ = 'y'
                answ_barr = self.igrok1.play(barr)
                if answ == 'y':
                    print('попытка зачеркнуть')
    
                    if  answ_barr is True:
                        # print(self.igrok1.get_card())
                        if self.igrok1.count_number_in_card() == 0:
                            print(self.igrok1.name, 'выиграл')
                            end =1
                            break
                        break
                    if  answ_barr  is False:
                        print(self.igrok1.name, 'проиграл')
                        end = 1
                        break
                if answ != 'y':
                    if answ_barr is True:
                        print ('Вы не зачеркнули число, которое есть на карточке')
                        print(self.igrok1.name, 'проиграл')
                        end = 1
                        break 
                if  answ != 'y':
                    if answ_barr  is False:
                        # print('Игра продолжается')
                        break
            
                            
            
            if  self.igrok2.play(barr) is True:
                    if self.igrok2.count_number_in_card() == 0:
                        print(self.igrok2.name, 'выиграл')
                        end =1

if __name__ == '__main__':
    gamer = Card('игрок')
    pc =  Card('компьютер')
    
    # print(gamer)
    
    game = Game('Игра 1', gamer, pc)
    game.play()




