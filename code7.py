#'''''''''''''''''''''''''''MAP''''''''''''''''
num = ["3","5","10"]
num = list(map(int,num))


#for i  in range(len (num)):
#    num[i] = int(num[i])
#    item = int(item)


#num[2] = num[2] + 1
#print(num[2])

#def sq(a):
#    return a*a

#num1 = [1,2,3,4,24,5,5,5,6,]
#square = list(map(num1))
#print(square)

#num1 = [1,2,3,4,24,5,5,5,6,]
#square = list(map(lambda x: x*x,num1))
#print(square)

#def square(a):
#    return a*a

#def cube(a):

#unc = [square,cube]
#num2 = [1,2,3,4,24,5,5,5,6,]
#for i in range(5):
    #val = list(map(lambda x:x(i), func))
    #print(val)

#'''''''''''''''''''''''''FILTER'''''''''''''

#list_1 = [2,3,1,2,3442,2,4,2]

#def is_greater_7(num):
#    return num>7

#gr_than_7 = list(filter(is_greater_7,list_1))
#print(gr_than_7)


#'''''''''''''''REDUCE''''''''''''''''

from functools import reduce

list1 = [1,2,3,4,7]
num = reduce(lambda x,y:x+y, list1 )

#num = 0
#for i in list1:
    #num = num + i
print(num)






