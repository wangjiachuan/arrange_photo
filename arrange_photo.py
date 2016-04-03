# -*- coding: gbk -*-  
  
""" 
功能：对照片按照拍摄时间进行归类 
使用方法：将脚本和照片放于同一目录，双击运行脚本即可 
作者：冰蓝 
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
            only_name = filename
            filename = os.path.join(root, filename)
            print(only_name)
            f,e = os.path.splitext(filename)  
            if e.lower() not in ('.jpg','.png','.mp4','.3gp'):  
                continue  
            info = "文件名: " + filename + " "
            #print(info)
            t=""  
            try:  
                t = getOriginalDate( filename )  
            except Exception,e:  
                print e  
                continue  
            info = info + "拍摄时间：" + t + " "  
            pwd = root +os.sep+ t  
            dst = pwd + os.sep + only_name  
            if not os.path.exists(pwd ):  
                os.mkdir(pwd)  
            #print (info, dst)
            print("file name is :%s" % (filename))
            print("Destination folder is: %s" % (dst))
            shutil.copy2( filename, dst )  
            os.remove( filename )  
   
if __name__ == "__main__":  
    path = "/home/wjc/Project/arrange_photo"  
    classifyPictures(path)  
