import random
scores = []					#定义空列表
num = {}					#定义空字典
for i in range(1000):				#生成1000个数字
    scores.append(random.randint(20, 100))	#随机生成的数在20-100中
scores.sort()					#排序
for i in scores:				#遍历列表
    counts = scores.count(i)			#统计次数
    num[i] = counts				
    #在空字典num中添加新key=scores,value=counts的键值对，若key存在，只更新value
print('数字\t出现次数')
for key in num:					#遍历字典
    print('%s\t%s' %(key,num[key]))
