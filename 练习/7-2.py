'''
@Author: Yaodecheng
@Date: 2019-12-04 20:39:51
@LastEditors: Yaodecheng
'''
import time
import random
#快速排序算法
#快速排序 传入列表、开始位置和结束位置
def quick_sort( li , start , end ):
     # 如果start和end碰头了，说明要我排的这个子数列就剩下一个数了，就不用排序了
    if not start < end :
          return
  
    mid = li[start] #拿出第一个数当作基准数mid
    low = start   #low来标记左侧从基准数始找比mid大的数的位置
    high = end  #high来标记右侧end向左找比mid小的数的位置
 
     # 我们要进行循环，只要low和high没有碰头就一直进行,当low和high相等说明碰头了
    while low < high :
         #从high开始向左，找到第一个比mid小或者等于mid的数，标记位置,（如果high的数比mid大，我们就左移high）
         # 并且我们要确定找到之前，如果low和high碰头了，也不找了
        while low < high and li[high] > mid :
            high -= 1
         #跳出while后，high所在的下标就是找到的右侧比mid小的数
         #把找到的数放到左侧的空位 low 标记了这个空位
        li[low] = li[high]
         # 从low开始向右，找到第一个比mid大的数，标记位置,（如果low的数小于等于mid，我们就右移low）
         # 并且我们要确定找到之前，如果low和high碰头了，也不找了
        while low < high and li[low] <= mid :
            low += 1
         #跳出while循环后low所在的下标就是左侧比mid大的数所在位置
         # 我们把找到的数放在右侧空位上，high标记了这个空位
        li[high] = li[low]
         #以上我们完成了一次 从右侧找到一个小数移到左侧，从左侧找到一个大数移动到右侧
     #当这个while跳出来之后相当于low和high碰头了，我们把mid所在位置放在这个空位
    li[low] = mid
     #这个时候mid左侧看的数都比mid小，mid右侧的数都比mid大
 
     #然后我们对mid左侧所有数进行上述的排序
    quick_sort( li , start, low-1 )
     #我们mid右侧所有数进行上述排序
    quick_sort( li , low +1 , end )

#将数组分为两部分
def partition(l0,sta,end):
    i=sta-1
    for j in range(sta,end):
        if l0[j]<l0[end]:
            i=i+1
            #如果j所在的位置的值小于end，则i往前进一步，并与j的值交换，即将一个新的值加入到<end的区域
            x=l0[i]
            l0[i]=l0[j]
            l0[j]=x
    #一次“分”结束，将用于比较的值放在应该在的地方（两个区域的中间）
    i=i+1
    x=l0[i]
    l0[i]=l0[end]
    l0[end]=x
    return i
    
def quicksort(l0,sta,end):
    #当至少存在两个元素时，才进行接下来的分解
    if sta<end:
        mid=partition(l0,sta,end)
        #分成的sta—mid-1，mid+1—end两个区域接着进行分解、迭代
        quicksort(l0,sta,mid-1)
        quicksort(l0,mid+1,end)
    return l0


list3 =[]
n=1000
for i in range(n):
    list3.append(random.randint(0,n))
#print(list3)
list4=list3
t1=time.time()
list4.sort()
t2=time.time()
print(t2-t1)
print("开始")
t1=time.time()
quicksort(list3,0,len(list3)-1)
t2=time.time()
print("结束")
print(t2-t1)