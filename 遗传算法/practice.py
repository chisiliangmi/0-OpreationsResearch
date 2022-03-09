""" main.py """

import numpy as np

import geatpy as ga


# 获取目标函数地址

AIM_M = __import__('main')

# 变量设置

# 测试函数1
# vector_x = np.zeros((30, 2))
# vector_b = np.zeros((30, 2))
# for i in range(30):
#
#     vector_x[i] = [-30, 30]
#     vector_b[i] = [1, 1]
# 测试函数2
# vector_x = np.zeros((30, 2))
# vector_b = np.zeros((30, 2))
# for i in range(30):
#
#     vector_x[i] = [2.56, 5.12]
#     vector_b[i] = [1, 1]
# 测试函数3
vector_x = np.zeros((30, 2))
vector_b = np.zeros((30, 2))
for i in range(30):

    vector_x[i] = [300, 600]
    vector_b[i] = [1, 1]

ranges = vector_x.T  # 生成自变量的范围矩阵

borders = vector_b.T  # 生成自变量的边界矩阵

FieldDR = ga.crtfld(ranges, borders)  # 生成区域描述器

# 调用Geatpy内置进化算法模板

[pop_trace, var_trace, times] = ga.sga_new_real_templet(AIM_M, 'aimfuc', None, None, FieldDR, problem='R', maxormin=1,
                                                        MAXGEN=1000, NIND=100, SUBPOP=1, GGAP=0.5, selectStyle='tour',
                                                        recombinStyle='xovdp', recopt=0.9, pm=0.02, distribute=True,
                                                        drawing=1)
