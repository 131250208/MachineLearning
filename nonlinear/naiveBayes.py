# -*- coding:utf-8 -*-

#  朴素贝叶斯
class NaiveBayes:

    # 训练数据的向量和s的最后一个分量是分类编号
    def __init__(self, s, train_data):
        self.s = s # 指明各个分量的可取值总数，最后一个是分类
        self.train_data = train_data

    def P_yi(self, yi):

        n = 0
        num_yi = 0
        for vec in self.train_data:
            n += 1
            if vec[-1] == yi:
                num_yi += 1
        return (num_yi + 1) / (n + len(self.s[-1]))

    def P_x1yi(self, x, yi):
        P_x1yi = 1

        for ind, xi in enumerate(x):
            num_xiyi = 0
            num_yi = 0
            for vec in self.train_data:
                if vec[-1] == yi:
                    num_yi += 1
                    if vec[ind] == xi:
                        num_xiyi += 1
            p_xi1yi = (num_xiyi + 1) / (num_yi + len(self.s[ind]))
            print("x" + str(ind+1) + " = " + str(xi) + ", yi = " + str(yi) + ", p = " + str(p_xi1yi))
            P_x1yi *= p_xi1yi

        return P_x1yi

    def get_c(self, x):

        yi_max = -1 # 最大概率的分类
        p_yi_max= 0 # 最可能的分类的概率

        for yi in self.s[-1]:
            p = self.P_x1yi(x, yi) * self.P_yi(yi)
            print(p)
            if p > p_yi_max:
                p_yi_max = p
                yi_max = yi

        return yi_max

if __name__ == "__main__":
    train_data = [(1, "s", -1),
                  (1, "m", -1),
                  (1, "m", 1),
                  (1, "s", 1),
                  (1, "s", -1),
                  (2, "s", -1),
                  (2, "m", -1),
                  (2, "m", 1),
                  (2, "l", 1),
                  (2, "l", 1),
                  (3, "l", 1),
                  (3, "m", 1),
                  (3, "m", 1),
                  (3, "l", 1),
                  (3, "l", -1),]

    s = ((1, 2, 3), ("s", "m", "l"), (-1, 1),)
    nb = NaiveBayes(s,train_data)
    print(u"预测结果是：y = %d " % nb.get_c((2, "s")))