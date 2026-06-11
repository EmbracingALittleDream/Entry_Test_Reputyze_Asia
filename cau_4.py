# Tải thư viện
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
path = 'C:\\Users\\Admin\\Downloads\\Test_Entry_Reputyze_Asia\\RA_Bài test Data Analyst_Social Media Data Analyst Intern.xlsx'
df = pd.read_excel(path)

# Làm sạch biến Like

print(df['Like'])   # in Series Like

i = []
for index, item in enumerate(list(df['Like'])):
    if (isinstance(item, str)):
        i += [index]
print(i)    # in các chỉ số của giá trị kiểu ký tự trong Series Like

for item in i:
    print(df.loc[item, 'Like'], end = " ") # in các giá trị kiểu ký tự trong Series Like

arr = []
for index, item in enumerate(list(df['Like'])):
    if (isinstance(item, str)):
        df.loc[index, 'Like'] = int(item.replace('"', ''))
        arr += [df.loc[index, 'Like']]
print(arr) # in các giá trị sau khi làm sạch

# Thống kê các chỉ số theo ngày

print(df.groupby(['Created Date', 'Type']).size().unstack())    # tổng số bài post và comment theo ngày
print(df['Type'].value_counts())                                # tổng số bài post và comment trong tháng 5 

sub_df = df.groupby('Created Date')[['Like', 'Shares', 'Comments']].sum()
sub_df['Engagement'] = sub_df['Like'] + sub_df['Shares'] + sub_df['Comments']

sub_df['Mention'] = df.groupby('Created Date').size()
print(sub_df)

