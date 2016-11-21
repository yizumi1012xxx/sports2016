'''
https://openbook4.me/projects/193/sections/1154
'''

from gensim import corpora, models, similarities
documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

# remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once] for text in texts] 
print('texts')
print(texts)
print()

dictionary = corpora.Dictionary(texts)
dictionary.save('deerwester.dict')
dictionary.save_as_text('deerwester_text.dict')
print('dictionary')
print(dictionary)
print(dictionary.token2id)
print()

new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print('new_vec')
print(new_vec)
print()

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus) # store to disk, for later use
print('corpus')
print(corpus)
print()

model = models.ldamodel.LdaModel(corpus = corpus, id2word=dictionary, num_topics=3)

print(model[new_vec])
             
