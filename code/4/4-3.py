# -*- coding:utf-8 -*-
# 自定义类2

class Charmander:
    def __init__(self,name,gender,level):
        self.type = ('fire',None)
        self.gender = gender
        self.name = name
        self.level = level
        self.status = [10+2*level,5+1*level,5+1*level,5+1*level,5+1*level,5+1*level]
        # 最大HP,攻击，防御，特攻，特防，速度
    def getName(self):
        return self.name
    def getGender(self):
        return self.gender
    def getType(self):
        return self.type
    def getStatus(self):
        return self.status


if __name__ == '__main__':
    pokemon1 = Charmander('Bang','male',5)
    pokemon2 = Charmander('Loop','female',6)
    print(pokemon1.getName(),pokemon1.getGender(),pokemon1.getStatus())
    print(pokemon2.getName(),pokemon2.getGender(),pokemon2.getStatus())
