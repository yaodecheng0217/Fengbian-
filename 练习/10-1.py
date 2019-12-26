import random

# 出拳
punches = ['石头','剪刀','布']
while True:
    computer_choice = random.choice(punches)
    user_choice = ''
    user_choice = input('请出拳：（石头、剪刀、布）')  # 请用户输入选择
    while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
        print('输入有误，请重新出拳')
        user_choice = input()

    # 亮拳
    print('————战斗过程————')
    print('电脑出了：%s' % computer_choice)
    print('你出了：%s' % user_choice)

    # 胜负
    print('—————结果—————')
    if computer_choice==user_choice:
        print('平局')
    elif (computer_choice=='石头'and user_choice=='布')or (computer_choice=='剪刀'and user_choice=='石头') or (computer_choice=='布'and user_choice=='剪刀'):
                print('你赢了')
    else:
        print('你输了')
    
    if input('是否继续（y继续，其他退出）')!='y':
        break
print('游戏结束！')

