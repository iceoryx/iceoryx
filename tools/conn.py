from sqlalchemy import create_engine


def GetMysqlConn(DBUSER=None, DBPASSWD=None, DBHOST=None, DB=None):
    engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8' % (DBUSER, DBPASSWD, DBHOST, DB))
    return engine


def Getext(Textfile):
    f = open(r"%s" % Textfile)  # txt文件，存储股票代码，一行一个代码，小写字母
    symbols = [line.strip() for line in f.readlines()]
    f.close()
    return symbols


if __name__ == '__main__':
    DBUSER = 'root'
    DBPASSWD = '110110'
    DBHOST = '127.0.0.1'
    DB = 'macro'
