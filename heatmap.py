import datetime
import pandas as pd
import seaborn as sns
from mongo.timeseries import query

city = 'Toulouse'
station = '00115 - DEMOISELLES MISTRAL'
days = 30
threshold = datetime.datetime.now() - datetime.timedelta(days=days)

# Get the station information
df = query.station(city, station, threshold)

# Extract the hour and the day of the week
df['Hour'] = df.index.hour
df['Weekday'] = df.index.weekday

# Compute the heatmap with a pivot
heatmap = pd.pivot_table(df, values='b', index='Hour', columns='Weekday')

# Display the heatmap
sns.heatmap(heatmap)
