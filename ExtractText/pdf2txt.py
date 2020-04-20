import os,fnmatch
from win32com import client as wc
from win32com.client import Dispatch, gencache


'''
功能描述：pdf文件转化txt文本
参数描述：1 filePath：文件路径  2 savePath： 指定保存路径
'''
def Pdf2Txt(filePath,savePath=''):
    print(filePath)

    # 1 切分文件上级目录和文件名
    dirs,filename = os.path.split(filePath)

    # 2 修改转化后的文件名
    new_name = ''
    if fnmatch.fnmatch(filename,'*.pdf'):
        new_name = filename[:-4]+'.txt'
    else:
        print('格式不正确，仅支持pdf格式。')
        return

    # 3 文件转化后的保存路径
    if savePath=='': 
        savePath = dirs
    else: 
        savePath = savePath
    pdf_to_txt = os.path.join(savePath,new_name)
    print(pdf_to_txt)

    # 4 加载处理应用,pdf转化txt
    wordapp = wc.Dispatch('Word.Application')
    mytxt = wordapp.Documents.Open(filePath)
    mytxt.SaveAs(pdf_to_txt,4)
    mytxt.Close()



if __name__=='__main__':
    filePath=os.path.abspath(r'./为何我的属下不愿意改变.pdf')
    Pdf2Txt(filePath)