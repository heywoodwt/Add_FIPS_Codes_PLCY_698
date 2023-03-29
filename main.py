import addfips
import pandas as pd


# import csv
df = pd.read_csv('stRAPApplicationSummaryCSV.csv')

# Add FIPS codes based on county to df
af = addfips.AddFIPS()
df['FIPS'] = df.apply(lambda x: af.get_county_fips(x['County'], state=x['State']), axis=1)

# export to csv
df.to_csv('stRAPApplicationSummaryCSV_2.csv', index=False)
