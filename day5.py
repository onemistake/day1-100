#寻找水仙花数。
#说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和
# 正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。

# for i in range(100,1000):
#     a = i // 100
#     b = (i - 100*a) // 10
#     c = i - 100*a - 10*b
#     if i == a**3 + b**3 + c**3:
#         print(i)
#
#寻找水仙花，答案
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

#正整数反转,答案
# num = int(input("请输入一个正整数："))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print("该正整数的反转为：%d" % (reversed_num))

#百钱白鸡（穷举法，暴力搜索法）
# exist = False
# for x in range(0,20):
#     for y in range(0,33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print("公鸡%d只，母鸡%d只，小鸡%d只" % (x,y,z))
#             exist = True
# if exist == False:
#     print("无法做到百钱买百鸡")

#Craps赌博游戏
# import random
# money = 1000
# i = 0
# print("你拥有资金：1000")
# while money > 0:
#     # debt = int(input("请输入本局赌注："))
#     debt = 100
#     c = random.randint(1,6) + random.randint(1,6)
#     i += 1
#     print("玩家摇出了%d点" % (c))
#     if c == 7 or c == 11:
#         money += debt
#         print("你赢了，资金现有%d" % (money))
#     elif c == 2 or c == 3 or c == 12:
#         money -= debt
#         print("你输了，资金现有%d" % (money))
#     else:
#         while True:
#             d = random.randint(1,6) + random.randint(1,6)
#             i += 1
#             print("玩家摇出了%d点" % (d))
#             if d == 7:
#                 money -= debt
#                 print("你输了，资金现有%d" % (money))
#                 break
#             elif d == c:
#                 money += debt
#                 print("你赢了，资金现有%d" % (money))
#                 break
#             else:
#                 pass
# print("你破产了，游戏结束！")
# print(i)

#CRAPS读博游戏，答案
# from random import randint
#
# money = 1000
# while money > 0:
#     print('你的总资产为:', money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注: '))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('玩家摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜!')
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % current)
#         if current == 7:
#             print('庄家胜')
#             money -= debt
#         elif current == first:
#             print('玩家胜')
#             money += debt
#         else:
#             needs_go_on = True
# print('你破产了, 游戏结束!')


# 斐波那契数列前20个（说明：斐波那契数列（Fibonacci sequence），又称黄金分割数列，是意大利数学家
# 莱昂纳多·斐波那契（Leonardoda Fibonacci）在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，
# 所以这个数列也被戏称为"兔子数列"。斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，
# 每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13,
# i = 1
# j = 1
# n = 2
# Fib = []
# Fib.append(i)
# Fib.append(j)
# while n < 20:
#     i += j
#     Fib.append(i)
#     (i ,j) = (j , i)
#     n += 1
# print(Fib)


#1000以内的完美数。
#说明：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
# 例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。
# perfect_number = []
# for i in range(2,10000):
#     list = []
#     for j in range(1,(i // 2) + 1):
#         if i % j == 0:
#             list.append(j)
#     if sum(list) == i:
#         perfect_number.append(i)
# print(perfect_number)


#100以内所有的素数
import math
primes = []
for i in range(2,100):
    is_prime = True
    for j in range(2,int(i / 2)):
        if i % j == 0 :
            is_prime = False
            break
    if is_prime:
        primes.append(i)
print(primes)