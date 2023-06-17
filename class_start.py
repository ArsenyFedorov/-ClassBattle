import random
from console import *
from modul import *
from text import *
from time import sleep


class Start:
    """этот класс это какая то херня которая была сделана на основе файла control.py"""

    def start_game(self):
        """Запускает игру """
        self.p_1 = Player(input_data(name_player), input_class())
        self.p_2 = Player(input_data(name_player), input_class())
        self.p_1.xp_player()
        self.p_2.xp_player()
        print_message(self.p_1.__str__())
        print_message(self.p_2.__str__())
        f_attack = random.randint(1, 2)
        if f_attack == 1:
            fight_users(first_attack, self.p_1.name)
            self.f = Fight(self.p_1, self.p_2)
            while True:
                self.f.attack_p_1()
                if self.f.p_2.xp <= 0:
                    fight_users(win, self.p_1.name)
                    break
                else:
                    print(f"У {self.p_2.name} осталось {self.f.p_2.xp} xp")
                    sleep(5)
                self.f.attack_p_2()
                if self.f.p_1.xp <= 0:
                    fight_users(win, self.p_2.name)
                    break
                else:
                    print(f"У {self.p_1.name} осталось {self.f.p_1.xp} xp")
                    sleep(5)
        else:
            fight_users(first_attack, self.p_2.name)
            self.f = Fight(self.p_1, self.p_2)
            while True:
                self.f.attack_p_2()
                if self.f.p_1.xp <= 0:
                    fight_users(win, self.p_2.name)
                    break
                else:
                    print(f"У {self.p_1.name} осталось {self.f.p_1.xp} xp")
                    sleep(5)
                self.f.attack_p_1()
                if self.f.p_2.xp <= 0:
                    fight_users(win, self.p_1.name)
                    break
                else:
                    print(f"У {self.p_2.name} осталось {self.f.p_2.xp} xp")
                    sleep(5)

    def exit_game(self):
        """Ну тут и так понятно что делает эта функция """
        print_message(game_over)

    def game_progress(self):
        """Эта функция запускает игру"""
        while True:
            p_com = starting()
            match p_com:
                case 1:
                    Start.start_game(self)
                case 2:
                    Start.exit_game(self)
                    break
