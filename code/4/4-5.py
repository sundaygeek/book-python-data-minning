# -*- coding:utf-8 -*-
print('''自定义类5''')

class pokemon:
    def __init__(self,name,gender,level,type,status):
        self.__type = type
        self.__gender = gender
        self.__name = name
        self.__level = level
        self.__status = status
        self.__info = [self.__name,self.__type,self.__gender,self.__level,self.__status]
        self.__index = -1
    def getName(self):
        return self.__name
    def getGender(self):
        return self.__gender
    def getType(self):
        return self.__type
    def getStatus(self):
        return self.__status
    def level_up(self):
        self.__status = [s+1 for s in self.__status]
        self.__status[0]+=1  # HP每级增加2点，其余1点
    def __iter__(self):
        print('名字 属性 性别 等级 能力')
        return self
    def __next__(self):
        if self.__index ==len(self.__info)-1:
            raise StopIteration
        self.__index += 1
        return self.__info[self.__index]

class Charmander(pokemon):
    def __init__(self,name,gender,level):
        self.__type = ('fire',None)
        self.__gender = gender
        self.__name = name
        self.__level = level
        # 最大HP,攻击，防御，特攻，特防，速度
        self.__status = [10+2*level,5+1*level,5+1*level,5+1*level,5+1*level,5+1*level]
        pokemon.__init__(self,self.__name,self.__gender,self.__level,self.__type,self.__status)
		
		
pokemon1 = Charmander('Bang','male',5)
print(pokemon1.getGender())
for info in  pokemon1: # 输出对象全部信息
     print(info, end=' ')

print('-'*70)



print('''私有成员无法继承''')

class animal:
    def __init__(self,age):
        self.__age = age
    def print2(self):
        print(self.__age)
class dog(animal):
    def __init__(self,age):
        animal.__init__(self,age)
    def print2(self):
        print(self.__age)
        
a_animal = animal(10)
a_animal.print2()
# result: 10
a_dog = dog(10)
a_dog.print2()
# 程序报错，AttributeError: dog instance has no attribute '_dog__age'
# 如果把self.__age改为self.age，则程序可通过
