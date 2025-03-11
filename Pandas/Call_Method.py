import pandas as pd

# dummy data with id, city, latitute, longitude
data = {
    'id': [1, 2, 3, 4, 5],
    'city': [None, 'Los Angeles', 'Chicago', 'Houston', None],
    'latitude': [40.7128, 34.0522, 41.8781, 29.7604, 33.4484],
    'longitude': [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740]
}


city_lookup = {
    (40.7128, -74.0060): 'New York',
    (33.4484, -112.0740): 'Phoenix'
}

def get_city(row):
    return city_lookup[(row['latitude'], row['longitude'])]

df = pd.DataFrame(data)

df['city'] = df.apply(lambda row: get_city(row) if pd.isnull(row['city']) else row['city'], axis=1)

print(df)