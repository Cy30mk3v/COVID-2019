from datetime import date, timedelta, datetime
import urllib.request as request
import pandas as pd
import numpy as np
import os
#str_today = date.today()

#today = str_today.strftime("%m-%d-%Y")
#name_file=today+".csv"



def readCSV(file_name):
    df_csv = pd.read_csv(file_name)
    return df_csv

def writeCSV(*parameter):
    os.remove(parameter[1])
    parameter[0].to_csv(parameter[1],header=False,mode='a')




start_date = date(2020,1,22)
today = date.today()
print(today)
end_date = today
delta = timedelta(days=1)
time =datetime.utcnow()
if(time.hour==0):
    if(time.minute<=30):
        end_date-=delta
date = start_date+delta
total = 0
df_sum = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv', error_bad_lines=False)
total+=df_sum.shape[0]
# while(date<end_date):
#     str_date = date.strftime("%m-%d-%Y")+".csv"
#     print(str_date)
#     url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + str_date
#     df_temp = pd.read_csv(url,error_bad_lines=False)
#     total+=df_temp.shape[0]
#     #print(df_temp)
#     df_sum.append(df_temp,ignore_index=True)
#     date+=delta
writeCSV(df_sum,"data_COVID-2019_infected.csv")
print(df_sum)
print(df_sum.sum())