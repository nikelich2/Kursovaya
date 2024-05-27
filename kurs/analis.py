import pandas as pd
import sqlite3

conn = sqlite3.connect('ad_campaigns.db')
campaigns = pd.read_sql_query("SELECT * FROM campaigns", conn)
metrics = pd.read_sql_query("SELECT * FROM metrics", conn)
conn.close()

metrics['CTR'] = metrics['clicks'] / metrics['impressions'] * 100
metrics['CPA'] = metrics['cost'] / metrics['conversions']

print(metrics)

conn = sqlite3.connect('ad_campaigns.db')
metrics.to_sql('metrics', conn, if_exists='replace', index=False)
conn.close()