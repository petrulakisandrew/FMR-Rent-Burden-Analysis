#Imports
import pandas as pd

#Importing Tenant Info and FMR DataFrames
tenant_df = pd.read_excel('C:/Users/Andrew Petrulakis/Desktop/Reports/Rent Analysis/Rent Burden - FMR Analysis (DHA HCV)/Tenant Info.xlsx')
fmr_df = pd.read_excel('C:/Users/Andrew Petrulakis/Desktop/Reports/Rent Analysis/Rent Burden - FMR Analysis (DHA HCV)/DuPage Small Area FMRs.xlsx')

#Dropping unnecessary columns and cleaning
columns_to_drop = ['Property Code','Property Name','Tenant Status']
tenant_df = tenant_df.drop(columns_to_drop, axis=1)
tenant_df['Zip Code'] = tenant_df['Zip Code'].fillna(0).astype(int)     #Converting Blanks to 0 and Float to Int

#Adding custom columns for analysis
tenant_df['Annual Adjusted Income'] = tenant_df['Adjusted Monthly Income'] * 12
tenant_df['Annual Tenant Rent'] = tenant_df['Monthly Tenant Rent'] * 12
# print(tenant_df.dtypes)
# print(tenant_df)