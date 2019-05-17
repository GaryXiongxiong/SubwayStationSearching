# Subway Station Searching

## 功能说明

输入西安地铁中的起点站点与终点站点，输出可乘坐的最短路径

## 文件说明

### UseMapBFSFindSubway.py

主要算法，读取Stations.py中的地铁图信息并计算最短路径

### Stations.py

存储站点信息，目前仅录入了西安市中心的部分站点信息

* `Station`类以存储站点信息
* `stationMap`定义站点间的连接关系
* `stationStringMap`为记录站点名字符串与站点对象的对应关系