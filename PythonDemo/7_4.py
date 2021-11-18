import os
count = 0
def findSizeFile(path,size):
    global count
    tuples = os.walk(path)
    for root,dirs,files in tuples:
        for file in files:
            if os.path.getsize(os.path.join(root,file))>size*1024*2014:
                count += 1
                print(u"文件：",os.path.join(root,file),u"大小：",os.path.getsize(os.path.join(root,file)))
path = "D:\\我的文件"
size = 10
findSizeFile(path,size)