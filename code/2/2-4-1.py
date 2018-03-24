print('''创建列表''')
List1 = ['Python',5,0.2]
List2 = ['I','love']
'''通过下标访问列表元素'''
print(List1[0],List2[1],List2[-1])
# result: Python love love
print(List1[0:2],List1[:2]) # 注意子列表不包含List1[2]
# result:['Python', 5] ['Python', 5]
print(List2[:],List2[0:])
# result:['I', 'love'] ['I', 'love']
print('-'*70)



print('''列表方法''')
List1.append(3.1)
print(List1)
# result: ['Python', 5, 0.2, 3.1]
List2.insert(1,'really')
print(List2)
# result: ['I', 'really', 'love']
List1.remove(3.1)
print(List1)
# result: ['Python', 5, 0.2]
print(List1.index(5),List1.count(5))
# result: 1 1
List2.extend(List1)
print(List2)
# result: ['I', 'really', 'love', 'Python', 5, 0.2]
List2.reverse()
print(List2)
# result: [0.2, 5, 'Python', 'love', 'really', 'I']
List3=[1,3,2]
List3.sort()
print(List3)
#r esult: [1,2,3]
print('-'*70)



print('''列表用作栈和队列''')
stack=[7,8,9]
stack.append(10)
stack.append(11)
print(stack)
# result: [7,8,9,10,11]
stack.pop()
print(stack)
# result: [7,8,9,10]
print('-'*70)



'''deque用作队列'''
from collections import deque
queue = deque([7,8,9])
queue.append(10)           # 末尾插入元素10
queue.append(11)          # 末尾插入元素11
print(queue.popleft())                 # 开头弹出元素7
print(queue.popleft())                 # 开头弹出元素8
print(queue)                           
# result: deque([9, 10, 11])
