'''
@Author: Yaodecheng
@Date: 2019-12-03 10:21:43
@LastEditors: Yaodecheng
'''
# 需要的变量放到开头，明显一些。
print('****************************')
#初始化一个空anwser列表用于存放答案
anwser=[]
while True:
    #获取罪犯答案，循环提问，只能回答指定答案
    a = input('A，你认罪吗？请回答认罪或者不认:\n')
    while a!='认罪' and a!= '不认':
        a=input('只能回答“认罪”或“不认”！\n')
    b = input('B，你认罪吗？请回答认罪或者不认:\n')
    while b!='认罪' and b!= '不认':
        b=input('只能回答“认罪”或“不认”!\n')
    #将罪犯答案追加到列表
    anwser.append([a,b])

    if a=='不认' and b=='不认':
        print('都判3年，太棒了!')
        break
    elif a=='认罪' and b=='认罪':
        print('两人都得判10年，唉！')
    elif a=='认罪'and b=='不认':
       print('A判1年，B判20年')
    elif a=='不认'and b=='认罪':
       print('A判20年，B判1年')
# 打印是第几对实验者做出了最优选择。
print('第%d对实验者做出了最优选择。'%len(anwser))
# 通过循环打印每一对实验者的选择。
for n in range(len(anwser)):
    print('第%d对实验者的选择是:A:%sB:%s'%(n+1,anwser[n][0],anwser[n][1]))
print('****************************')
print('————————by YaoDecheng 2019/12/3' )

