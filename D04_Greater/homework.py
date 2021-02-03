import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([45,90,82,72,66,77])

#1.有多少學生英文成績比數學成績高?
ans1 = np.greater(english_score,math_score)
# print(ans1)
Ans = [ A for A in ans1 if A==True ]
print('有 %d 個學生英文成績比數學成績高' % len(Ans))
print('有 %d 個學生英文成績比數學成績高' % np.sum(Ans))

#2.是否全班同學最高分都是國文?
ans2 = np.greater(chinese_score,english_score,math_score )
# print(ans2)
Ans = [ A for A in ans2 if A==1 ]
print('是否全班同學最高分都是國文: %s' % ( len(Ans)==6) )
print('是否全班同學最高分都是國文: %s' % ans2.any() )

ch_greater_ma = np.greater(chinese_score,math_score)
ch_greater_en = np.greater(chinese_score,english_score)
print(np.logical_and(ch_greater_ma,ch_greater_en))
print(np.logical_and(ch_greater_ma,ch_greater_en).all())