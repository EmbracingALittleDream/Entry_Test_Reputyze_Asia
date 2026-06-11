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

# Câu 6: Vẽ biểu đồ tỷ lệ thảo luận trên từng nền tảng

print(df['Platform'].value_counts().index)
print(df['Type'].value_counts())

table = df.groupby(['Platform', 'Type']).size().unstack(fill_value=0)
table['Total'] = table.sum(axis=1)
table['Per_cmt'] = table['comment'] / table['Total']
table['Per_post'] = table['post'] / table['Total']
print(table)

data = {
    'comment': table['Per_cmt'].values,
    'post': table['Per_post'].values
}

index = ['Facebook', 'Forum', 'News', 'Tiktok', 'Youtube']

df_plot = pd.DataFrame(data, index=index)

ax = df_plot.plot(kind='barh')

for p in ax.patches:
    ax.annotate(
        f'{p.get_width():.1%}',
        (p.get_width(), p.get_y() + p.get_height()/2),
        xytext=(5, 0),
        textcoords='offset points',
        va='center'
    )

plt.xlabel('Platform')
plt.ylabel('Tỉ lệ')
plt.title('Tỉ lệ thảo luận trên từng nền tảng')

plt.show()