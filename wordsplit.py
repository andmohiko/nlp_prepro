import numpy as np
import MeCab


wakati = MeCab.Tagger('-Owakati')

def get_wakati(text):
    return wakati.parse(text).strip()


def make_corpus(series):
    corpus_spaced = [0] * len(series)
    for i, words in enumerate(series):
        try:
            corpus_spaced[i] = get_wakati(words)
        except TypeError:
            print(i, words)
            corpus_spaced[i] = "nopositon"
    return corpus_spaced


def split_words(corpus_spaced):
    corpus_splitted = [0] * len(corpus_spaced)
    for i, c in enumerate(corpus_spaced):
        corpus_splitted[i] = c.split()
    return corpus_splitted


def join_words(corpus_splitted):
    corpus_joined = [0] * len(corpus_splitted)
    for i, c in enumerate(corpus_splitted):
        corpus_joined[i] = " ".join(c)
    return corpus_joined


def remove_stopwords(corpus_splitted, stopwords):
    na_idx = []
    for i, c in enumerate(corpus_splitted):
        corpus_splitted[i] = [word for word in c if word not in stopwords]
        if corpus_splitted[i] == []:
            na_idx.append(i)
    return corpus_splitted, na_idx


def prepro(data, stopwords):
    corpus_splitted = split_words(make_corpus(data["sentence"]))
    corpus_rmsw, na_idx = remove_stopwords(corpus_splitted, stopwords)
    data["wordlist"] = corpus_rmsw
    data = data.drop(na_idx).reset_index(drop=True)
    return data