import random
from console import *
from modul import *
from text import *
from time import sleep


def start():
    """В этой функции происходят все события от начала игры до самой драки"""
    while True:
        p_com = starting()
        match p_com:
            case 1:
                player_1 = Player(input_data(name_player), input_class())
                player_1.xp_player()
                player_2 = Player(input_data(name_player), input_class())
                player_2.xp_player()
                print_message(player_1.__str__())
                print_message(player_2.__str__())
                f_attack = random.randint(1, 2)
                if f_attack == 1:
                    fight_users(first_attack, player_1.name)
                    fight = Fight(player_1, player_2)
                    while True:
                        fight.attack_p_1()
                        if fight.p_2.xp <= 0:
                            fight_users(win, player_1.name)
                            break
                        else:
                            print(f"У {player_2.name} осталось {fight.p_2.xp} xp")
                            sleep(5)
                        fight.attack_p_2()
                        if fight.p_1.xp <= 0:
                            fight_users(win, player_2.name)
                            break
                        else:
                            print(f"У {player_1.name} осталось {fight.p_1.xp} xp")
                            sleep(5)
                else:
                    fight_users(first_attack, player_2.name)
                    fight = Fight(player_1, player_2)
                    while True:
                        fight.attack_p_2()
                        if fight.p_1.xp <= 0:
                            fight_users(win, player_2.name)
                            break
                        else:
                            print(f"У {player_1.name} осталось {fight.p_1.xp} xp")
                            sleep(5)
                        fight.attack_p_1()
                        if fight.p_2.xp <= 0:
                            fight_users(win, player_1.name)
                            break
                        else:
                            print(f"У {player_2.name} осталось {fight.p_2.xp} xp")
                            sleep(5)
            case 2:
                print_message(game_over)
                break
