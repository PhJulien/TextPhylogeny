#!/usr/bin/pyhton

import os, glob
import  scipy, numpy
from gensim import corpora, models, similarities

stoplist = set('for a of the and to in to be which some is at that we i who whom show via may my our might as well'.split())

def text2vec(texts, stoplist):
    texts = [[word for word in A.lower().split() if word not in stoplist] for A in texts]
    #all_tokens = sum(texts, [])
    #tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    #texts = [[word for word in text if word not in tokens_once] for text in texts]
    return texts





files_dir = "~/Dropbox/Code/text_phylo/Darwin/*"
files_dir = "/Users/pjulien/Dropbox/Code/text_phylo/Darwin/*"

glob.glob(files_dir)



## Build a corpus and dictionary from all the files

### Get all the texts into a list
txts = []
for n in glob.glob(files_dir):
    f = open(n)
    data=f.read().replace('\n', '').replace('\r', '')
    txts.append(data)
    

### Pre process texts
texts = text2vec(txts, stoplist)


### Create dictionary and corpus
dictionary = corpora.Dictionary(texts)
#print(dictionary.token2id)
 
corpus = [dictionary.doc2bow(text) for text in texts]



## Initializing model for our "database"

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=256)
index = similarities.MatrixSimilarity(lsi[corpus])

# Parsing input (reference abstract in this case)

matrix = []
for i in range(len(txts)):
    q = txts[i]
    vec_bow = dictionary.doc2bow(q.lower().split())
    vec_lsi = lsi[vec_bow] # convert the query to LSI space # Should understand what this means =)
    #print(vec_lsi)
    ## Get cosine similarity score from our input
    sims = index[vec_lsi]
    ## Storing it
    matrix.append(sims)
    #print(list(enumerate(sims)))



import matplotlib.pyplot as plt
plt.bar(range(len(txts)), sims)
plt.show()
## Index lsi for later search




# Getting titles
titles = [t2.replace(".txt", "") for t2 in [os.path.basename(t) for t in glob.glob(files_dir)]]
titles2 = titles[:]
titles2.insert(0 , " ")

content = ""
sep = ""
for t in titles2:
    content +=  sep + t
    sep = "\t"

content += "\n"



for i in range(len(titles)):
    content += titles[i]
    sep="\t"
    for n in matrix[i]:
        content += sep + str(n)
    content += "\n"
    
file = open("/Users/pjulien/Dropbox/Code/text_phylo/Results/Darwin.Cosine.Sim.lsi.Matrix.txt", "w")

file.write(content)


file.close()
        





########### Trying a lda model

lda = models.LdaModel(corpus, num_topics=256)
index_lda = similarities.MatrixSimilarity(lda[corpus])

# lda.print_topics()

matrix_lda = []
for i in range(len(txts)):
    q = txts[i]
    vec_bow = dictionary.doc2bow(q.lower().split())
    vec_lda = lda[vec_bow] # convert the query to LSI space # Should understand what this means =)
    #print(vec_lsi)
    ## Get cosine similarity score from our input
    sims = index_lda[vec_lda]
    ## Storing it
    matrix_lda.append(sims)
    #print(list(enumerate(sims)))



