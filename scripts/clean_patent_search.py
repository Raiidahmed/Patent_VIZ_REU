import pandas as pd
import json,pprint,os,glob

#Identify the file you want to ingest
directory = '../data/raw_data'
file ='Patent_Search_irrelevant.csv'

out_directory ='../data/cleaned_data'
out_file =file.replace('.csv','_cleaned.csv')



#Read Data with Header=None since you don't have header columns
data = pd.read_csv(os.path.join(directory,file),header=None)
print(data.head(5)) #prints first 5 rows

#Define columns
col = ['patent_name','patent_id_str','uspto_link']
data.columns = col #Assign Columns
print(data.head())

#Clean ID column
for row in data.index:
    #For each row in data, read 'patent_id_str' column and replace all commas. Then assign to new column 'patent_id'
    data.loc[row,'patent_id'] = str(data.loc[row,'patent_id_str']).replace(',','')

# Build Google US Patent Link
google_base = "https://patents.google.com/patent/US"
for row in data.index:
    #For each row in data, read 'patent_id' column and build google patent url. Then assign to new column 'google_url'
    data.loc[row,'google_url'] = google_base+data.loc[row,'patent_id']

# Save Cleaned DataFile
data.to_csv(os.path.join(out_directory,out_file),index=None)





