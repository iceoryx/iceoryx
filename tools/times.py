from datetime import datetime

import pandas as pd


def getdatenow():
    return datetime.today()


def stringtodatetime(str="20210101"):
    # from datetime import datetime
    # datetime_str = '09/19/18 13:55:26'
    datetime_object = datetime.strptime(str, '%Y%m%d')
    # print(type(datetime_object))
    return datetime_object  # printed in default format


def objtodatetime(objs=None):
    # from datetime import datetime
    # datetime_str = '09/19/18 13:55:26'
    for obj in range(0, len(objs) - 1):
        objs[obj] = datetime.strptime(objs[obj], '%Y%m%d')
    # print(type(datetime_object))
    return objs  # printed in default format


def inttodatetime(pdint=None):
    pdint = pd.DataFrame([20211203.0])
    # for item in range(0,len(pdint)):
    # pdint.values[item].


if __name__ == '__main__':
    print(stringtodatetime())
    # print(Gettimenow())
    # print(Getdatenow())
