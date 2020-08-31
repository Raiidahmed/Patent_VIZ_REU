from collections import Counter
import operator, math, os, pprint, glob, json, re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os

def get_cosine(vec1, vec2):
    intersection = set(vec1) & set(vec2)
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0
    else:
        return int(((numerator) / denominator)*100)


def text_to_vector(text):
    WORD = re.compile(r'\w+')
    words = WORD.findall(text)
    return Counter(words)


def compare_two_phrases(phrase_a, phrase_b):
    vector1 = text_to_vector(phrase_a)
    vector2 = text_to_vector(phrase_b)
    cosine = get_cosine(vector1, vector2)
    return cosine


def get_patent(file):
    data = json.loads(open(file, 'r').read())
    return data


def intersection(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    return Counter(intersection)

vector_funct_basis = {        'Material': 1,
                              'Signal': 1,
                              'Energy': 1,
                              'Human': 1,
                              'Gas': 1,
                              'Liquid': 1,
                              'Solid': 1,
                              'Plasma': 1,
                              'Mixture': 1,
                              'Status': 1,
                              'Control': 1,
                              'Acoustic': 1,
                              'Biological': 1,
                              'Chemical': 1,
                              'Electrical': 1,
                              'Electromagnetic': 1,
                              'Hydraulic': 1,
                              'Magnetic': 1,
                              'Mechanical': 1,
                              'Pneumatic': 1,
                              'Radioactive/Nuclear': 1,
                              'Thermal': 1,
                              'Object': 1,
                              'Particulate': 1,
                              'Composite': 1,
                              'Gas–gas': 1,
                              'Liquid–liquid': 1,
                              'Solid–solid': 1,
                              'Solid–liquid': 1,
                              'Liquid–gas': 1,
                              'Solid–gas': 1,
                              'Solid–liquid–gas': 1,
                              'Colloidal': 1,
                              'Auditory': 1,
                              'Olfactory': 1,
                              'Tactile': 1,
                              'Taste': 1,
                              'Visual': 1,
                              'Analog': 1,
                              'Discrete': 1,
                              'Optical': 1,
                              'Solar': 1,
                              'Rotational': 1,
                              'Translational': 1,
                              'Hand': 1,
                              'foot': 1,
                              'head': 1,
                              'Homogeneous': 1,
                              'Incompressible': 1,
                              'compressible': 1,
                              'homogeneous': 1,
                              'Rigid-body': 1,
                              'elastic-body': 1,
                              'widget': 1,
                              'Aggregate': 1,
                              'Aerosol': 1,
                              'Toneword': 1,
                              'Temperature': 1,
                              'pressure': 1,
                              'roughness': 1,
                              'Position': 1,
                              'displacement': 1,
                              'Oscillatory': 1,
                              'Binary': 1,
                              'Effort': 1,
                              'Force': 1,
                              'Affinity': 1,
                              'Electromotive Force': 1,
                              'Magnetomotive Force': 1,
                              'Torque': 1,
                              'Temperature': 1,
                              'Flow': 1,
                              'Velocity': 1,
                              'Particle velocity': 1,
                              'Volumetric ﬂow': 1,
                              'Reaction rate': 1,
                              'Current': 1,
                              'Flow': 1,
                              'Magnetic ﬂux rate': 1,
                              'Angular velocity': 1,
                              'Linear velocity': 1,
                              'Mass ﬂow': 1,
                              'Decay rate': 1,
                              'Heat ﬂow': 1,
                              'Isolate': 1,
                              'sever': 1,
                              'disjoin': 1,
                              'Detach': 1,
                              'isolate': 1,
                              'release': 1,
                              'sort': 1,
                              'split': 1,
                              'disconnect': 1,
                              'subtract': 1,
                              'Reﬁne': 1,
                              'ﬁlter': 1,
                              'purify': 1,
                              'percolate': 1,
                              'strain': 1,
                              'clear': 1,
                              'Cut': 1,
                              'drill': 1,
                              'lathe': 1,
                              'polish': 1,
                              'sand': 1,
                              'Diffuse': 1,
                              'dispel': 1,
                              'disperse': 1,
                              'dissipate': 1,
                              'diverge': 1,
                              'scatter': 1,
                              'Form entrance': 1,
                              'allow': 1,
                              'input': 1,
                              'capture': 1,
                              'Dispose': 1,
                              'eject': 1,
                              'emit': 1,
                              'empty': 1,
                              'remove': 1,
                              'destroy': 1,
                              'eliminate': 1,
                              'Carry': 1,
                              'deliver': 1,
                              'Advance': 1,
                              'lift': 1,
                              'move': 1,
                              'Conduct': 1,
                              'convey': 1,
                              'Direct': 1,
                              'shift': 1,
                              'steer': 1,
                              'straighten': 1,
                              'switch': 1,
                              'Move': 1,
                              'relocate': 1,
                              'Spin': 1,
                              'turn': 1,
                              'Constrain': 1,
                              'unfasten': 1,
                              'unlock': 1,
                              'Associate': 1,
                              'connect': 1,
                              'Assemble': 1,
                              'fasten': 1,
                              'Attach': 1,
                              'Add': 1,
                              'Blend': 1,
                              'Coalesce': 1,
                              'Combine': 1,
                              'pack': 1,
                              'Enable': 1,
                              'Initiate': 1,
                              'Start': 1,
                              'turn-on': 1,
                              'Control': 1,
                              'Equalize': 1,
                              'Limit': 1,
                              'maintain': 1,
                              'Allow': 1,
                              'open': 1,
                              'Close': 1,
                              'Delay': 1,
                              'interrupt': 1,
                              'Adjust': 1,
                              'Modulate': 1,
                              'Clear': 1,
                              'Demodulate': 1,
                              'Invert': 1,
                              'Normalize': 1,
                              'Rectify': 1,
                              'reset': 1,
                              'scale': 1,
                              'vary': 1,
                              'modify': 1,
                              'Amplify': 1,
                              'Enhance': 1,
                              'Magnify': 1,
                              'multiply': 1,
                              'Attenuate': 1,
                              'Dampen': 1,
                              'reduce': 1,
                              'Compact': 1,
                              'Compress': 1,
                              'Crush': 1,
                              'Pierce': 1,
                              'Deform': 1,
                              'form': 1,
                              'Prepare': 1,
                              'Adapt': 1,
                              'treat': 1,
                              'End': 1,
                              'Halt': 1,
                              'Pause': 1,
                              'Interrupt': 1,
                              'restrain': 1,
                              'Disable': 1,
                              'turn-off': 1,
                              'Shield': 1,
                              'Insulate': 1,
                              'Protect': 1,
                              'resist': 1,
                              'Condense': 1,
                              'Create': 1,
                              'Decode': 1,
                              'Differentiate': 1,
                              'Digitize': 1,
                              'Encode': 1,
                              'Vaporate': 1,
                              'Generate': 1,
                              'Integrate': 1,
                              'Liquefy': 1,
                              'Process': 1,
                              'Solidify': 1,
                              'transform': 1,
                              'Accumulate': 1,
                              'Capture': 1,
                              'enclose': 1,
                              'Absorb': 1,
                              'Consume': 1,
                              'ﬁll': 1,
                              'reserve': 1,
                              'Provide': 1,
                              'Replenish': 1,
                              'retrieve': 1,
                              'Feel': 1,
                              'determine': 1,
                              'Discern': 1,
                              'Perceive': 1,
                              'recognize': 1,
                              'Identify': 1,
                              'locate': 1,
                              'Announce': 1,
                              'Show': 1,
                              'Denote': 1,
                              'Record': 1,
                              'register': 1,
                              'Mark': 1,
                              'time': 1,
                              'Emit': 1,
                              'Expose': 1,
                              'select': 1,
                              'Compare': 1,
                              'Calculate': 1,
                              'check': 1,
                              'Steady': 1,
                              'Constrain': 1,
                              'Hold': 1,
                              'Place': 1,
                              'ﬁx': 1,
                              'Align': 1,
                              'Locate': 1,
                              'Orient': 1,
                              'Divide': 1,
                              'Extract': 1,
                              'Remove': 1,
                              'Transport': 1,
                              'Transmit': 1,
                              'Translate': 1,
                              'Rotate': 1,
                              'Join': 1,
                              'Link': 1,
                              'Increase': 1,
                              'Decrease': 1,
                              'Shape': 1,
                              'Condition': 1,
                              'Prevent': 1,
                              'Inhibit': 1,
                              'Contain': 1,
                              'Collect': 1,
                              'Detect': 1,
                              'Measure': 1,
                              'Track': 1,
                              'Display': 1,
                              'Separate': 1,
                              'Distribute': 1,
                              'Import': 1,
                              'Export': 1,
                              'Transfer': 1,
                              'Guide': 1,
                              'Couple': 1,
                              'Mix': 1,
                              'Actuate': 1,
                              'Regulate': 1,
                              'Change': 1,
                              'Stop': 1,
                              'Convert': 1,
                              'Store': 1,
                              'Supply': 1,
                              'Sense': 1,
                              'Indicate': 1,
                              'Process': 1,
                              'Stabilize': 1,
                              'Secure': 1,
                              'Position': 1,
                              'Branch': 1,
                              'Channel': 1,
                              'Connect': 1,
                              'Magnitude': 1,
                              'Convert': 1,
                              'Provision': 1,
                              'Signal': 1,
                              'Support': 1,
                              }
tokens_funct_basis = word_tokenize(' '.join(vector_funct_basis))
stemmer1 = PorterStemmer()
stemmed_tokens1 = [stemmer1.stem(word=word) for word in tokens_funct_basis]  # list of stemmed tokens
vector_funct_basis = ' '.join(stemmed_tokens1)
vector_funct_basis = text_to_vector(vector_funct_basis)

patent_filelist = glob.glob('../data/cleaned_data/google_patents/*.json')
patent_filelist2 = glob.glob('../data/cleaned_data/google_patents_irrelevant/*.json')

filelist = patent_filelist

results = []

counter = 0
counter2 = 0
counter3 = 0
counter4 = 0

count1 = next(os.walk('../data/cleaned_data/google_patents'))[2]
count2 = next(os.walk('../data/cleaned_data/google_patents_irrelevant'))[2]
count_relevant = len(count1)
count_irrelevant = len(count2)

print('This is the amount of relevant patents ' + str(count_relevant) + '.')
print('This is the amount of relevant patents ' + str(count_irrelevant) + '.')

print('This matrix cointains the similarity values of every possible combination of patents from the directory.')

for x in range(0, 3):
    filelist = patent_filelist
    if counter >= count_relevant:
        filelist = patent_filelist2
        counter = 0
        counter4 = counter
    for ind, file in enumerate(filelist):
            if ind < count_relevant:
                filelist = patent_filelist
                if counter >= count_relevant:
                    filelist = patent_filelist2
                counter2 = 0
                if results != []:
                    print(results)
                results = []
                patent = get_patent(file)
                abstract = patent['abstract']
                tokens = word_tokenize(abstract)
                stemmer = PorterStemmer()
                stemmed_tokens = [stemmer.stem(word=word) for word in tokens]  # list of stemmed tokens
                vector_abstract = text_to_vector(' '.join(stemmed_tokens))
                vector_clean = intersection(vector_abstract, vector_funct_basis)
                counter = counter + 1
                if counter >= count_relevant:
                    print('Start of irrelevant patents.')
                    break
                if counter4 > count_irrelevant:
                    break

            for x in range(0, 3):
                    filelist = patent_filelist
                    if counter2 >= count_relevant:
                        filelist = patent_filelist2
                        counter2 = 0
                        counter3 = counter2
                    for ind, file in enumerate(filelist):
                        if ind < count_relevant:
                                filelist = patent_filelist
                                if counter2 >= count_relevant:
                                    filelist = patent_filelist2
                                patent2 = get_patent(file)
                                abstract2 = patent2['abstract']
                                tokens2 = word_tokenize(abstract2)
                                stemmer2 = PorterStemmer()
                                stemmed_tokens2 = [stemmer2.stem(word=word) for word in tokens2]
                                vector_abstract2 = text_to_vector(' '.join(stemmed_tokens2))
                                vector_clean2 = intersection(vector_abstract2, vector_funct_basis)
                                comparison = get_cosine(vector_clean, vector_clean2)
                                results.append(comparison)
                                counter2 = counter2 + 1
                                if counter2 >= count_relevant:
                                    results.append('Start of Irrelevant Patents.')
                                    break
                                if counter3 > count_irrelevant:
                                    break








