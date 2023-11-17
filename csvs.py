# Read a CSV file into a list of dictionaries
data=[]
with open (data_file) as f:
    rows = csv.DictReader(f)
    for row in rows:
        row['NumPrevInteractions'] = int(row['NumPrevInteractions'])
        data.append(row)
return data
