'''
@Author: Yaodecheng
@Date: 2019-12-07 22:50:22
@LastEditors: Yaodecheng
'''
# 请将你在上一步写好的代码复制黏贴，在其基础上加实例方法。
class robot:
    def __init__(self,name,yourname):
        self.name=name
        self.yourname=yourname
        print('hello {},i\'am {}.Nice to meet you!'.format(yourname,name))
    def make_a_vow(self):
        wish=input(self.name+': wath is your wish？\n')
        print(self.yourname+'your wish is:')
        for time in range(3):
            print(wish)
wall_E=robot('wall.E','jack')
wall_E.make_a_vow()