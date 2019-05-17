class Station(object):#定义站点类
    __name = ""
    __line = []
    def __init__(self, name, *lines):#站点构造函数，参数为站点名称，站点所在线路
        self.__name = name
        self.__line = lines
    def getName(self):
        return self.__name
    def getLines(self):
        return self.__line
    def addLines(self, line):
        self.__line.append(line)
yuXM = Station("玉祥门",1)#开始声明各个站点
saJQ = Station("洒金桥",1)
beiDJ = Station("北大街",1,2)
wuLK = Station("五路口",1,4)
chaoYM = Station("朝阳门",1)
kangFL = Station("康复路",1)
tongHM = Station("通化门",1,3)
zhongL = Station("钟楼",2)
yongNM = Station("永宁门",2)
nanSM = Station("南稍门",2)
tiYC = Station("体育场",2)
xiaoZ = Station("小寨",2,3)
changLGY = Station("长乐公园",3)
xianNL = Station("咸宁路",3)
yanXM = Station("延兴门",3)
qingLS = Station("青龙寺",3)
beiCT = Station("北池头",3)
daYT = Station("大雁塔",3,4)
jiXC = Station("吉祥村",3)
taiBNL = Station("太白南路",3)
daCS = Station("大差市",4)
hePM = Station("和平门",4)
jianZKJDX = Station("建筑科技大学",4)
xiAKJDX = Station("西安科技大学",4)
stationStringMap={
    yuXM.getName():yuXM,
    saJQ.getName():saJQ,
    yuXM.getName():yuXM,
    saJQ.getName():saJQ,
    beiDJ.getName():beiDJ,
    wuLK.getName():wuLK,
    chaoYM.getName():chaoYM,
    kangFL.getName():kangFL,
    tongHM.getName():tongHM,
    zhongL.getName():zhongL,
    yongNM.getName():yongNM,
    nanSM.getName():nanSM,
    tiYC.getName():tiYC,
    xiaoZ.getName():xiaoZ,
    changLGY.getName():changLGY,
    xianNL.getName():xianNL,
    yanXM.getName():yanXM,
    qingLS.getName():qingLS,
    beiCT.getName():beiCT,
    daYT.getName():daYT,
    jiXC.getName():jiXC,
    taiBNL.getName():taiBNL,
    daCS.getName():daCS,
    hePM.getName():hePM,
    jianZKJDX.getName():jianZKJDX,
    xiAKJDX.getName():xiAKJDX
}
stationMap = {}#建立站点图，其中每个站点对应散列表中的一个数组，数组中包含与站点联通的所有站点
stationMap[yuXM] = [saJQ]
stationMap[saJQ] = [yuXM,beiDJ]
stationMap[beiDJ] = [saJQ,wuLK,zhongL]
stationMap[wuLK] = [beiDJ,chaoYM,daCS]
stationMap[chaoYM] = [wuLK,kangFL]
stationMap[kangFL] = [chaoYM,tongHM]
stationMap[tongHM] = [kangFL,changLGY]
stationMap[zhongL] = [beiDJ,yongNM]
stationMap[yongNM] = [zhongL,nanSM]
stationMap[nanSM] = [yongNM,tiYC]
stationMap[tiYC] = [nanSM,xiaoZ]
stationMap[xiaoZ] = [tiYC,jiXC,daYT]
stationMap[changLGY] = [tongHM,xianNL]
stationMap[xianNL] = [changLGY,yanXM]
stationMap[yanXM] = [xianNL,qingLS]
stationMap[qingLS] = [yanXM,beiCT]
stationMap[beiCT] = [qingLS,daYT]
stationMap[daYT] = [beiCT,xiAKJDX,xiaoZ]
stationMap[jiXC] = [xiaoZ,taiBNL]
stationMap[taiBNL] = [jiXC]
stationMap[daCS] = [wuLK,hePM]
stationMap[hePM] = [daCS,jianZKJDX]
stationMap[jianZKJDX] = [hePM,xiAKJDX]
stationMap[xiAKJDX] = [jianZKJDX,daYT]
