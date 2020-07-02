import pandas as pd
import numpy as np
import datetime as dt


df = pd.read_csv('kiln1.csv')

index_to_drop = []
for index, row in df.iterrows():

    if row['humidity'] > 99 or row['humidity'] < 2:
        index_to_drop.append(index)

    if row['temperature'] > 160 or row['temperature'] < 90:
        index_to_drop.append(index)
print(index_to_drop)
df.drop(index_to_drop, inplace=True)
df = df.reset_index(drop=True)

time_stamp_list = []
for index, row in df.iterrows():
    date_string = '{} {} {} {} {}'.format(
                                int(row['year']),
                                int(row['month']),
                                int(row['day']),
                                int(row['hour']),
                                int(row['minute']))

    timestamp = dt.datetime.strptime(date_string, '%Y %m %d %H %M')
    time_stamp_list.append(timestamp)

d = {'time_stamp':time_stamp_list}
time_stamp_df = pd.DataFrame(d)
time_stamp_df = time_stamp_df.reset_index(drop=True)

clean_data = df.drop(columns=['year', 'month', 'day', 'hour', 'minute', 'load'])
clean_data = clean_data.reset_index(drop=True)

result_data = pd.concat([time_stamp_df, clean_data], axis=1)

file_to_send = result_data.to_csv('kiln1_data_cleaned.csv')
