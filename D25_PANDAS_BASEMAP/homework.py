from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.figure(figsize=(16,8))
map = Basemap(llcrnrlon = 119.3, llcrnrlat = 20.7, urcrnrlon = 124.6, urcrnrlat = 26,resolution = 'h', epsg = 3415)
map.drawmapboundary(fill_color = 'aqua')
map.fillcontinents(color = 'coral', lake_color = 'aqua')
map.drawcoastlines()
plt.show()

