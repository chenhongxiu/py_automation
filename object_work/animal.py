#!/usr/bin/env python
# __*__ coding:utf-8 __*__
# @Time : 2021/4/8 9:30 上午
# @Author : shicheju
# @File : animal.py




from work.object_work.get_data import get_aniaml_datas

#定义一个动物类
class Animal:

    #类的属性值
    def __init__(self,name,color,age,gender):
        self.name=name
        self.color=color
        self.age=age
        self.gender=gender

    def crying(self):
        print(f"{self.name} 会叫")

    def running(self):
        print(f"{self.name} 会跑")

class Cat(Animal):

    def __init__(self,name,color,age,gender):
        self.hair="短毛"
        super().__init__(name,color,age,gender)

    def catch_mice(self):
        print(f"{self.name},{self.color},{self.age},{self.gender},{self.hair}，抓到老鼠")

    def crying(self):
        print(f"{self.name},{self.color},{self.age},{self.gender},{self.hair}， 喵喵叫")

class Dog(Animal):

    def __init__(self,name,color,age,gender):
        self.hair="长发"
        super().__init__(name,color,age,gender)

    def housekeeping(self):
        print(f"{self.name},{self.color},{self.age},{self.gender},{self.hair}，会看家")

    def crying(self):
        print(f"{self.name},{self.color},{self.age},{self.gender},{self.hair}， 汪汪叫")

if __name__ == '__main__':
    case_cat=Cat(get_aniaml_datas()[0]['name'],get_aniaml_datas()[0]['color'],get_aniaml_datas()[0]['age'],get_aniaml_datas()[0]['gender'])
    print(case_cat.catch_mice())

    case_dog=Dog(get_aniaml_datas()[1]['name'],get_aniaml_datas()[1]['color'],get_aniaml_datas()[1]['age'],get_aniaml_datas()[1]['gender'])
    print(case_dog.housekeeping())




