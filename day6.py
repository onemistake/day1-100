# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fmn = 1
# for num in range(1, m - n + 1):
#     fmn *= num
# print(fm // fn // fmn)

# def factorial(num):
#     """ 求阶乘"""
#     result = 1
#     for i in range(1,num + 1):
#         result *= i
#     return result
#
# m = int(input("m = "))
# n = int(input("n = "))
# #在计算阶乘时直接调用函数即可
# print(factorial(m) // factorial(n) // factorial(m - n))


# 求最大公约数和最小公倍数
# def factor(x,y):
#     if x > y:
#         (x, y) = (y, x)  # 交换x，y，保证x<y
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
#
# def lcm(x,y):
#     """求最小公倍数"""
#     return x * y // factor(x , y)
#
# m = factor(15,20)
# n = lcm(15,20)
# print(m,n)


#判断一个数是不是回文数
# def is_palindrome(num):
#     """判断是个数是不是回文数"""
#     temp = 0
#     n = num
#     while n > 0:
#         temp = temp * 10 + n % 10
#         n = n // 10
#     return temp == num
# if __name__ == '__main__':
#     num = int(input("请输入一个正整数："))
#     if is_palindrome(num):
#         print("%d是回文数。" % (num))
#     else:
#         print("%d不是回文数" % (num))


#判断一个数是不是素数
import math
from hello import is_palindrome
def is_prime(num):
    '''判断一个数是不是素数'''
    prime = True
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0 :
            prime = False
            break
    return True if num != 1 else False

num = int(input("请输入一个数："))
if is_prime(num) and is_palindrome(num):
    print("%d是一个回文素数！" % (num))
else:
    print("%d不是回文素数" % (num))