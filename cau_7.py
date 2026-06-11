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

# Câu 7: Vẽ biểu đồ thể hiện tỉ lệ sắc thái thảo luận (sentiment)

print(df['Platform'].value_counts())
print(df['Sentiment'].value_counts())

df_sub = df.groupby(['Platform', 'Sentiment']).size().unstack(fill_value=0)
df_sub['Total'] = df_sub['negative'] + df_sub['neutral'] + df_sub['positive'] 
df_sub['Per_negative'] = df_sub['negative'] / df_sub['Total']
df_sub['Per_neutral'] = df_sub['neutral'] / df_sub['Total']
df_sub['Per_positive'] = df_sub['positive'] / df_sub['Total']
print(df_sub)

axe = df_sub[['Per_negative', 'Per_neutral', 'Per_positive']].plot(kind ='barh', figsize=(13, 6))

for p in axe.patches:
    axe.annotate(
        f'{p.get_width():.1%}',
        (p.get_width(), p.get_y() + p.get_height()/2),
        xytext=(5, 0),
        textcoords='offset points',
        va='center'
    )

plt.xlabel('Tỉ lệ')
plt.title('Tỉ lệ sắc thái trên từng nền tảng')

# Thông tin thêm
df_ssub = df.groupby(['Platform', 'Sentiment', 'Type']).size().unstack(fill_value=0)
df_ssub['Total'] = df_ssub['comment'] + df_ssub['post']
df_ssub['Per_cmt'] = df_ssub['comment'] / df_ssub['Total']
df_ssub['Per_post'] = df_ssub['post'] / df_ssub['Total']
print(df_ssub)

plt.show()
