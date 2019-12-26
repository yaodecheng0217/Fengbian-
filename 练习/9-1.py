'''
@Author: Yaodecheng
@Date: 2019-12-06 20:14:52
@LastEditors: Yaodecheng
'''
#定义两个函数：第一个函数功能为根据工作月数返回奖金额，
def reward(month):
    if month<5:
        return 500
    elif 6<=month<=12:
        return 120*month
    else:
        return 180*month 
#第二个函数功能为打印出'该员工来了XX个月，获得奖金XXX元'。
def printall(name,month):
    print ('{}来了{}个月，获得奖金{}元'.format(name,month,reward(month)))


#最后传入参数('大聪'，14)调用第二个函数，打印结果'大聪来了14个月，获得奖金2520元'
if __name__ == "__main__":
    printall('大聪',14)