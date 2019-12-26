'''
@Author: Yaodecheng
@Date: 2019-12-01 19:10:52
@LastEditors: Yaodecheng

*****练习要求
小明、小红、小刚是同班同学，且坐在同一排，分别坐在第一位、第二位、第三位。
由于他们的身高都差不多，所以，老师计划让他们三个轮流坐在第一位。
每次换座位的时候，第一位变第三位，后面两位都往前一位。
'''
students = ['小明','小红','小刚']
for i in range(3):
    students.append(students.pop(0))
    print('students =',students)