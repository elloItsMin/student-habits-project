#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import numpy as np
import matplotlib
import sklearn


# In[2]:


print(pd.__version__)
print(np.__version__)
print(matplotlib.__version__)
print(sklearn.__version__)


# In[3]:


import os
import sys


# In[4]:


print(sys.executable)


# In[5]:


def load_data(file_path):
    # File Exisistence Check
    if not os.path.exists(file_path):
        print(f"오류: '{file_path}' 파일을 찾을 수 없습니다. 프로그램을 종료합니다.")
        sys.exit(1)

    try:
        # Reading CSV files
        df = pd.read_csv(file_path, encoding="utf-8-sig")
        # Getting data shape
        rows, cols = df.shape
        print(f"데이터 로드 완료: {rows}행 × {cols}열")
        return df

    except Exception as e:
        print(f"데이터를 읽는 중 오류가 발생했습니다: {e}")
        sys.exit(1)


# In[14]:


def explore_structure(df):

    rows, cols = df.shape
    print(f"{rows}행 {cols}열")

    # print(df.columns)
    print(df.dtypes)
    print(df.head(5))
    # df.info()


# In[31]:


def show_statistics(df):
    df_numeric = df.select_dtypes(include="number")
    print(df_numeric.describe())

    # count: The number of data points excluding missing values (If it is less than 200, missing values exist)
    # mean: The average value
    # std: Standard deviation (How spread out the values are from the mean)
    # min / max: The minimum value / maximum value
    # 25% / 50% / 75%: The lower quartile / median / upper quartile cutoff values (Quartiles)

    for num_col in df_numeric.columns:
        print(f"{num_col}의 평균: {df_numeric[num_col].mean()}")


# In[49]:


def check_missing(df):

    total_rows = len(df)

    if total_rows == 0:
        return {}

    d_null = {}

    s_null =  df.isnull().sum()

    for idx, val in s_null.items():
        if val != 0:
            percent = 100 * val / total_rows
            if percent < 5:
                severity = "낮음"
            elif percent >= 20:
                severity = "높음"
            else:
                severity = "주의"
            d_null[idx] = {
                "결측치": int(val),
                "결측치 비율(%)": round(percent),
                "심각도": severity
            }
            print(f"{idx} | 결측치: {percent}% | 심각도: {severity}")
    return d_null


# In[80]:


def numpy_stats(df, col):
    df_vals = df[col].dropna().to_numpy()

    result = {'mean': np.mean(df_vals),
             'std': np.std(df_vals),
             '50%': np.median(df_vals),
             'min': np.min(df_vals),
             'max': np.max(df_vals)}

    print(f"6시간 이상 공부하는 학생 수: {len(df_vals[df_vals >= 6])}")

    df_stat = df[col].describe()

    for stat_name, val in result.items():
        v1 = round(df_stat[stat_name], 2)
        v2 = round(val, 2)
        print(f"[{stat_name:4}] Pandas: {v1:<6} | NumPy: {v2:<6} | Identical: {v1 == v2}")    


# In[84]:


def main():
    file_path = r"C:\Users\jmhlo\OneDrive\Documents\student-habits-project\student-habits-project\data\student_habits.csv"
    df = load_data(file_path)
    explore_structure(df)
    show_statistics(df)
    check_missing(df)
    numpy_stats(df, "study_hours")


# In[85]:


main()


# In[ ]:




