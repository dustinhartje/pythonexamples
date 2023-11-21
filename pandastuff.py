import pandas as pd

# Read a dataframe in from a CSV
csv1 = pd.read_csv('./testdata/test1.csv')


# Force headers and/or datatypes from CSVs that don't infer them correctly / they are missing:

this_data = pd.read_csv(
    './testdata/test2.csv',
    header = None,
    names = ['H1', 'H2', 'H3'],
    dtype = {'H1': 'string'}
    )


# Inspect and pick through dataframes

print('\nShow dataframe basic details')
this_data.info()

print('\nShow the header and first few rows')
print(this_data.head())

print('\nShow unique column values')
print(this_data['H2'].explode().unique())

print('\nSorted unique values')
print(sorted(this_data['H2'].explode().unique()))


# Selecting rows

print('\nSelect rows matching a particular column value (H2 == \'eight\')')
print(this_data[this_data['H2'] == 'eight'])
print('\nSelect rows not matching a particular column value (H2 != \'eight\')')
print(this_data[this_data['H2'] != 'eight'])
print('\n')
print('\n')
print('\n')
print('\n')
