import re

class DateId(object):
    def __init__(self, s):
        s = re.sub("[^0-9]","",s)
        self.__target = s
        self.__length = len(s)

    def checkDate(self):
        if self.__length == 6:
            start = int(self.__target[0:2])
            end = int(self.__target[4:6])
            # yymmdd | mmddyy | ddmmyy
            if start > 31:
                if self.__check_mmdd(self.__target[2:6]):
                    return True, "yymmdd"
                elif self.__check_ddmm(self.__target[2:6]):
                    return True, "yyddmm"
                else:
                    return False, None
            elif end > 31:
                if self.__check_mmdd(self.__target[0:4]):
                    return True, "mmddyy"
                elif self.__check_ddmm(self.__target[0:4]):
                    return True, "ddmmyy"
                else:
                    return False, None
            else:
                return  False, None
        elif self.__length == 8:
            # yyyymmdd | mmddyyyy | ddmmyyyy
            start = int(self.__target[0:4])
            end = int(self.__target[4:8])
            if 1931 < start <= 2099:
                if self.__check_ddmm(self.__target[4:8]):
                    return True, "yyyyddmm"
                elif self.__check_mmdd(self.__target[4:8]):
                    return  True, "yyyymmdd"
                else:
                    return  False, None
            elif 1931 < end <= 2099:
                if self.__check_ddmm(self.__target[0:4]):
                    return True, "ddmmyyyy"
                elif self.__check_mmdd(self.__target[0:4]):
                    return True, "mmddyyyy"
                else:
                    return False, None
            else:
                return False, None
        else:
            return False, None

    def __check_mmdd(self,data):
        mm = int(data[0:2])
        dd = int(data[2:4])
        return 1 <= mm <= 12 and 1<= dd <= 31

    def __check_ddmm(self,data):
        mm = int(data[2:4])
        dd = int(data[0:2])
        return 1 <= mm <= 12 and 1<= dd <= 31

# if __name__ == "__main__":
#     data = "ew102419..95^^"
#     iden = DateId(data)
#     print(iden.checkDate())
