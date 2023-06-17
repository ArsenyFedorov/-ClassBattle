from text import *


def starting():
    print(start_game)
    p_com = input(user_comand).strip()
    if p_com.isdigit() and 0 < int(p_com) < 3:
        return int(p_com)
    else:
        print_message(command_error)


def print_message(message):
    print("=" * len(message))
    print(message)
    print("=" * len(message))


def input_data(message: str) -> str:
    while True:
        print("=" * len(message))
        data = input(message).strip()
        print("=" * len(message))
        if data:
            return data
        print_message(input_error)


def input_class() -> int:
    while True:
        print(person_class)
        u_class = input(user_comand).strip()
        if u_class.isdigit() and 0 < int(u_class) < 5:
            if int(u_class) == 4:
                print(person_head)
            else:
                return int(u_class)
        else:
            print_message(class_error)


def fight_users(message: str, name: str):
    print(message + name)

