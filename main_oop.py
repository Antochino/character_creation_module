"""Main part of game prog."""
from random import randint

from graphic_arts.start_game_banner import run_screensaver as annimation

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    """Create main character."""

    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name):
        """Initialize constructor."""
        self.name = name

    def attack(self):
        """Attack basic method."""
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self):
        """Defence basic method."""
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self):
        """Execute special abilities."""
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        """Describe variables."""
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    """Subclass which creates Warrior character."""

    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    """Subclass which creates Mage character."""

    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    """Subclass which creates Healer character."""

    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def start_training(char_class):
    """Принимает на вход имя и класс персонажа.

    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    selected_train = None
    actions = {'attack': char_class.attack, 'defence': char_class.defence,
               'special': char_class.special}

    while selected_train != 'skip':
        selected_train = input('Введи команду: ')
        if selected_train in actions:
            print(actions[selected_train]())
        elif selected_train != 'skip':
            print('Вы ввели бред, попробуйте заново.')
        else:
            return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """Возвращает строку с выбранным классом персонажа."""
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: str = None

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: '
                               'Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        if selected_class in game_classes:
            char_class: Character = game_classes[selected_class](char_name)
            # Вывели в терминал описание персонажа.
            print(char_class)
            approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                                   'или любую другую кнопку, '
                                   'чтобы выбрать другого персонажа ').lower()
            if approve_choice != 'y':
                print('Вы ввели бред. Попробуйте еще раз')
            else:
                return char_class
        


if __name__ == '__main__':
    annimation()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: Character = choice_char_class(char_name)
    print(start_training(char_class))
