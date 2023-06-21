from random import choice, randint


class Player:
    """Этот класс создаёт война по требованию пользователя"""
    def __init__(self, name: str, p_class: int):
        self.name = name
        self.p_class = p_class
        self.xp = 0

    def xp_player(self):
        if self.name == "Stoyn":
            self.xp = 666
        elif self.p_class == 1:
            self.xp = 125
        elif self.p_class == 2:
            self.xp = 65
        else:
            self.xp = 100

    def __str__(self):
        return f"Имя {self.name}, класс - {self.p_class}, {self.xp}xp"


class Fight:
    """Этот класс заставляет драться двух войнов"""
    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2

    def attack_player(self, p_1, p_2):
        if p_2.p_class == 3:
            if randint(1, 2) == 1:
                print(f"{p_2.name} Увернулся")
                return ""
        if p_1.p_class == 1:
            damage = randint(15, 30)
            p_2.xp -= damage
            print(f"{self.p_1.name} Снёс {damage}xp")
        elif p_1.p_class == 2:
            damage = randint(30, 50)
            p_2.xp -= damage
            print(f"{p_1.name} Снёс {damage}xp")
        else:
            damage = randint(10, 25)
            p_2.xp -= damage
            print(f"{p_1.name} Снёс {damage}xp")
