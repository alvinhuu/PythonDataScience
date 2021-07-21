


# 電影院裡通常都是成對情侶一起去看，假設電影院中有100 個人裡面，有 90 名男性和 10 名女性。
# 在這 10 名女性裡，有一半的人有長髮（5 人），另一半有短髮（5人）；在 90 名男性當中，81 個人有短髮，9個人有長髮。

# Q1: 所以根據這個情況條件下，你會預測照片中的長髮是男性或女性(直覺回答)?
print('男性')
# Q2:以上圖資料，計算當你看到長髮時，是女生的機率?
def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    	# calculate P(not A)
	not_a = 1 - p_a
	# calculate P(B)
	p_b = p_b_given_a * p_a + p_b_given_not_a * not_a
	# calculate P(A|B)
	p_a_given_b = (p_b_given_a * p_a) / p_b
	return p_a_given_b
 
# P(A): P(女生)
# P(not A): P(男生)
p_a = 0.1
# P(B|A): P(長髮|女生)
p_b_given_a = 0.5
# P(B|not A): P(長髮|男生)
p_b_given_not_a = 0.1
# calculate P(A|B): P(女生|長髮)
result = bayes_theorem(p_a, p_b_given_a, p_b_given_not_a)
# summarize
# P(女生|長髮)
print('P(A|B) = {0}'.format(round(result * 100,2)))

#所以看到長髮男生的可能性大於女生。

# Q3:你的決策因為男生女生比例不同(先驗分配不同)，和投影片的結果相比，決策有沒有改變?
print('透過貝式定理的運算，得出長髮男生的可能性大於女生，造成決策上的改變，所以以作業和投影片的例子可以看出，先驗分配的重要性，假設錯誤，決策可能就會錯誤。')