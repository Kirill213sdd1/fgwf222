class Employee:

    def __init__(self, name, number, otdel, dol):
        self.name = name
        self.number = number
        self.otdel = otdel
        self.dol = dol

    def __str__(self):
        return f'ФИО: {self.name}, идинтификационный номер: {self.number}, отдел: {self.otdel}, должность: {self.dol}'

pers1 = Employee('Панков Михаил Кириллович', '1231245', 'САОК', 'Очень трудная работа')
pers2 = Employee('Куликов Андрей Ростиславович', '1231969', 'АГД', 'Просиживание штанов')
pers3 = Employee('Куртов Валерий Дмитриевич', '228229', 'АДЦ', 'Изучение Корп культуры')
print(pers1)
print(pers2)
print(pers3)