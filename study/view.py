# 将一组数字 a,b,c,b,a,d,c,a,a
# 改写成 a,b,c,b_0,a_0,d,c_o,a_1,a_2
old_list = ['a', 'b', 'b', 'a', 'd', 'c', 'a', 'c', 'a']


def method(lis):
    new_list = []
    for i in lis:
        new_list.append(i)
        numb = new_list.count(i)
        if numb > 1:
            length = len(new_list)
            lis[length-1] = lis[length-1] + '_%d' % (numb-2)
    return lis


print(method(old_list))



import unittest

print(unittest.path)










