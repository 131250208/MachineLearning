# -*- coding:utf-8 -*-

class KeyBoradPatternId(object):

    def __init__(self):

        self._row1 = "qwertyuiop"
        self._row2 = "asdfghjkl"
        self._row3 = "zxcvbnm"
        self.rows = [self._row1,self._row2,self._row3]
        pass

    def isAdjacent(self,x,y):
        (x1,y1) = (-1,-1)
        (x2,y2) = (-1,-1)

        for i in range(len(self.rows)):
            j = self.rows[i].find(x)
            if (j != -1):
                (x1,y1) = (i,j)

            j = self.rows[i].find(y)
            if(j!=-1):
                (x2,y2) = (i,j)

        t = abs( (x2+y2) - (x1+y1) )
        if(t>=0 and t <= 1):
            return True

        return False

        pass

    def isSameRow(self,x,y):

        for row in self.rows:
            if (row.find(x)!=-1 and row.find(y)!=-1):
                return True

        return False

    def isSameRowandcontinues(self, x, y):

        for row in self.rows:
            if (row.find(x) != -1 and row.find(y) != -1):
                if abs(row.find(x) - row.find(y)) == 1:
                    return True

        return False


        pass

    def whichPattern(self, string):#返回输入字符串的键盘模式类型


        if (len(string)<4):
            return "NO_PATTERN"

        samerow = True
        zig_zag = True

        for i in range(len(string)-1):

            if (self.isAdjacent(string[i],string[i+1])):
                samerow = samerow and self.isSameRow(string[i],string[i+1])

                zig_zag = zig_zag and not self.isSameRow(string[i],string[i+1])

            else:
                samerow = samerow and self.isSameRow(string[i],string[i+1])
                if (not samerow):
                    return "NO_PATTERN"



        if (samerow):
            return "SAME_ROW"

        if (zig_zag):
            return "ZIG_ZAG"

        return "SNAKE"

    def isKBPattern(self, string):
        if self.whichPattern(string) == "NO_PATTERN":
            return False
        return True

    #
    # def countcontinous(self,string):
    #
    #     dp = [ 1 ] * len(string)
    #
    #     for i in range(1,len(string)):
    #
    #         if self.isSameRowandcontinues(string[i],string[i-1]):
    #             dp[i] = dp[i-1] + 1
    #         else:
    #             dp[i] = dp[i-1]
    #     return dp[len(string)-1]
    #
    #     pass



#
# keyb = KeyBoradPatternId()
# print(keyb.isKBPattern("qazs"))
