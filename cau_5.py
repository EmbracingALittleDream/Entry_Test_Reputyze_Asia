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
print(arr)                                                      # in các giá trị sau khi làm sạch


print(df.groupby(['Created Date', 'Type']).size().unstack())    # tổng số bài post và comment theo ngày
print(df['Type'].value_counts())                                # tổng số bài post và comment trong tháng 5 

sub_df = df.groupby('Created Date')[['Like', 'Shares', 'Comments']].sum()
sub_df['Engagement'] = sub_df['Like'] + sub_df['Shares'] + sub_df['Comments']

sub_df['Mention'] = df.groupby('Created Date').size()

# Câu 5: 
"""Vẽ biểu đồ xu hướng thảo luận (mention) và tương tác (egagement) theo thời gian. 
Cho thấy được lượng thảo luận và tương tác mỗi ngày là bao nhiêu"""

seq = list(range(1, 32, 1))
seq.pop(26)
for item in seq:
    print(item, end = ' ')

figure, axes = plt.subplots(1, 2, figsize = (12, 5))

axes[0].plot(seq, sub_df['Engagement'],
             linestyle = 'solid',
             linewidth = 2,
             color = 'skyblue',
             marker = '*',
             markersize = 6,
             markerfacecolor = 'yellow',
             markeredgecolor = 'black')
axes[0].set_title('Engagement')
axes[0].set_xlabel('Ngay')
axes[0].set_ylabel('Tong so Engagement')
for xi, yi in zip(seq, sub_df['Engagement']):
    axes[0].annotate(
        yi,
        (xi, yi),
        textcoords = 'offset points',
        xytext = (0, 5),
        ha = 'center')

axes[1].plot(seq, sub_df['Mention'],
             linestyle = 'solid',
             linewidth = 2,
             color = 'skyblue',
             marker = '*',
             markersize = 6,
             markerfacecolor = 'yellow',
             markeredgecolor = 'black')
axes[1].set_title('Mention')
axes[1].set_xlabel('Ngay')
axes[1].set_ylabel('Tong so Mention')
for xi, yi in zip(seq, sub_df['Mention']):
    axes[1].annotate(
        yi,
        (xi, yi),
        textcoords = 'offset points',
        xytext = (0, 5),
        ha = 'center')
    
plt.show()