
# coding: utf-8

# In[ ]:


def list_condenser_Rosalind(list_name):
    #empty list
    list2 = []
    for i in list_name:
        #adds the name of the gene as well as an empty index immediately afterwards
        if '>' in i:
            list2.append(i[1:])
            list2.append('')
        else:
            #adds the DNA string to the current empty index
            list2[len(list2)-1] =  list2[len(list2)-1] + i
    return list2

def prefix_suffix_genes_Rosalind(listOfStrings, k = 3):
    #empty dictionary
    prefSuffDic = {}
    for i in range(len(listOfStrings)):
        #sequences should be at every odd index
        if i % 2 != 0:
            #so when you find a sequence create a new dict entry for the index before
            prefSuffDic[listOfStrings[i-1]] = [0,0]
            #set the first value of the dict entry to be the prefix
            prefSuffDic[listOfStrings[i-1]][0] = l[i][0:k]
            #set the second value of the dict entry as the suffix
            prefSuffDic[listOfStrings[i-1]][1] = l[i][-k:]
    #retruns 2D dictionaries that have both prefix and suffix stored for a particular key
    return prefSuffDic

def edge_list(prefSuffDic):
    edgeList = []
    #have to compare every entry in the dictionary with each other
    for key in prefSuffDic:
        for key2 in prefSuffDic:
            #check if the suffix of one key matches the prefix of another and make sure the keys are not the same
            #gene fragment can't overlap with itself
            if (prefSuffDic[key][1] == prefSuffDic[key2][0]) and (key != key2):
                edgeList.append(key + ' ' + key2)
    #return list of edges
    return edgeList

def codon_list():
    d = {'UUU' :'F',      'CUU': 'L',     'AUU': 'I',      'GUU': 'V',
'UUC': 'F',      'CUC': 'L' ,     'AUC': 'I',      'GUC': 'V',
'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
'UCG': 'S',      'CCG': 'P' ,     'ACG': 'T',      'GCG': 'A',
'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA' :'E',
'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
'UGC': 'C',      'CGC': 'R',      'AGC': 'S' ,     'GGC': 'G',
'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'} 
    return d

#default remove all whitepace, line breaks, tabs, and remnant / or \, 
#set variable to false
def sequence_cleaner(sequence, whiteSpace = True, lineBreak = True, tab = True, backslash = True, forwardslash = True):
    s = sequence
    if lineBreak is True:
        s = s.replace('\n', '')
    if whiteSpace is True:
        s = s.replace(' ', '')
    if tab is True:
        s = s.replace('\t', '')
    if forwardslash is True:
        s = s.replace('/', '')
    if backslash is True:
        s = s.replace('\\', '')
    return s

