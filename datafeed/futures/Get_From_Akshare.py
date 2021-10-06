import akshare as ak
import pandas as pd
# from tools.conn import *
from tqdm import tqdm


def GetFutures_sql(today="20210927", dbname='akfutures'):
    # get_futures_daily_df = get_futures_daily(start_date="20200105", end_date="20200201", market="INE", index_bar=False)
    # print(get_futures_daily_df)

    try:
        get_dce_daily_df = ak.get_dce_daily(date=today)
        SaveToSql(pd.DataFrame(get_dce_daily_df), '%s' % dbname)
        # print(get_dce_daily_df.head(1))
    except Exception as e:
        print(e)

    try:
        get_cffex_daily_df = ak.get_cffex_daily(date=today)
        SaveToSql(pd.DataFrame(get_cffex_daily_df), '%s' % dbname)
        # print(get_cffex_daily_df.head(1))
    except Exception as e:
        print(e)

    try:
        get_ine_daily_df = ak.get_ine_daily(date=today)
        # print(get_ine_daily_df.head(1))
        SaveToSql(pd.DataFrame(get_ine_daily_df), '%s' % dbname)
    except Exception as e:
        print(e)

    try:
        get_czce_daily_df = ak.get_czce_daily(date=today)
        # print(get_czce_daily_df.head(1))
        SaveToSql(pd.DataFrame(get_czce_daily_df), '%s' % dbname)
    except Exception as e:
        print(e)

    try:
        get_shfe_daily_df = ak.get_shfe_daily(date=today)
        # print(get_shfe_daily_df.head(1))
        SaveToSql(pd.DataFrame(get_shfe_daily_df), '%s' % dbname)
    except Exception as e:
        print(e)


def GetFuturesTocsv(today="20210927", path='../../db/futures/ak/', exchanges=['dce', 'shfe', 'cffex', 'ine', 'czce']):
    # get_futures_daily_df = get_futures_daily(start_date="20200105", end_date="20200201", market="INE", index_bar=False)
    # print(get_futures_daily_df)

    DEBUG = 1
    for exchange in exchanges:
        if exchange in ['dce']:
            try:
                get_dce_daily_df = ak.get_dce_daily(date=today)
                if get_dce_daily_df is not None:
                    pd.DataFrame(get_dce_daily_df).to_csv("%s%s/%s.csv" % (path, exchange, today))
                    if DEBUG: print(today + exchange)

                # pd.DataFrame(get_dce_daily_df).to_csv('dce%s.csv'%today)
                # SaveToSql(pd.DataFrame(get_dce_daily_df), )
                # print(get_dce_daily_df.head(1))
            except Exception as e:
                print(e)

        if exchange in ['cffex']:
            try:
                get_cffex_daily_df = ak.get_cffex_daily(date=today)
                if get_cffex_daily_df is not None:
                    pd.DataFrame(get_cffex_daily_df).to_csv("%s%s/%s.csv" % (path, exchange, today))
                    if DEBUG: print(today + exchange)
                # SaveToSql(pd.DataFrame(get_cffex_daily_df), '%s'%dbname)
                # print(get_cffex_daily_df.head(1))
            except Exception as e:
                print(e)

        if exchange in ['ine']:
            try:
                get_ine_daily_df = ak.get_ine_daily(date=today)
                if get_ine_daily_df is not None:
                    pd.DataFrame(get_ine_daily_df).fillna(0).to_csv("%sine/%s.csv" % (path, today))
                    if DEBUG: print(today + exchange)
                # print(get_ine_daily_df.head(1))
                # SaveToSql(pd.DataFrame(get_ine_daily_df), '%s'%dbname)
            except Exception as e:
                print(e)

        if exchange in ['czce']:
            try:
                get_czce_daily_df = ak.get_czce_daily(date=today)
                if get_czce_daily_df is not None:
                    pd.DataFrame(get_czce_daily_df).to_csv("%sczce/%s.csv" % (path, today))
                    if DEBUG: print(today + exchange)

                # SaveToSql(pd.DataFrame(get_czce_daily_df),'%s'%dbname)
            except Exception as e:
                print(e)

        if exchange in ['shfe']:
            try:
                get_shfe_daily_df = ak.get_shfe_daily(date=today)
                if get_shfe_daily_df is not None:
                    if len(pd.DataFrame(get_shfe_daily_df)):
                        pd.DataFrame(get_shfe_daily_df).to_csv("%sshfe/%s.csv" % (path, today))
                        if DEBUG: print(today + exchange)
                # print(get_shfe_daily_df.head(1))
                # SaveToSql(pd.DataFrame(get_shfe_daily_df),'%s'%dbname)
            except Exception as e:
                print(e)


def GetFuturesTohdf(today="20210927", path='./akfuture.h5', exchanges=['dce', 'shfe', 'cffex', 'ine', 'czce']):
    # get_futures_daily_df = get_futures_daily(start_date="20200105", end_date="20200201", market="INE", index_bar=False)
    # print(get_futures_daily_df)

    DEBUG = 1
    for exchange in exchanges:
        if exchange in ['dce']:
            try:
                df = ak.get_dce_daily(date=today)
                if pd.DataFrame(df).shape[0]:
                    # pd.DataFrame(df).to_csv("%s%s/%s.csv"%(path,exchange,today))
                    pd.DataFrame(df).to_hdf(path, "hdb/futures/ak/%s/%s" % (exchange, today))
                    if DEBUG: print(today + exchange)

                # pd.DataFrame(get_dce_daily_df).to_csv('dce%s.csv'%today)
                # SaveToSql(pd.DataFrame(get_dce_daily_df), )
                # print(get_dce_daily_df.head(1))
            except Exception as e:
                if DEBUG:
                    print('ERROR DT=' + today + exchange)
                    print(e)

        if exchange in ['cffex']:
            try:
                df = ak.get_cffex_daily(date=today)
                if pd.DataFrame(df).shape[0]:
                    # pd.DataFrame(get_cffex_daily_df).to_csv("%s%s/%s.csv"%(path,exchange,today))
                    pd.DataFrame(df).to_hdf(path, "hdb/futures/ak/%s/%s" % (exchange, today))
                    if DEBUG: print(today + exchange)
                # SaveToSql(pd.DataFrame(get_cffex_daily_df), '%s'%dbname)
                # print(get_cffex_daily_df.head(1))
            except Exception as e:
                if DEBUG:
                    print('ERROR DT=' + today + exchange)
                    print(e)

        if exchange in ['ine']:
            try:
                df = ak.get_ine_daily(date=today)
                if pd.DataFrame(df).shape[0]:
                    # pd.DataFrame(get_ine_daily_df).fillna(0).to_csv("%sine/%s.csv"%(path,today))
                    pd.DataFrame(df).to_hdf(path, "hdb/futures/ak/%s/%s" % (exchange, today))
                    if DEBUG: print(today + exchange)
                # print(get_ine_daily_df.head(1))
                # SaveToSql(pd.DataFrame(get_ine_daily_df), '%s'%dbname)
            except Exception as e:
                if DEBUG:
                    print('ERROR DT=' + today + exchange)
                    print(e)

        if exchange in ['czce']:
            try:
                df = ak.get_czce_daily(date=today)
                if pd.DataFrame(df).shape[0]:
                    # pd.DataFrame(get_czce_daily_df).to_csv("%sczce/%s.csv"%(path,today))
                    pd.DataFrame(df).to_hdf(path, "hdb/futures/ak/%s/%s" % (exchange, today))
                    if DEBUG: print(today + exchange)

                # SaveToSql(pd.DataFrame(get_czce_daily_df),'%s'%dbname)
            except Exception as e:
                if DEBUG:
                    print('ERROR DT=' + today + exchange)
                    print(e)

        if exchange in ['shfe']:
            try:
                df = ak.get_shfe_daily(date=today)
                if pd.DataFrame(df).shape[0]:
                    # pd.DataFrame(get_shfe_daily_df).to_csv("%sshfe/%s.csv"%(path,today))
                    pd.DataFrame(df).to_hdf(path, "hdb/futures/ak/%s/%s" % (exchange, today))
                    if DEBUG: print(today + exchange)
                # print(get_shfe_daily_df.head(1))
                # SaveToSql(pd.DataFrame(get_shfe_daily_df),'%s'%dbname)
            except Exception as e:
                if DEBUG:
                    print('ERROR DT=' + today + exchange)
                    print(e)


def Get_All_Futures_Daily(start=2020, end=2020, exchanges=['dce', 'shfe', 'cffex', 'ine', 'czce']):
    for year in tqdm(range(start, end + 1)):
        # print('/****************%s*******************/'%year)
        for month in tqdm(range(1, 13)):
            # print('/****************%s *******************/' % month)
            if month < 10: month = '0' + str(month)
            for day in range(1, 32):
                if day < 10: day = '0' + str(day)
                tday = str(year) + str(month) + str(day)
                print('>>>>>+++++++++++++----------------' + tday + '----------------')
                # GetFuturesTocsv(today='%s'%tday,exchanges=exchanges)
                GetFuturesTohdf(today='%s' % tday, exchanges=exchanges)
                # print('*********************************' + tday + '*************/n')
                # time.sleep(0.1)


def run():
    # macro_china_qyspjg()
    # macro_china_fdi()
    # macro_china_shrzgm()
    # macro_china_cpi_monthly()
    # macro_china_ppi_yearly()
    # macro_china_m2_yearly()

    # Get_All_Futures_Daily(2000,2021,exchanges=['ine','shfe','dce'])
    Get_All_Futures_Daily(2010, 2021)
    # Get_All_Futures_Daily(2000, 2021, exchanges=['dce'])
    # GetFuturesTocsv('20000116',exchanges=['ine','shfe'])
    # for tday in tqdm(range(20210920, 20211001)):
    # GetFuturesTocsv(today='%s' % str(tday))
    # time.sleep(0.5)


if __name__ == '__main__':
    run()
