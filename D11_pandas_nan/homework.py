import pandas as pd  
# 運用編碼處理類別資料
# 補缺失值
# 作業重點:

# 類別編碼有多種方法，需分辨使用方法與時機
# 補缺失值須因應情境決定如何補值
# 題目 : 將以下問卷資料的職業(Profession)欄位缺失值填入字串'others'，更進一步將字串做編碼。 此時用什麼方式做編碼比較適合?為什麼?
q_df = pd.DataFrame([['male', 'teacher'], 
                    ['male', 'engineer'], 
                    ['female', None], 
                    ['female', 'engineer']],columns=['Sex','Profession'])


#缺失值填入字串'others'
print(q_df.fillna('others'))

#更進一步將字串做編碼。 此時用什麼方式做編碼比較適合?為什麼?
print( 'one-hot \n %s' % pd.get_dummies(q_df)) 
data_le=pd.DataFrame(q_df)
print('Label encoding \n%s' % data_le)

print('取值之間沒有大小的意義, 使用 one-hot 編碼比較好')
