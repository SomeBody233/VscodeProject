#读写文件
f=open("C:\\Users\\soulzgd\\Desktop\\temp.txt","r")
#先读第一行
ht = (f.readline()).strip()
L1 = list(ht.split(" "))
#读第二行
lt = (f.readline()).strip()
L2 = list(lt.split(" "))
f.close()
L3 = []
sum = 0
for i in range(len(L1)):
    #将数转为整型
    L1[i] = int(L1[i])
    L2[i] = int(L2[i])
    L3.append((L1[i]+L2[i])/2)
    sum += L3[i]
print(L1)
print(L2)
print("最高气温: ",max(L1))
print("最低气温: ",min(L2))
print("平均气温: %.2f"%(sum/len(L3)))
