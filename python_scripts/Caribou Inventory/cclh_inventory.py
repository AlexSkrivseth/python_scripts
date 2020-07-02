
import pandas as pd
import numpy as np
from pprint import pprint


df_inv_yard = pd.read_csv('inv_csvs/Sheet 1-Table 1.csv')
df_inv_sheet = pd.read_csv('inv_csvs/Sheet 1-Table 2.csv')

list_yard = []
for index, row in df_inv_yard.iterrows():
    list_yard.append(row[0])

list_sheet = []
for index, row in df_inv_sheet.iterrows():
    list_sheet.append(row[0])


not_in_yard = []
for index, row in df_inv_sheet.iterrows():
    if row[0] not in list_yard:
        not_in_yard.append(row[0])

not_in_sheet = []
for index, row in df_inv_yard.iterrows():
    if row[0] not in list_sheet:
        not_in_sheet.append(row[0])



pprint("There are {} Logs that we say we have in the Inventory sheet but that we dont have in the Yard".format(len(not_in_yard)))
print('\n')
pprint('Here are the tag numbers of the logs that are missing')
pprint(not_in_yard)

print("#"*20)
print("#"*20)

pprint('There are {} Logs that are in the Yard but are not in the Inventory Sheet'.format(len(not_in_sheet)))
print('\n')
pprint('Here are the tag numbers that are not in the Inventory Sheet')
pprint(not_in_sheet)
