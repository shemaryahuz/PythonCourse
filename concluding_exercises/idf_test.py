
# for x in enumerate(range(2)):
#     print(x)
#
#
# dct = {(1,2,4): 8, (4,2,1): 10, (1,2): 12}

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def remove(self, value):
#         current = self.head
#         prev = None
#         while current:
#             if current['value'] == value:
#                 if prev:
#                     prev['next'] = current['next']
#                 else:
#                     self.head = current['next']
#                 return True
#             prev = current
#             current = current['next']
#         return False
#
#     def append(self, value):
#         if not self.head:
#             self.head = self.tail = {'value': value, 'next': None}
#         else:
#             self.tail['next'] = {'value': value, 'next': None}
#             self.tail = self.tail['next']
#
#
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# print(ll.remove(2))  # True
# print(ll.remove(4))  # False



# x = ~4
# print(x)

# import math
#
# def foo(a):
#     cnt = 0
#     for i in range (1,int(math.sqrt(a))):
#         if a % i == 0:
#             cnt += 2
#     if a % int(math.sqrt(a)) == 0:
#         cnt += 1
#     return cnt
#
# n = 97
#
# if foo(n) == 2:
#     print(str(n)+" is prime")
# else:
#     print(str(n)+" is not prime")

# a="2a3bd1r"
# for i in range(len(a)-1):
#      if a[i]>='0' and a[i]<='9':
#         for j in range(ord(a[i])-ord('0')):
#             print(a[i+1],end="")


# output: aabbbr

# a="what a wonderful day"
# cnt=0
# if a[0]!=" ":
#     cnt+=1
# for i in range(1,len(a)):
#     if a[i]!=" " and a[i-1]==" ":
#         cnt+=1
# print(cnt)

# output: 4
# the function count the words in the string









# def r(a):
#     b=0
#     while a>0:
#         b*=10
#         b+=a%10
#         a//=10
#     return b
#
#
# def g(a):
#     cnt=0
#     while a>0:
#         cnt+=1
#         a//=10
#     return cnt
#
# # algorithm 1
# def foo1(a,b):
#     c=0
#     a=
#     b=
#     while a>9 or b>9:
#         if a>9:
#             ___(3)__
#             c+=a%10
#         if b>9:
#             c*=10
#             ___(4)__
#         a =
#         b =
#     return c
#
#
# # algorithm 2
# def foo2(a,b):
#     c=0
#     c1= (1)___
#     c2=g(b)
#     a=r(a)
#     b= (2)
#     while c1>0 or c2>0:
#         if c1>0:
#             ___(3)____
#             ___(4)____
#             ___(5)____
#         if c2>0:
#             ___(6)____
#             ___(7)____
#             (8)____
#         a//=10
#         b//=10
#     return c













# def merge(a,b):
#     c=[]
#     i=j=0
#     while i<len(a) or j<len(b):
#
#         if i<len(a) and j<len(b):
#
#             if a[i]<b[j]:
#                 c.append(a[i])
#                 i += 1
#             else:
#                 c.append(b[j])
#                 j += 1
#         elif j < len(b) :
#             c.append(b[j])
#             j += 1
#         else:
#             c.append(a[i])
#             i += 1
#     return c
#
# a1 = [1, 4, 6]
# a2 = [3, 5, 8, 11]
# print(merge(a1, a2))




# def what(bigMat,r,c,smallMat):
#
#     for i in range(len(smallMat)):
#
#         for j in range(len(smallMat)):
#
#             if r+i<len(bigMat) and c+j<len(bigMat[0]):
#
#                 bigMat[i+r][j+c]*=smallMat[i][j]
#
# a=[[1,4,7,3,4],
# [4,5,8,3,2],
# [7,8,9,2,1]
# ]
# b=[[0,0],
# [1,0]
# ]
# what(a,0,1,b)
# print(a)

# output:
# [[1, 0, 0, 3, 4], [4, 5, 0, 3, 2], [7, 8, 9, 2, 1]]


# def f(mat):
#     for i in range(len(mat)):
#         for j in range(i+1,len(mat)):
#             if mat[i][j]!=mat[j][i]:
#                 return False
#     return True

# x = "False"
# print(bool(x))

