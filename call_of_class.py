from example_of_class import Sword as sw

Test = sw('Верный', 1.5,
               'под хват двумя руками')
print(type(Test))

# При создании экземпляра класса str
# нет необходимости указывать имя родительского класса
# Python сам понимает: раз в кавычках — значит, str.
spell = str('Stupefy')

print(spell)