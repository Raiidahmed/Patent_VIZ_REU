import json,os,glob,pprint
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

def find_patent_citations (list):
        pat_citation_section = [item for item in soup.findAll('h2') if 'Patent Citation' in item.text][0]
        print([item for item in pat_citation_section.next_siblings ])

        ##### I have a problem here.  Trying to do this.  or that.
        for item in pat_citation_section.next_siblings:
            print('item is',item)
            if item!='\n':
                print('FOUND', item.find('span',{'itemprop':'publicationNumber'}))

        for text in soup.find_all('span', {'itemprop' : 'publicationNumber'}):
            list.append(text.text)

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8','Accept': 'application/json'}

#grab Data
data = pd.read_csv('../data/cleaned_data/Patent_Search_cleaned.csv')


output_json = dict()

#for each fow in data
for ind,row in enumerate(data.index):

    #test on small subset, namely, the first row
    if ind > -1: # Change to -1 to run all documents
        entry_dict = dict()

        url = data.loc[row,'google_url']
        patent_id = data.loc[row,'patent_id']

        print(url)
        google_patent = requests.get(url, headers=headers)
        soup = BeautifulSoup(google_patent.text, 'html.parser')

        #Explore the HTML
        pprint.pprint(soup)
        #Abstract Text
        try:
            abstract = soup.find('section',{'itemprop':'abstract'}).find('div',{'class':'abstract'}).text
            check = 1
        except:
            abstract = ""
            check = 0
        entry_dict['abstract'] = abstract

        # Title Text
        try:
            title = soup.find('h1', {'itemprop': 'pageTitle'}).text
            #print(title)
        except:
            title = ""
        entry_dict['title'] = title

        # Claims Text
        try:
            claims = soup.find('section', {'itemprop': 'claims'}).text
            #print(claims)
        except:
            claims = ""
        entry_dict['claims'] = claims

        # Similar Documents (use findAll to iterate through all <tr itemprop="similarDocuments" itemscope="" repeat="">
        similar_documents = []#.. add code here
        entry_dict['similar_documents'] = similar_documents

        # Invention Description <div class="description" lang="EN" load-source="patent-office">
        try:
            invention_desc = soup.find('div', {'class': 'description'}).text
            #print(invention_desc)
        except:
            invention_desc = ""
        entry_dict['invention_desc'] = invention_desc

        # Patent Citations <h2>Patent Citations </
        patent_citations = []
        try:
           find_patent_citations(patent_citations)
        except:
            patent_citations = ""

        entry_dict['patent_citations'] = patent_citations

        # Inventor
        try:
            inventor = soup.find('dd', {'itemprop':'inventor'}).text #.. add code here
        except:
            inventor = ""
        entry_dict['inventor'] = inventor

        # Original Assignee
        try:
            assignee = soup.find('dd', {'itemprop':'assigneeOriginal'}).text
        except:
            entry_dict['assignee'] = assignee

        # Priority Date
        try:
            priority_date = soup.find('time', {'itemprop':'priorityDate'}).text# .. add code here
        except:
            priority_date = ""
        entry_dict['priority_date'] = priority_date

        # Patent Date
        try:
            patent_date = soup.find('time', {'itemprop':'filingDate'}).text
        except:
            entry_dict['patent_date'] = patent_date
        if check == 1:
            output_json[patent_id] = entry_dict
            time.sleep(2)
            print(entry_dict);
            with open('../data/cleaned_data/google_patents/'+str(patent_id)+'.json','w') as f:
                f.write(json.dumps(entry_dict))
                f.close()