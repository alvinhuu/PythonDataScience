# Basemap module 安裝步驟：
# 第一步： 因為basemap是基於geos的，所以需要先安裝geos。
# > pip install geos 
# 第二步： basemap下載的時候會先連接pyproj，所以需要下載pyproj.
# > pip install pyproj 
# 第三步： basemap
# > pip install basemap 
# 在裡面找到 pyproj 下載 whl 文件：Unofficial Windows Binaries for Python Extension Packages
# # 若是無法直接安裝 basemap
# 1.  需要手動下載: basemap-1.2.1-cp38-cp38-win_amd64.whl 檔
# 2.  開啟terminal
# 3.  在命令列 pip install basemap-1.2.1-cp38-cp38-win_amd64.whl 

#Basemap 地理資訊圖
# Basemap工具，它是mpl_toolkits包中的一個專門用於構建地理信息數據可視化的擴展庫。
# Basemap工具在地理信息讀寫、坐標映射、空間坐標轉化與投影等方面做的要比geopandas更加成熟，它可以使用常規的地圖素材數據源（shp）作為底圖進行疊加繪圖，效果與精度控制比較方便
# 導入開發套件
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# 新建地圖
map = Basemap()
#Basemap有很多屬性，這里全都使用默認?數
# 畫圖
map.drawcoastlines()
# 顯示
plt.show()
# 存
plt.savefig('test.png')