'''
@Author: Yaodecheng
@Date: 2019-12-06 20:27:48
@LastEditors: Yaodecheng
'''
#函数封装
import random
import time

# 提示：将以下部分封装进函数
'''
hellokitty抽奖器
lukylist 参与抽奖人元组
'''
def hellokitty(*luckylist):
    a = random.choice(luckylist)  
    print('开奖倒计时',3)
    time.sleep(1)
    print('开奖倒计时',2)
    time.sleep(1)
    print('开奖倒计时',1)
    time.sleep(1)
    image = '''
     /\_)o<
    |      \\
    | O . O|
     \_____/
    '''
    print(image)
    print('恭喜'+a+'中奖！')
    
#运行抽奖器 
if __name__ == "__main__":
    hellokitty('海绵宝宝','派大星','章鱼哥','我')