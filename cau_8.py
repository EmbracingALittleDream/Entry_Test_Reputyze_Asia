# Tải thư viện
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
path = 'C:\\Users\\Admin\\Downloads\\Test_Entry_Reputyze_Asia\\RA_Bài test Data Analyst_Social Media Data Analyst Intern.xlsx'
df = pd.read_excel(path)

# Làm sạch biến Like

print(df['Like'])                                               # in Series Like

i = []
for index, item in enumerate(list(df['Like'])):
    if (isinstance(item, str)):
        i += [index]
print(i)                                                        # in các chỉ số của giá trị kiểu ký tự trong Series Like

for item in i:
    print(df.loc[item, 'Like'], end = " ")                      # in các giá trị kiểu ký tự trong Series Like

arr = []
for index, item in enumerate(list(df['Like'])):
    if (isinstance(item, str)):
        df.loc[index, 'Like'] = int(item.replace('"', ''))
        arr += [df.loc[index, 'Like']]
print(arr)                       

# Câu 8: 
"""Top 5 chủ đề (nội dung) có nhiều thảo luận nhất trong bảng dữ liệu
và tỉ lệ phần trăm thảo luận của từng chủ đề (nội dung)"""

top_5 = df.sort_values(by = 'Comments', ascending = False).head()
print(top_5[['Title', 'Content']])

total = df['Comments'].sum()

ti_le = df['Comments'].sort_values(ascending = False).head() / total
print(ti_le)