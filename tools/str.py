import os


def strmodel(string: str, substr=[',', '$']):
    for sub in substr:
        str = str.replace(sub, "")
    return str


def csvlist(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        print(root)
        for file in files:
            if os.path.splitext(file)[1] == '.csv':
                L.append(os.path.join(root, file))
                print(L)
    return L


def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1] == '.csv':
            list_name.append(file_path)


def char2num(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return DIGITS[s]


def str2int(s):
    from functools import reduce
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


if __name__ == '__main__':
    # df=pd.DataFrame(["6,132.00","$12,45.01"])
    # print(df)
    # print (convert_currency(df))
    # df=file_name('C:/Users/yu3a/PycharmProjects/quandl/db/')
    list_name = []
    listdir('..\\db\\', list_name)
    print(list_name)
