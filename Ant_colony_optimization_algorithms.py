import os
import pandas as pd
from math import radians, cos, sin, asin, sqrt

# Connect the file with the data.
file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(file_dir, 'City_Map.xlsx')
sheet_name = 'Областные центры'

df = pd.read_excel(file_name, sheet_name)

# Checking a validity file.

# Check the number of columns.
if df.shape[1] != 3:
    print(f"Included incorrect amount of data.\n"
          f"Check the downloadable XLSX file.\n"
          f"There must be only 3 columns.")
    df = None

# Check on empty cells.
if df.isnull().sum().sum() != 0:
    print(f"Included incorrect amount of data.\n"
          f"Check the downloadable xlsx file.\n"
          f"Should not be empty cells.")
    df = None



def haversine(lat1, lon1, lat2, lon2):
    """
    Calculation of distances between cities in kilometers.
    Calculate the distance between the two coordinates
    (indicated in decimal degrees).
    """
    # We convert decimal degrees into radians.
    # Latitude (lat).
    # Longitude (lon).
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Formula Gaversinus.
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371 * c  # Earth radius 6371 kilometers.

    return km


# We prepare for the creation of a distances table between cities.
df_distance = {}

# We consider the number of cities.
number_of_cities = range(len(df))

# We generate the first string with the names of the goths.
for num_city in number_of_cities:
    df_distance[df.iloc[num_city][0]] = {}

# Fill the table by tramings between all cities.
for num_city_x in number_of_cities:
    for num_city_y in number_of_cities:
        df_distance[df.iloc[num_city_y][0]][df.iloc[num_city_x][0]] = haversine(
            df.iloc[num_city_x, 1], df.iloc[num_city_x, 2], df.iloc[num_city_y, 1], df.iloc[num_city_y, 2])

# Convert data to DataFrame.
df_distance = pd.DataFrame(df_distance)
