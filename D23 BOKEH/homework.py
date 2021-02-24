
from bokeh.plotting import figure, output_file, show
from bokeh.models import widgets
from bokeh.io import output_notebook
import numpy as np

#https://towardsdatascience.com/data-visualization-with-bokeh-in-python-part-one-getting-started-a11655a467d4
# 讓網頁直接輸出在NOTEBOOK
output_notebook()

#Bokeh官方有提供sample_data給大家練習，gallery豐富的範例都取自sample_data。
#下載sample_data指令為bokeh.sampledata.download()，直接貼在jupyter執行。檔案會下載到bokeh module裡。
import bokeh.sampledata
bokeh.sampledata.download()


# 基本條形圖 條形圖是常見且重要的繪圖類型。通過 Bokeh，可以輕鬆創建各種堆疊或嵌套的條形圖，並通常處理分類數據。 請使用 vbar 方法創建的，用於繪製垂直條。
# 1.  建立簡單的水果資料集
# fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
# counts = [5, 3, 4, 2, 4, 6]
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]

source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))

p = figure(x_range=fruits, plot_height=250, y_range=(0, 9), title="Fruit Counts")
p.vbar(x='fruits', top='counts', width=0.9, color='color', legend_field="fruits", source=source)

p.xgrid.grid_line_color = None
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

show(p)
# 2.   利用 Source 建立字典，再用 figure 輸出 BAR 圖
# source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))
from bokeh.models import FactorRange
from bokeh.transform import factor_cmap

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ['2015', '2016', '2017']

data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 3, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}

# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
x = [ (fruit, year) for fruit in fruits for year in years ]
counts = sum(zip(data['2015'], data['2016'], data['2017']), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=250, title="Fruit Counts by Year")

#p.vbar(x='x', top='counts', width=0.9, source=source)

p.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",

       # use the palette to colormap based on the the x[1:2] values
       fill_color=factor_cmap('x', palette=['firebrick', 'olive', 'navy'], factors=years, start=1, end=2))

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)
# 3.   Bokeh 官方有提供 sample_data 給大家練習，gallery 豐富的範例都取自 sample_data，對比官方的資料格式就能輕鬆模仿應用，下載 股市資料

# 4.   使用 HoverTool(游標滑過時顯示資料)；Click_policy (藉由標籤控制數值顯示)
import bokeh.io
from bokeh.resources import INLINE
from bokeh.models import HoverTool
from bokeh.palettes import Spectral4
from bokeh.plotting import figure, output_file, show, output_notebook, ColumnDataSource
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT
import pandas as pd

# 環境 settings
bokeh.io.reset_output()
bokeh.io.output_notebook(INLINE)


# set hover
## HoverTool
# 游標滑過時顯示資料,date格式需要轉換，不然會是timestamp
hover = HoverTool(
    tooltips = [
        ("date", "@date"),
        ("close", "@open"),
        ("close", "@close"),
        ("high", "@high"),
        ("low", "@low"),
        ("volume","@volume")
    ], 
    formatters={"@date":"datetime"}
)

# set figure
p = figure(
    plot_width=1000, 
    plot_height=400, 
    x_axis_type="datetime",
    tools=[hover,"pan,box_zoom,reset,save"],
)
p.title.text = 'Stock_Price--Click on legend entries to mute the corresponding lines and show daily details in hover'

# use ColumnDataSource to control
# click_policy
# 藉由標籤控制數值顯示
# hide為隱藏，mute為切換自訂顯示模式
# 可在muted_color控制顏色, muted_alpha控制顏色濃淡

for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    source = ColumnDataSource(df)
    p.line(x="date",y="close", line_width=2, color=color, alpha=0.8,
           muted_color=color, muted_alpha=0.2, legend_label=name,source=source)


p.legend.location = "top_left"
# use hide or mute
p.legend.click_policy="mute"

# output_file("interactive_legend.html", title="interactive_legend.py example")

show(p)
output_notebook() 
