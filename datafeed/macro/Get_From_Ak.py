import akshare as ak
import pandas as pd


def a():
    import akshare as ak
    macro_cnbs_df = ak.macro_cnbs()
    print(macro_cnbs_df)
    SaveToSql(macro_cnbs_df, 'macro_cnbs')


def macro_china_qyspjg():  # 企业商品价格指数
    import akshare as ak
    macro_china_qyspjg_df = ak.macro_china_qyspjg()
    SaveToSql(macro_china_qyspjg_df, 'macro_china_qyspjg')
    print(macro_china_qyspjg_df)


def macro_china_fdi():  # 外商直接投资
    import akshare as ak
    macro_china_fdi_df = ak.macro_china_fdi()
    SaveToSql(macro_china_fdi_df, 'macro_china_fdi', 'macro')
    print(macro_china_fdi_df)


def macro_china_shrzgm():  # 社会融资规模增速
    import akshare as ak
    macro_china_shrzgm = ak.macro_china_shrzgm()
    SaveToSql(macro_china_shrzgm, 'macro_china_shrzgm', 'macro')
    print(macro_china_shrzgm)


def b():
    a()


def macro_china_m2_yearly():
    import akshare as ak
    macro_china_m2_yearly = ak.macro_china_m2_yearly()
    print(macro_china_m2_yearly)
    print(macro_china_m2_yearly.name)

    macro_china_m2_yearly = pd.DataFrame(macro_china_m2_yearly)
    macro_china_m2_yearly['Date'] = macro_china_m2_yearly.index

    print(macro_china_m2_yearly)
    # print(macro_china_ppi_yearly_df.name)
    SaveToSql(macro_china_m2_yearly, 'macro_china_m2_yearly', 'macro')


def macro_china_ppi_yearly():
    import akshare as ak
    macro_china_ppi_yearly_df = ak.macro_china_ppi_yearly()

    macro_china_ppi_yearly_df = pd.DataFrame(macro_china_ppi_yearly_df)
    macro_china_ppi_yearly_df['Date'] = macro_china_ppi_yearly_df.index

    print(macro_china_ppi_yearly_df)
    # print(macro_china_ppi_yearly_df.name)
    SaveToSql(macro_china_ppi_yearly_df, 'macro_china_ppi_yearly', 'macro')


def macro_china_cpi_monthly():
    import akshare as ak
    macro_china_cpi_monthly = ak.macro_china_cpi_monthly()
    macro_china_cpi_monthly = pd.DataFrame(macro_china_cpi_monthly)
    macro_china_cpi_monthly['Date'] = macro_china_cpi_monthly.index
    print(macro_china_cpi_monthly)

    print(macro_china_cpi_monthly.shape)
    SaveToSql(macro_china_cpi_monthly, 'macro_china_cpi_monthly', 'macro')


def GetFutures_sql(today="20210927"):
    # get_futures_daily_df = get_futures_daily(start_date="20200105", end_date="20200201", market="INE", index_bar=False)
    # print(get_futures_daily_df)

    dbname = 'futures_day'
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


def GetFuturesTocsv(today="20210927"):
    # get_futures_daily_df = get_futures_daily(start_date="20200105", end_date="20200201", market="INE", index_bar=False)
    # print(get_futures_daily_df)

    path = './db/'
    try:
        get_dce_daily_df = ak.get_dce_daily(date=today)
        if get_dce_daily_df is not None:
            pd.DataFrame(get_dce_daily_df).to_csv("%sdce/%s.csv" % (path, today))

        # pd.DataFrame(get_dce_daily_df).to_csv('dce%s.csv'%today)
        # SaveToSql(pd.DataFrame(get_dce_daily_df), )
        # print(get_dce_daily_df.head(1))
    except Exception as e:
        print(e)

    try:
        get_cffex_daily_df = ak.get_cffex_daily(date=today)
        if get_cffex_daily_df is not None:
            pd.DataFrame(get_cffex_daily_df).to_csv("%scffex/%s.csv" % (path, today))
        # SaveToSql(pd.DataFrame(get_cffex_daily_df), '%s'%dbname)
        # print(get_cffex_daily_df.head(1))
    except Exception as e:
        print(e)

    try:
        get_ine_daily_df = ak.get_ine_daily(date=today)
        if get_ine_daily_df is not None:
            pd.DataFrame(get_ine_daily_df).fillna(0).to_csv("%sine/%s.csv" % (path, today))
        # print(get_ine_daily_df.head(1))
        # SaveToSql(pd.DataFrame(get_ine_daily_df), '%s'%dbname)
    except Exception as e:
        print(e)

    try:
        get_czce_daily_df = ak.get_czce_daily(date=today)
        if get_czce_daily_df is not None:
            pd.DataFrame(get_czce_daily_df).to_csv("%sczce/%s.csv" % (path, today))
        # print(get_czce_daily_df.head(1))
        # SaveToSql(pd.DataFrame(get_czce_daily_df),'%s'%dbname)
    except Exception as e:
        print(e)

    try:
        get_shfe_daily_df = ak.get_shfe_daily(date=today)
        if get_shfe_daily_df is not None:
            pd.DataFrame(get_shfe_daily_df).to_csv("%sshfe/%s.csv" % (path, today))
        # print(get_shfe_daily_df.head(1))
        # SaveToSql(pd.DataFrame(get_shfe_daily_df),'%s'%dbname)
    except Exception as e:
        print(e)


def Get_All_Futures_Daily(start=2020, end=2020):
    for year in range(start, end + 1):
        print('/****************%s*******************/' % year)
        for month in range(1, 13):
            print('/****************%s *******************/' % month)
            if month < 10: month = '0' + str(month)
            for day in range(1, 32):
                if day < 10: day = '0' + str(day)
                tday = str(year) + str(month) + str(day)
                print('>>>>>+++++++++++++----------------' + tday + '----------------')
                GetFuturesTocsv(today='%s' % tday)
                print('*********************************' + tday + '*************')


def run():
    # macro_china_qyspjg()
    # macro_china_fdi()
    # macro_china_shrzgm()
    # macro_china_cpi_monthly()
    # macro_china_ppi_yearly()
    # macro_china_m2_yearly()

    Get_All_Futures_Daily(2013, 2014)
    # GetFuturesTocsv('20210928')


if __name__ == '__main__':
    run()
