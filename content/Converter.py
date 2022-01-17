import pandas as pd
df = pd.read_csv (r'data.csv')
df.to_json (r'data.json')
