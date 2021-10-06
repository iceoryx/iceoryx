from datetime import datetime

from pandas_datareader import data


def GetStockYahoo(StockList=None, Start=None, End=None):
    if End is None:             End = datetime.now()
    if Start is None:           Start = datetime(End.year - 10, End.month, End.day)
    if StockList is None:      df = data.DataReader('BABA', 'yahoo', Start, End)
    if StockList is not None:      df = data.DataReader(StockList, 'yahoo', Start, End)
    return df


def SaveStockToSql():
    # conn=GetLocalConn('md')
    end = datetime.now()
    start = datetime(end.year - 10, end.month, end.day)
    StockLists = ['JD', 'BABA']
    for stock in StockLists:
        df = GetStockYahoo(stock)
        print(df)
        SaveToSql(df, stock)
        # df.to_sql('%s'%stock.lower(),conn,if_exists='append')


def run():
    SaveStockToSql()


if __name__ == '__main__':
    run()
