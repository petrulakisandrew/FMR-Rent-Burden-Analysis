#Imports
import pandas as pd
import openpyxl

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

#Merging FMR based on Zip and Bedroom size onto tenant_df
unit_fmr = []

for i, row in tenant_df.iterrows():
    zip_code = row['Zip Code']
    bedrooms = row['Bedrooms']
    
    matchedfmr = fmr_df[fmr_df['Zip Code'] == zip_code]
    
    if matchedfmr.empty:
        unit_fmr.append(None)
    else:
        if bedrooms == 0:
            unit_fmr.append(matchedfmr.iloc[0]['Efficency'])
        elif bedrooms == 1:
            unit_fmr.append(matchedfmr.iloc[0]['One-Bedroom'])
        elif bedrooms == 2:
            unit_fmr.append(matchedfmr.iloc[0]['Two-Bedroom'])
        elif bedrooms == 3:
            unit_fmr.append(matchedfmr.iloc[0]['Three-Bedroom'])
        elif bedrooms == 4:
            unit_fmr.append(matchedfmr.iloc[0]['Four-Bedroom'])
        else:
            unit_fmr.append(None)
        

# print(unit_fmr)
    
tenant_df['FMR'] = unit_fmr
tenant_df['FMR'] = tenant_df['FMR'].fillna(0).astype(int)
# print(tenant_df)

#Creating new sorted DataFrame for excel export
sortedtenant_df = tenant_df[
    # (tenant_df['Voucher Payment Standard'] == tenant_df['FMR']) &     #Payment Standard Equals FMRs
    # (tenant_df['HAP'] >= 0.95 * tenant_df['Voucher Payment Standard'])&     #HAP equals 95% or more of Payment Standard
    (tenant_df['Annual Adjusted Income'] != 0)    #Removing all tenants that have an annual income of 0
].reset_index()

# print(sortedtenant_df)

#Sorted DataFrame exported to Excel
sortedtenant_df.to_excel('Rent Burden Analysis - DHA FMRs.xlsx', index=False)