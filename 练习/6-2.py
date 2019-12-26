'''
@Author: Yaodecheng
@Date: 2019-12-03 11:22:16
@LastEditors: Yaodecheng
'''
print('****************************')
movies = {
'妖猫传':['黄轩','染谷将太'],
'无问西东':['章子怡','王力宏','祖峰'],
'超时空同居':['雷佳音','佟丽娅'],
}

actor = input('你想查询哪个演员？')
#定义一个该演员所有出演电影的列表，初始化为空
include_list=[]
#遍历字典
for name in movies:
    #如果演员出演了电影，则添加到出演电影列表
    if(actor in movies[name]):
        include_list.append(name)
#如果电影列表不为空，则说明找到该演员出演电影
if include_list:
    print('%s出演的电影有：'%actor)
    for vel in include_list:
            print('<%s>'%vel)
#否则没有查询到出演电影
else :
     print('没有找到%s出演的电影。'%actor)
print('****************************')
print('————————by YaoDecheng 2019/12/3' )

