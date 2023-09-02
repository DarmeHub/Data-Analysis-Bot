import pandas as pd

# Load Dataset
df_2021 = pd.read_excel("All Routes Data.xlsx", sheet_name="FMLM")
df_2022 = pd.read_excel("All Routes Data.xlsx", sheet_name="FMLM (2022)")
df_2023 = pd.read_excel("All Routes Data.xlsx", sheet_name="FMLM (2023)")

df = pd.concat([df_2021, df_2022, df_2023], ignore_index=True)

df = df.drop(['Bus Roll-out', 'Bus Roll-in', 'Average Fare', 'Average Ridership per Bus', 'Bus Capacity',
              'Capacity Supplied', 'Capacity Utilization (%)', 'Capacity Unutilised',
              'Utilization Performance'], axis=1)

df = df.drop(df[df['Date'] == 'SUBTOTAL'].index)
df = df.drop(df[df['Date'] == 'GRANDTOTAL'].index)

df.dropna(subset=['Date', 'Month', 'Ridership', 'Revenue', 'Bus Deployed', 'Actual Round Trips'], inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

df.to_csv('flm_data.csv', index=False)
