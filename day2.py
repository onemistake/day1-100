#摄氏温度和华氏温度转换，答案
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

#根据半径计算周长和面积
# import math
# radius = float(input("请输入圆的半径："))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius ** 2
# print("圆的周长为：" + str(perimeter))
# print("圆的面积为：" + str(area))


#判断平年闰年
# year = int(input("请输入年份："))
# if year % 100 == 0 :
#     if year % 400 == 0:
#         print("闰年")
#     else:
#         print("平年")
# elif year % 4 == 0 :
#     print("闰年")
# else:
#     print("平年")

#平年闰年答案
# year = int(input("请输入年份："))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("闰年")
# else:
#     print("平年")