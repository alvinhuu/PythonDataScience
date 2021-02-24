
from bokeh.plotting import figure, output_file, show
from bokeh.models import widgets
from bokeh.io import output_notebook
import numpy as np

#https://towardsdatascience.com/data-visualization-with-bokeh-in-python-part-one-getting-started-a11655a467d4
# 讓網頁直接輸出在NOTEBOOK
output_notebook()

# 基本條形圖 條形圖是常見且重要的繪圖類型。通過 Bokeh，可以輕鬆創建各種堆疊或嵌套的條形圖，並通常處理分類數據。 請使用 vbar 方法創建的，用於繪製垂直條。
# 1.  建立簡單的水果資料集
# fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
# counts = [5, 3, 4, 2, 4, 6]
# 2.   利用 Source 建立字典，再用 figure 輸出 BAR 圖
# source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))
# 3.   Bokeh 官方有提供 sample_data 給大家練習，gallery 豐富的範例都取自 sample_data，對比官方的資料格式就能輕鬆模仿應用，下載 股市資料
# 4.   使用 HoverTool(游標滑過時顯示資料)；Click_policy (藉由標籤控制數值顯示)