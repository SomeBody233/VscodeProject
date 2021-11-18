f = open('C:\\Users\\soulzgd\\Desktop\\1.txt','r+',encoding='utf-8')
 
ls = f.readlines()                 #此时读取指针已到了文本末尾
 
lineupdate = str()              
lsupdate = list()
 
for line in ls:
    for i in line:
        if i.islower():             # str.islower()判断一个字符是否是小写字母
            i = i.upper()           # str.upper() 将小写字母转换成大写字母
        elif i.isupper():
            i = i.lower()
 
        lineupdate += i              # 生成新的字符串
    lsupdate.append(lineupdate)      # 将新生成的字符串追加到列表中
    lineupdate = ''                  # 清空lineupdate的内容
 
f.seek(0)                            # 将指针移动到文本头部
f.writelines(lsupdate)               # 将数组写入文本中，此时指针已经移动到文本末尾
 
f.seek(0)                            # 再次将指针移动到文本头部
print(f.read())
f.close()