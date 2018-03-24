# -*- coding:utf-8 -*-
print('''自定义类3''')

class Charmander:
    def __init__(self,name,gender,level):
        self.__type = ('fire',None)
        self.__gender = gender
        self.__name = name
        self.__level = level
        self.__status = [10+2*level,5+1*level,5+1*level,5+1*level,5+1*level,5+1*level]
        # 最大HP,攻击，防御，特攻，特防，速度
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
        self.__status[0]+=1  #HP每级增加2点，其余1点
    def __test(self):
        pass


pokemon1 = Charmander('Bang','male',5)
# print pokemon1.type 程序报错
print(pokemon1._Charmander__type)
print('升级前：',pokemon1.getStatus())
pokemon1.level_up()
print('升级后：',pokemon1.getStatus())

print('-'*70)



for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end=' ')


	
print('''自定义类4''')
	
class Charmander:
    def __init__(self,name,gender,level):
        self.__type = ('fire',None)
        self.__gender = gender
        self.__name = name
        self.__level = level
        self.__status = [10+2*level,5+1*level,5+1*level,5+1*level,5+1*level,5+1*level]
		 # 最大HP,攻击，防御，特攻，特防，速度
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

pokemon1 = Charmander('Bang','male',5)
for info in  pokemon1: # 输出对象全部信息
      print(info, end=' ')
