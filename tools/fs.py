import os


def GetFileNameList(FindPath, FlagStr=[]):
    '''''
    #获取目录中指定的文件名
    #>>>FlagStr=['F','EMS','txt'] #要求文件名称中包含这些字符
    #>>>FileList=GetFileList(FindPath,FlagStr) #
    '''
    FileList = []
    AllList = Get_FileTypeList(FindPath)

    if AllList:
        if FlagStr is not None:
            for nameitem in FlagStr:
                pass

    # 对文件名排序
    if (len(FileList) > 0):
        FileList.sort()
    return FileList


def Get_FileTypeList(file_dir, FileType=None):
    # 获取指定文件类型的文件
    filelist = []
    # print(FileType)
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if FileType is None:
                filelist.append(os.path.join(root, file))
            elif os.path.splitext(file)[1] in FileType:
                filelist.append(os.path.join(root, file))
            # print(filelists)
    return filelist


def Get_AllFileTypeList(Path, FileType='*.csv'):
    filelists = []
    for subfile in os.listdir(Path):
        subfile_path = os.path.join(Path, subfile)
        if os.path.isdir(subfile_path):
            filelists.append(Get_FileTypeList(subfile_path))
        elif os.path.splitext(subfile_path)[1] in FileType:
            filelists.append(subfile_path)
    return filelists


if __name__ == '__main__':
    # print(Get_AllFileTypeList('./',FileType=['*.csv','*.py']))
    # print(GetFileNameList('./',FlagStr=['str','con']))
    # print(Get_FileTypeList('./','*.csv'))
    print(Get_FileTypeList('./'))
