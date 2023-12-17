# №2
class Respondent:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
    def __str__(self):
        return f'name:{self.name} + age:{self.age}'

class Groups:
    def __init__(self):
        self.respondents_0_18 = []
        self.respondents_26_35 = []
        self.respondents_46_60 = []
        self.respondents_81_100 = []
        self.respondents_101 = []

    def add_respondent(self, name, age):
        if int(age) <= 18:
            self.respondents_0_18.append(Respondent(name, age))
        elif 26 <= int(age) <= 35:
            self.respondents_26_35.append(Respondent(name, age))
        elif 46 <= int(age) <= 60:
            self.respondents_46_60.append(Respondent(name, age))
        elif 81 <= int(age) <= 100:
            self.respondents_81_100.append(Respondent(name, age))
        elif int(age) >= 101:
            self.respondents_101.append(Respondent(name, age))

    def sorting(self):
        if len(self.respondents_101) > 0:
            self.respondents_101.sort(key=lambda x:(x.age, x.name))
        if len(self.respondents_0_18) > 0:
            self.respondents_0_18.sort(key=lambda x: (x.age, x.name))
        if len(self.respondents_26_35) > 0:
            self.respondents_26_35.sort(key=lambda x: (x.age, x.name))
        if len(self.respondents_46_60) > 0:
            self.respondents_46_60.sort(key=lambda x: (x.age, x.name))
        if len(self.respondents_81_100) > 0:
            self.respondents_81_100.sort(key=lambda x: (x.age, x.name))

    def get_str_mas(self, mass: list):
        result = []
        for el in mass:
            result.append(f'{el.name}, {el.age}; ')
        return ' '.join(result)

    def __str__(self):
        return f'101+: {self.get_str_mas(self.respondents_101)}\n 81-100: {self.get_str_mas(self.respondents_81_100)}\n' \
               f' 46-50: {self.get_str_mas(self.respondents_46_60)}\n 26-35: {self.get_str_mas(self.respondents_46_60)}\n' \
               f' 0-18: {self.get_str_mas(self.respondents_0_18)}'


with open('respondents.txt', encoding="utf-8") as f:
    groups = Groups()
    for respondent in f:
        name, age = respondent.strip().split(',')
        groups.add_respondent(name, int(age))
    groups.sorting()
    print(groups)
f.close()

