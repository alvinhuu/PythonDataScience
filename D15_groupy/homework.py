import pandas as pd  
import numpy as np

# 題目 : 運用下列分數資料分析 

score_df = pd.DataFrame([[1,50,80,70,'boy',1],[2,60,45,50,'boy',2],[3,98,43,55,'boy',1],[4,70,69,89,'boy',2],[5,56,79,60,'girl',1],[6,60,68,55,'girl',2],[7,45,70,77,'girl',1],[8,55,77,76,'girl',2],[9,25,57,60,'girl',1],[10,88,40,43,'girl',3],[11,25,60,45,'boy',3],[12,80,60,23,'boy',3],[13,20,90,66,'girl',3],[14,50,50,50,'girl',3],[15,89,67,77,'girl',3]],
    columns=['student_id','math_score','english_score','chinese_score','sex','class'])

# 找出全年級各科成績最高分與最低分？

# 找出數學班平均最高的班級？
# 分析全校女生與男生國文平均差幾分？