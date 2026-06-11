import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
path = 'C:\\Users\\Admin\\Downloads\\Test_Entry_Reputyze_Asia\\RA_Bài test Data Analyst_Social Media Data Analyst Intern.xlsx'
df = pd.read_excel(path)

# EDA
print(df.head())
print(df.info())
print(df.shape)