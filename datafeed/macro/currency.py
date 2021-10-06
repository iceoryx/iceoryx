import datetime as datetime

import pandas as pd
import pandas_datareader as web


def GetUsGs(DATATYPE=None):
    import pandas_datareader as pdr
    # tablename='US/GS'
    if DATATYPE is None: return 0

    # if DATATYPE in [1,2,3,5,7,10,15,30]:        gs=pdr.get_data_fred('GS%s'%DATATYPE)
    gs = pdr.get_data_fred('GS%s' % DATATYPE)
    # if gs is no:   return gs
    if gs is not None:      return gs


def GetGdp(COUNTRY=None, Start=None, End=None):
    if COUNTRY is None: COUNTRY = 'CN'
    # 设定经济指标为GDP,国家为中国
    gdpquery = 'ticker=GDP%s' % COUNTRY
    # 设定开始结束时间
    if Start is None:   Start = datetime.datetime(1990, 1, 1)
    if End is None:     End = datetime.datetime.now()
    # 取得中国GDP数据
    df = web.DataReader(gdpquery, 'econdb', start=Start, end=End)
    # gdpcn.to_csv("gdpcn1.csv")
    df.columns = ['GDP%s' % COUNTRY]
    return df


def SaveGsToSql():
    conn = GetLocalConn()  # macro
    dfgs = pd.DataFrame()
    for gs in [1, 2, 3, 5, 7, 10, 20, 30]:
        df = GetUsGs(gs)
        # print(df)
        dfgs = pd.concat([dfgs, df], axis=0)
    print(dfgs)
    dfgs.to_sql('US/GS', conn, if_exists='append')


def SaveGdpToSql():
    conn = GetLocalConn()  # macro
    dfgs = pd.DataFrame()
    for country in ['CN', 'US']:
        df = GetGdp(country)
        # print(df)
        # dfgs=pd.concat([dfgs,df],axis=1)
        df.to_sql(str('GDP%s' % country).lower(), conn, if_exists='append')
    # print(dfgs)
    # dfgs.to_sql('GDP',conn, if_exists='append')


def run():
    # SaveGsToSql()   #美国各期国债
    SaveGdpToSql()  # 中美gdp


if __name__ == '__main__':
    run()
