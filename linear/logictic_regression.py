#-*- coding:utf-8 -*-

import math

positive = ((1,1,1), (1,2,1), (2,2,1), (1,0,1))
negtive = ((4,5,1), (5,6,1), (6,7,1), (6,6,1))

w1, w2, w0 = 0, 0, 0
w = [w1, w2, w0]
a = 1

def fun(x):
    res = 0
    for i,d in enumerate(w):
        res += w[i] * x[i]
    return res

def sigmoid(y):
    return 1/(1 + math.exp(-y))

def h(x):
    return sigmoid(fun(x))

def iter_w(times):

    for t in range(times):
        gradient = [0 * i for i in positive[0]]# 初始化为全0

        # 正例样本
        for x in positive:
            c = 1 - h(x)
            x_ = x
            x_ = [c * i for i in x]

            for ind, xi in enumerate(x_):# 累加得梯度
                gradient[ind] += xi

        # 负例样本
        for x in negtive:
            c = 0 - h(x)
            x_ = x
            x_ = [c * i for i in x]

            for ind, xi in enumerate(x_):  # 累加得梯度
                gradient[ind] += xi

        # 所有分量上升一个梯度
        for ind, wi in enumerate(w):
            w[ind] += a * gradient[ind]

if __name__ == "__main__":
    iter_w(1000)
    print(w) # 输出参数

    # 对训练数据集对分类
    for x in positive:
        if h(x) > 0.5:
            print(1 , u" : 正例")
        else: print(0 , u" : 负例")

    for x in negtive:
        if h(x) > 0.5:
            print(1 , u" : 正例")
        else: print(0 , u" : 负例")