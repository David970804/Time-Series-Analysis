import pandas as pd
from datetime import datetime
name = 'Luyi.csv'

df = pd.read_csv(name)
df = df.dropna()
df['date']= pd.to_datetime(df['date'].astype(str),format='%m/%d/%Y')
df['date'] = df['date'].dt.strftime('%d/%m/%Y')
print(df)
df.to_csv('processed.csv', index = False)