from collections import Counter
import operator,math,os,pprint,glob,json,re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    WORD = re.compile(r'\w+')
    words = WORD.findall(text)
    return Counter(words)

def compare_two_phrases(phrase_a,phrase_b):
    vector1 = text_to_vector(phrase_a)
    vector2 = text_to_vector(phrase_b)
    cosine = get_cosine(vector1, vector2)
    return cosine


def get_patent(file):
    data = json.loads(open(file,'r').read())
    return data


# GLOB returns all files with the following pattern (where * is a wildcard placeholder)
patent_filelist = glob.glob('../data/cleaned_data/google_patents/*.json')

for ind,file in enumerate(patent_filelist):
    #Restrict to specifc patent index
    if ind==1:
        print('patent file is:',file)
        patent = get_patent(file)
        abstract = patent['abstract']
        print(abstract)

        #Let's compare this abstract against another abstract in the patent list, say the 5th index
        another_abstract = get_patent(patent_filelist[4])['abstract']
        comparison = compare_two_phrases(abstract,another_abstract)
        print(comparison)

        #Let's compare this abstract against a vector
        vector_abstract = text_to_vector(abstract)
        print('I am the abstract vector:',vector_abstract)

        # Here is a vector I made up.. You'll insert the vector of the functional basis here
        vector_compare = {'invention':50,
                          'jar':24,
                          'opener':12}
        second_comparison = get_cosine(vector_abstract,vector_compare)
        print(second_comparison)

        # You can also stem words.
        #..by turning a phrase into tokens and stemming the word tokens
        tokens = nltk.tokenize.word_tokenize(abstract)
        print(tokens)
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(word=word) for word in tokens] # list of stemmed tokens
        print(stemmed_tokens)

        #..and you can remove stop-words
        stop_words = set(stopwords.words('english'))
        tokens = nltk.tokenize.word_tokenize(abstract)
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(word=word) for word in tokens if word not in stop_words]

