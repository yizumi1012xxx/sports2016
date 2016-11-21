'''
https://openbook4.me/projects/193/sections/1154
https://radimrehurek.com/gensim/apiref.html
'''

import os
import csv
import pandas as pd
import numpy as np
from gensim import corpora, models

def get_absolute_path(filepath):
    return os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath))

def read_csv(filepath):
    """
    read_csv
    """
    dataframe = pd.read_csv(filepath, encoding='Shift_JIS', dtype='str')
    return dataframe.columns.tolist(), dataframe.values

def write_csv(header, data, filepath):
    """
    write_csv
    """
    with open(filepath, 'w') as file_object:
        writer = csv.writer(file_object, lineterminator='\n')
        writer.writerow(header)
        writer.writerows(data)

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
        compactness__offside = row[columns.index("Compactness__Offside")]
        neighbor_player = row[columns.index("NeighborPlayerWord")]

        if attack_id not in output_dict:
            output_dict[attack_id] = []

        output_dict[attack_id].append(hotzone)
        output_dict[attack_id].append(action_word)
        #output_dict[attack_id].append(compactness_attack_word)
        #output_dict[attack_id].append(compactness_defense_word)
        #output_dict[attack_id].append(vulnerability_attack_word)
        output_dict[attack_id].append(vulnerability_defense_word)
        #output_dict[attack_id].append(offside_line_attack_word)
        #output_dict[attack_id].append(offside_line_defense_word)
        #output_dict[attack_id].append(front_line_word)
        output_dict[attack_id].append(compactness__offside)
        output_dict[attack_id].append(neighbor_player)

    for attack_id, row in output_dict.items():
        output_list.append(' '.join(row))

    return output_list

def get_topic_distribution_of_doc(model, dictionary, documents):
    """
    ドキュメントごとのトピック分布を出力
    """

    columns = ["topic0", "topic1", "topic2", "topic3", "topic4"]
    output = []
    for document in documents:
        temp = np.zeros(5) # topic number
        bow = dictionary.doc2bow(document.lower().split())
        topics = model.get_document_topics(bow, 0)
        for topic in topics:
            topic_id = topic[0]
            topic_probability = topic[1]
            print(topic_id, topic_probability)
            temp[topic_id] = topic_probability
        output.append(temp)
    output = np.array(output)

    filepath = get_absolute_path('tmp/get_topic_distribution_of_doc.csv')
    write_csv(columns, output, filepath)


def get_word_distribution_of_topic(model, dictionary):
    """
    トピックごとの単語分布を出力
    """
    rows = []
    columns = ["word"]
    for word in dictionary.items():
        word_id = word[0]
        word_name = word[1]
        columns.append("%s"%word_name)

    for topic in model.show_topics():
        topic_id = topic[0]
        row = [0] * len(columns)
        row[0] = "topic[%s]"%topic_id
        for word in model.show_topic(topic_id, len(columns)):
            word_name = word[0]
            word_probability = word[1]
            row[columns.index(word_name)] = word_probability
        rows.append(row)

    filepath = get_absolute_path('tmp/get_word_distribution_of_topic.csv')
    write_csv(columns, rows, filepath)

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

    dictionary = corpora.Dictionary(texts)
    dictionary.save(get_absolute_path('tmp/deerwester.dict'))
    dictionary.save_as_text(get_absolute_path('tmp/deerwester_text.dict'))

    # new_doc = "Human computer interaction"
    # new_vec = dictionary.doc2bow(new_doc.lower().split())

    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize(get_absolute_path('tmp/deerwester.mm'), corpus)

    # https://radimrehurek.com/gensim/models/ldamodel.html
    model = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5)
    return dictionary, model

if __name__ == '__main__':
    DOC1 = get_data(get_absolute_path('tmp/LDAdocuments.csv'))
    DOC2 = ["Human machine interface for lab abc computer applications",
            "A survey of user opinion of computer system response time",
            "The EPS user interface management system",
            "System and human system engineering testing of EPS",
            "Relation of user perceived response time to error measurement",
            "The generation of random binary unordered trees",
            "The intersection graph of paths in trees",
            "Graph minors IV Widths of trees and well quasi ordering",
            "Graph minors A survey"]
    DICTIONARY, MODEL = main(DOC1)
    get_word_distribution_of_topic(MODEL, DICTIONARY)
    get_topic_distribution_of_doc(MODEL, DICTIONARY, DOC1)