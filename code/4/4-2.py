# -*- coding:utf-8 -*-
# 自定义类1

class Charmander:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    
if __name__ == '__main__':
    pokemon1 = Charmander()
    pokemon2 = Charmander()
    pokemon1.setName('Bang')
    pokemon2.setName('Loop')
    pokemon1.getName()
    pokemon2.getName()
