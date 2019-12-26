"""
@Author: Yaodecheng
@Date: 2019-12-12 18:09:51
@LastEditors: Yaodecheng
"""
import math

# 方法1，关键词：条件判断
def abs_value1(x):
    if x > 0.0:
        return x
    else:
        return -x


# 方法2，关键词：内置函数
def abs_value2(x):
    return abs(x)


# 方法3，关键词：内置模块
def abs_value3(x):
    return math.fabs(x)


# 写完3种方法后，验证一下吧。
if __name__ == "__main__":

    x = -5.20
    print(abs_value1(x))
    print(abs_value2(x))
    print(abs_value3(x))
