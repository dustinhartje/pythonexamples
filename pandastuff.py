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

# Show dataframe basic details
this_data.info()

# Show the header and first few rows
print(this_data.head())

# Show unique column values
print(this_data['H2'].explode().unique())
