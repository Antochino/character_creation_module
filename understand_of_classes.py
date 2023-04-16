class MeleeWeapon:

    def __init__(self, name):
        self.name = name
        self.strength = 100
    
    # Метод родительского класса.
    def slashing_blow(self):
        # При рубящем ударе уменьшаем прочность меча на 10.
        self.strength -= 10
        return f'Нанесён рубящий удар оружием {self.name}.'
    
    def sharpen(self):
        self.strength = 100
        return (f'Оружие "{self.name}" заточено.')

class Sword(MeleeWeapon):

    # Переопределяем метод родительского класса...
    def slashing_blow(self):
        # ...меняем значение снижения прочности...
        self.strength -= 5
        # ...и меняем сообщение.
        return f'Мечом {self.name} был нанесен рубящий удар.'
    
# Этот класс-наследник полностью наследует все методы и свойства
# родительского класса.

class Axe(MeleeWeapon):

    def __init__(self, name, material):
        super().__init__(name)
        self.material = material
   
    # Объявляем собственный для класса Axe метод.
    def slashing_blow(self):
        # Описываем логику работы метода дочернего класса.
        print('СОКРУШИТЕЛЬНЫЙ УДАР!')
        # Возвращаем результат выполнения метода slashing_blow() в родительском классе.
        return super().slashing_blow()  

test = MeleeWeapon('Test')
brodex = Axe('The best', 'Iron')
xiphos = Sword('Not good')

print(brodex.strength)
print(xiphos.strength)
print(brodex.slashing_blow())
print(xiphos.slashing_blow())
print(xiphos.strength)
a = 'fdfsdfsd'
print(type(a))
print(type(test))

