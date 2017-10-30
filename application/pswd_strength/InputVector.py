#-*- coding:utf-8 -*-

#密码结构
import re
import random
from nonlinear import naiveBayes

# 返回密码的多样性指数
def get_structure_variety(pswd):
    s_var = {'U': 0, 'L': 0, 'D': 0, 'S': 0,} # 多样性向量

    for i in pswd:
        if i.isdigit():
            s_var['D'] = 1 # 数字
        elif i.isalpha():
            pattern = r'[A-Z]'
            flag = re.match(pattern, i)
            if flag:
                s_var['U'] = 1 # 大写字母
            else:
                s_var['L']  = 1# 小写字母
        else:
            s_var['S'] = 1 # 字符

    goals = 0
    for i in s_var.values(): # 返回多样性指数
        if i == 1 :
            goals += 1
    return goals

# 键盘密码占比
# 日期密码占比
# 拼音单词占比

# 计算编辑距离
def get_eidt_dis(pw1, pw2):
    fine_blank = 1
    fine_rep = 1

    vect1 = [i for i in range(len(pw1) + 1)]
    vect2 = [i + 1 for i in range(len(pw1) + 1)]

    for i, c2 in enumerate(pw2):
        for j, c1 in enumerate(pw1):
            cost_rep = 0 # replace的惩罚值
            if c1 != c2: cost_rep = fine_rep

            vect2[j + 1] = min([vect2[j] + fine_blank, vect1[j + 1] + fine_blank, vect1[j] + cost_rep])

        if i == len(pw2) - 1: break

        # 交替使用list
        vect1 = vect2
        vect2 = [x + 1 for x in range(len(pw1) + 1)]
        vect2[0] = i + 2

    return vect2[-1]

# 返回两个密码的相似度
def get_simularity_degree_pws(pw1, pw2):
    return 1 - get_eidt_dis(pw1, pw2)/(len(pw1) + len(pw2))*2

# 与密码库相似指数
def get_simularity_num(pswd):
    s_num = 0

    file = open("yahoo_pswd")
    while True:
        line = file.readline()
        if line == None or line == "": break

        index = line.split(":")[0]
        code = line.split(":")[1]

        if get_simularity_degree_pws(pswd, code.strip()) >= 0.7: # 如果两个密码相似度大于等于0.7，将它们归为一个相似密码类
            s_num += 1
            print("index: %s, pw: %s" % (index,code))
    return s_num # 返回相似密码类的总数

def get_vector(pswd): # 特征向量定义：（结构多样性指数， 键盘密码占比， 日期密码占比， 拼音单词占比， 与密码库相似指数）
    return

def get_test_data_r():
    t_data = []
    n = 10
    while n:
        t_data.append((random.randint(1,4), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(1,3),random.randint(1,3)))
        n -= 1
    print("test_rd: ")
    print(t_data)

    return t_data

if __name__=="__main__":
    s = ((1, 2, 3, 4), (0, 1), (0, 1), (0, 1), (1, 2, 3), (1, 2, 3))
    train_data = get_test_data_r()

    nb = naiveBayes.NaiveBayes(s, train_data)
    nb.get_c((1, 0, 0, 1, 3))

    print(u"预测结果是：y = %d " % nb.get_c((2, "s")))