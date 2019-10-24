#猜数字
# import random
#
# a = random.randint(1,101)
# counter = 0
# while True:
#     b = input("请猜测1-100的某个数字：")
#     counter += 1
#     if int(b) == a:
#         print("恭喜你猜中了！")
#         break
#     elif int(b) > a:
#         print("大了")
#     else:
#         print("小了")
#
# print("你一共猜了" + str(counter) + "次")


#九九乘法表

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d * %d = %d" % (j ,i , i * j ),end="\t")
#     print("")
#



#判断是否为素数
# i = int(input("请输入一个数："))
# if i % 2 == 0:
#     print("%d不是素数" % (i))
# else:
#     is_prime = True
#     for j in (1,(i+1)/2):
#         if i % j+1 == 0:
#             is_prime = False
#     if is_prime:
#         print("%d是素数" % (i))
#     else:
#         print("%d不是素数" % (i))

#素数，答案
# from math import sqrt
#
# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)


#最小公倍数和最大公约数,答案
# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     (x, y) = (y, x)         #交换x，y，保证x<y
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break


#打印三角图案
# for i in range(1,7):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")

# for i in range(6,0,-1):
#     for j in range(1,7):
#         if j < i :
#             print(" ",end='')
#         else:
#             print("*",end="")
#     print("")

for i in range(0,5):
    for j in range(1,(6+i)):
        if j < (5-i):
            print(" ",end='')
        else:
            print("*",end='')
    print("")
