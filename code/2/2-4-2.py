print('''创建字符串''')
str1 = 'learn Python'
print(str1,str1[0],str1[-1]) #输出整个字符串,第一个字符，最后一个字符
print(str1[:6])  #切片

# result:learn
# result:learn Python l n
# str1[0] = 'h' 程序报错，不允许修改字符串
print('-'*70)
print('"Hello,my name is Mike"') #当字符串中双引号，最好用单引号创建
# result:"Hello,my name is Mike"
print('doesn\'t')  #如果用单引号创建有单引号的字符串，字符串中的单引号前加上\
# result:doesn't
print('-'*70)
str2 = '''Python具有丰富和强大的库。它常被昵称为胶水语言，
能够把用其他语言制作的各种模块（尤其是C/C++）很轻松地联结在一起。
常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面），
然后对其中[2]  有特别要求的部分，用更合适的语言改写。
'''
print(str2)
str3 = '''Python具有丰富和强大的库。它常被昵称为胶水语言,\
能够把用其他语言制作的各种模块（尤其是C/C++）很轻松地联结在一起。
常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面），\
然后对其中[2]  有特别要求的部分，用更合适的语言改写。\
'''
print(str3)
# 输出太长这里就不展示了，请读者动手运行感受str2与str3的不同
print('-'*70)



print('E:\note\Python.doc')  #\n会被当作换号符处理
# result:E:
#       ote\Python.doc
print(r'E:\note\Python.doc') #字符串前加r，所以特殊字符失效
# result:E:\note\Python.doc
print('-'*70)



str4 = 'String\t' 
str5 = 'is powerful'
str4 = str4+str5
# 不会报错，实际上这不是修改str4，而是先消去现有的str4，再用'+'返回的新的合并后的字符串去重新创建str4
print(str4)
# result:String	 is powerful
print('-'*70)
format_str1 = 'There are %d apples %s the desk.' # %d表示整数而%s表示字符串
a_tuple = (2,'on')
print(format_str1 % a_tuple)
# result:There are 2 apples on the desk.
format_str2 = 'There are {0} apples {1} the desk.'.format(3,'on')
print(format_str2)   # 这是另一种写法，更简便
# result:There are 3 apples on the desk.
print('-'*70)



print('''字符串方法''')
str6 = "Zootopia"
print(str6.find('to'))# 返回第一个to的索引，注意str6[3]='t',str6[4]='o'
# result：3
print('-'*70)
str6_2 = "Z o o t o p i a"
print(str6_2.split()) # 利用空格符分隔开字符
# result: ['Z', 'o', 'o', 't', 'o', 'p', 'i', 'a']
print(''.join(str6_2.split())) # 再通过join函数又可以还原
# result: Zootopia
print('-'*70)
str7 = '54321'
print('>'.join(str7)) # 上一个例子是列表的join，这个是字符串的join,功能类似
# result: 5>4>3>2>1
print('-'*70)
str8 = '"Yes!",I answered.'
print(str8.split(','))# split()可以指定一个字符作为分隔符
# result:['"Yes!"', 'I answered.']
# 如果想把多个字符作为分隔符，可用下面这个方法
sep=['!',',','.','"']
for i in sep:
    str8 = str8.replace(i,' ')# 将全部分隔符替换为空格
print(str8.split()) # 成功提取句子中的所有单词
# result:['Yes', 'I', 'answered']
print('-'*70)
str9 = 'A apple'
print(str9.count('A')) #注意区分大小写
# result: 1
str9 = str9.lower()
print(str9.count('a'))
# result: 2
print('-'*70)
str10 = '12345'
print(str10.isalnum())
# result: True
print('-'*70)



print('''Unicode字符串''')
unicode_str =  '\u4f60\u597d'
print(unicode_str) #"你好"的Unicode编码
# result: 你好
utf8_str = unicode_str.encode('utf-8')
print(utf8_str)
# 注意'你好'的utf-8编码为'\xe4\xbd\xa0\xe5\xa5\xbd'(在Python Shell中直接输入utf8_str会显示这个编码)，
# 但是print()函数不会自动解码，所以直接输出为乱码
print(utf8_str.decode('utf-8'))
# result: 你好
print(str(utf8_str,'utf-8')) #这两种方法一样
# result: 你好
