'''
https://openbook4.me/projects/193/sections/1154
'''

import os
from gensim import corpora, models
import pandas as pd


# global param
MODEL = None
DICTONARY = None


def get_absolute_path(filepath):
    return os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath))

def read_csv(filepath):
    """
    read_csv
    """
    dataframe = pd.read_csv(filepath, encoding='Shift_JIS', dtype='str')
    return dataframe.columns.tolist(), dataframe.values

def get_data(filepath):
    columns, rows = read_csv(filepath)
    output_dict = {}
    output_list = []
    for row in rows:
        attack_id = row[columns.index("attackID")]
        hotzone = row[columns.index("hotzone")]
        action_word = row[columns.index("actionWord")]
        compactness_attack_word = row[columns.index("CompactnessAttackWord")]
        compactness_defense_word = row[columns.index("CompactnessDefenseWord")]
        vulnerability_attack_word = row[columns.index("VulnerabilityAttackWord")]
        vulnerability_defense_word = row[columns.index("VulnerabilityDefenseWord")]
        offside_line_attack_word = row[columns.index("OffsideLineAttackWord")]
        offside_line_defense_word = row[columns.index("OffsideLineDefenseWord")]
        front_line_word = row[columns.index("FrontLineWord")]

        if attack_id not in output_dict:
            output_dict[attack_id] = []

        output_dict[attack_id].append(hotzone)
        output_dict[attack_id].append(action_word)
        #output_dict[attack_id].append(compactness_attack_word)
        output_dict[attack_id].append(compactness_defense_word)
        #output_dict[attack_id].append(vulnerability_attack_word)
        output_dict[attack_id].append(vulnerability_defense_word)
        output_dict[attack_id].append(offside_line_attack_word)
        output_dict[attack_id].append(offside_line_defense_word)
        #output_dict[attack_id].append(front_line_word)

    for attack_id, row in output_dict.items():
        output_list.append(' '.join(row))

    return output_list

def main(documents):
    """
    main
    """
    # remove common words and tokenize
    stoplist = set('for a of the and to in'.split())
    texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

    # remove words that appear only once
    all_tokens = sum(texts, [])
    tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    texts = [[word for word in text if word not in tokens_once] for text in texts]
    # print('texts')
    # print(texts)
    # print()
        
    
    global DICTIONARY
    DICTIONARY = corpora.Dictionary(texts)
    DICTIONARY.save(get_absolute_path('tmp/deerwester.dict'))
    DICTIONARY.save_as_text(get_absolute_path('tmp/deerwester_text.dict'))
    # print('DICTIONARY')
    # print(DICTIONARY)
    # print(DICTIONARY.token2id)
    # print()

    new_doc = "Human computer interaction"
    new_vec = DICTIONARY.doc2bow(new_doc.lower().split())
    # print('new_vec')
    # print(new_vec)
    # print()

    corpus = [DICTIONARY.doc2bow(text) for text in texts]
    # store to disk, for later use
    corpora.MmCorpus.serialize(get_absolute_path('tmp/deerwester.mm'), corpus)
    # print('corpus')
    # print(corpus)
    # print()

    global MODEL
    MODEL = models.ldamodel.LdaModel(corpus=corpus, id2word=DICTIONARY, num_topics=3)
    # print(MODEL[new_vec])

if __name__ == '__main__':
    DOC1 = get_data('LDAdocuments.csv')
    DOC2 = ["Human machine interface for lab abc computer applications",
            "A survey of user opinion of computer system response time",
            "The EPS user interface management system",
            "System and human system engineering testing of EPS",
            "Relation of user perceived response time to error measurement",
            "The generation of random binary unordered trees",
            "The intersection graph of paths in trees",
            "Graph minors IV Widths of trees and well quasi ordering",
            "Graph minors A survey"]
    main(DOC1)
