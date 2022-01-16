import numpy as np
import pandas as pd

# import dataset
df = pd.read_csv ('./data.csv', encoding='utf-8')

# add json column to the dataframe
# since we use 'records' each row will be converted with a structure {'col1': 'value', 'col2': 'value'}
# lines=True adds a line delimiter '\n' at the end of each record
# splitlines will split the json string into multiple rows
df['json'] = df.to_json(orient='records', lines=True).splitlines()

# take the json column of the dataframe
dfjson = df['json']

# print out the dataframe to a file
# since dfjson.values returns an array, the easiest option is to use np.savetxt
# fmt='%s' means that we are formatting as a string
# note that the timestamp forward slash (/) used in the dates is escaped to be valid JSON
np.savetxt(r'./output.txt', dfjson.values, fmt='%s')