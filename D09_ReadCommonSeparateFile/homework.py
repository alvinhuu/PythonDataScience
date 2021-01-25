import pandas as pd
import sqlite3

# https://www.itread01.com/content/1545132004.html
# 讀寫excel
# 讀寫json
# boston_json_data = pd.read_json('boston.json')
# print(boston_json_data)
# boston_json_data.to_excel('myHomework.xlsx', sheet_name='boston')

# 讀寫SQL資料庫
# connection = sqlite3.connect('boston.sqlite')
# boston_sqlData = pd.io.sql.read_sql('select * from boston', connection)
# connection.close()
# boston_sqlData.to_excel('myHomework.xlsx', sheet_name='boston')

# 讀寫csv
# 讀取資料夾中 boston.csv 讀取其欄位 CHAS、NOX、RM，輸出成 .xlsx 檔案
boston_data = pd.read_csv('boston.csv',usecols=['CHAS','NOX','RM'])
print(boston_data)
boston_data.to_excel('myHomework.xlsx', sheet_name='boston')