import numpy as np
import math
# define aim function


def cos(vector):
    for i in range(100):
        vector[i] = math.cos(vector[i])
    return vector


def aimfuc(variables, LegV):
    # # 测试函数1
    # x = np.zeros((30, 100, 1))
    # for i in range(30):
    #     x[i] = variables[:, [i]]
    #
    # f = 0
    # for i in range(29):
    #     f = f + (100*(pow(x[i+1]**2-x[i], 2)) + pow((x[i+1]-1), 2))
    # 测试函数2
    # x = np.zeros((30, 100, 1))
    # for i in range(30):
    #     x[i] = variables[:, [i]]
    # f = 0
    # pi = math.pi
    # for i in range(30):
    #
    #     f = f + (x[i]**2 - 10*cos(2 * pi * (x[i])) + 10)
    # # 测试函数3
    x = np.zeros((30, 100, 1))
    for i in range(30):
        x[i] = variables[:, [i]]

    f_1 = 0
    f_2 = 1
    for i in range(30):
        f_1 = f_1 + ((x[i]**2) / 4000)
        f_2 = f_2 * (cos(x[i])/((i+1)**0.5) + 1)

    f = f_1 + f_2

    return [f, LegV]  # 对结果进行转置，使目标函数值矩阵符合Geatpy数据结构
