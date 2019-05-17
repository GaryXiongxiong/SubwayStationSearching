#UseMapBFSFindSubway
import os
from Stations import *#导入编写的地铁站信息
from collections import deque#导入队列类
def search(station,dst):#参数为起点与终点
    search_queue = deque()#创建搜索队列
    searched = {station.getName():None}#创建列表记录已搜索的站点
    search_queue += [station] #将起始站点导入队列尾
    while search_queue:#当队列不为空时，循环搜索
        curStation = search_queue.popleft()#从队列头取出一个站点
        for subStation in stationMap[curStation]:#遍历当前站点的所有后置站点
            if subStation.getName() not in searched.keys():#判断站点是否为目的地站点
                if subStation.getName() == dst.getName():
                    searched[subStation.getName()] = curStation.getName()
                    return searched,dst.getName()
                else:#如果不是
                    search_queue += [subStation]#把当前站点相连通的站点导入队列尾 
                    searched[subStation.getName()] = curStation.getName()#把当前站点标记为已搜索,并把这一站与这一站的前置站点放入散列表searched
                    
    print("NULL")
    return False,dst
start = input("请输入起点站：  ")
dst = input("请输入目的地：  ")
searchedOut,dstOut = search(stationStringMap[start],stationStringMap[dst])
print("-"*10+"路径如下"+"-"*10)
path = [dstOut]
while searchedOut[dstOut] is not None:#
    path.append(searchedOut[dstOut])
    dstOut = searchedOut[dstOut]
path.reverse()
for each in path:
    print(each+" ",end="")
print("\n")
os.system('pause')

