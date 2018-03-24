print('''变量与赋值''')
x=3
print(x)
# result: 3
print(id(x)) #查看x的内存地址，每次运行都会发生变化
# result: 39011144
x*=2
print(x)
# result: 6
print(id(x)) #再次查看x的内存地址，每次运行都会发生变化，但内存必然会变化
# result: 39011108
