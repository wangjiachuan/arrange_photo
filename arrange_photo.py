# -*- coding: gbk -*-  
  
""" 
���ܣ�����Ƭ��������ʱ����й��� 
ʹ�÷��������ű�����Ƭ����ͬһĿ¼��˫�����нű����� 
���ߣ����� 
"""  
  
  
import shutil  
import os  
import time  
import exifread  
  
  
class ReadFailException(Exception):  
    pass  
  
def getOriginalDate(filename):  
    try:  
        fd = open(filename, 'rb')  
    except:  
        raise ReadFailException, "unopen file[%s]\n" % filename  
    data = exifread.process_file( fd )  
    if data:  
        try:  
            t = data['EXIF DateTimeOriginal']  
            return str(t).replace(":",".")[:7]  
        except:  
            pass  
    state = os.stat(filename)  
    return time.strftime("%Y.%m", time.localtime(state[-2]))  
  
   
def classifyPictures(path):  
    for root,dirs,files in os.walk(path,True):  
        dirs[:] = []  
        for filename in files:  
            filename = os.path.join(root, filename)  
            f,e = os.path.splitext(filename)  
            if e.lower() not in ('.jpg','.png','.mp4'):  
                continue  
            info = "�ļ���: " + filename + " "  
            t=""  
            try:  
                t = getOriginalDate( filename )  
            except Exception,e:  
                print e  
                continue  
            info = info + "����ʱ�䣺" + t + " "  
            pwd = root +'\\'+ t  
            dst = pwd + '\\' + filename  
            if not os.path.exists(pwd ):  
                os.mkdir(pwd)  
            print info, dst  
            shutil.copy2( filename, dst )  
            os.remove( filename )  
   
if __name__ == "__main__":  
    path = "."  
    classifyPictures(path)  
