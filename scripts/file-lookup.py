import pprint,os,glob,json

files = glob.glob(os.path.join('..','data','cleaned_data','google_patents','*.json'))

out_dict = dict()
out_dict['files']=[]
for file in files:
    out_dict['files'].append(file)

with open('../data/cleaned_data/patent-lookup.json','w') as f:
    f.write(json.dumps(out_dict))
f.close()