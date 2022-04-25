"""
Date: 25th April 2022 Monday
Name: Bapatla Sravan
File Desc: String Slicing
"""

x='apartment'
print(x)
print(x[0]) # a
print(x[1]) # p
print(x[2]) # a
print(x[3]) # r
print(x[8]) # t
# print(x[9]) # IndexError: string index out of range

x='apartment'
print(x[1]+x[2]+x[3]+x[4]) # part
print(x[7]+x[6]+x[8]) # net
#print(x[3]+x[9]) #IndexError: string index out of range

x='sravan'
print(x[:])  # sravan
print(x[0:]) # sravan
print(x[1:]) # ravan
print(x[2:]) # avan
print(x[3:]) # van
print(x[4:]) # an
print(x[5:]) # n
print(x[6:]) # blank line
print(x[0:4]) # srav
print(x[2:5]) # ava
print(x[2:3]) # a
print(x[5:1]) # blank line 
print(x[4:3]) # blank line
print(x[:6]) # sravan

x='sravan'
print(x[-1]) # n
print(x[-2]) # a
# print(x[-7]) # IndexError: string index out of range
print(x[:-1]) # srava
print(x[:-4]) # sr
print(x[:-6]) #  blank line 
print(x[2:-4]) # blank line 
print(x[-5:-3]) # ra

