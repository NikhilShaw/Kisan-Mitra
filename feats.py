import pandas as pd
from sklearn.svm import SVR
import numpy as np

def get_temp_and_pre(m):
    YEARS = np.array([[2017], [2016], [2015], [2014], [2013], [2012]])
    df_maxT = pd.read_csv("./MaxTemp.csv")
    reg = SVR()
    reg.fit(YEARS,df_maxT.values[m][1:])
    max_temp = reg.predict([[2018]])

    df_minT = pd.read_csv("./MinTemp.csv")
    reg = SVR()
    reg.fit(YEARS, df_minT.values[m][1:])
    min_temp = reg.predict([[2018]])

    df_per = pd.read_csv("./Precip.csv")
    reg = SVR()
    reg.fit(YEARS, df_per.values[m][1:])
    per = reg.predict([[2018]])
    return(max_temp, min_temp, per)

if __name__ == "__main__":
    print(get_temp_and_pre(6))