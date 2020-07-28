import re
from collections import OrderedDict
import pandas as pd
from tqdm import tqdm
import sys
import fire
import csv


def process(file_name):

    pt_phrases = []
    gi_phrases = []

    pt_word_list = {}
    gi_word_list = {}

    with open(file_name) as f:

        data = csv.reader(f)

        for item in data:

            pt = item[0]
            gi = item[1]

            pt_phrases.append(pt)
            gi_phrases.append(gi)

    print(" * Processando PT:")
    for phrase in tqdm(pt_phrases):

        pt_word_list = word_counter(phrase, pt_word_list)

    print(" * Processando GI:")
    for phrase in tqdm(gi_phrases):

        gi_word_list = word_counter(phrase, gi_word_list)


    sort_and_csv_generate(pt_word_list,"PT")
    sort_and_csv_generate(gi_word_list,"GI")

def sort_and_csv_generate(word_list, name):

    word_list_num_ord = OrderedDict(
        sorted(word_list.items(), key=lambda t: t[1], reverse=True))

    word_list_alpha_ord = OrderedDict(
        sorted(word_list.items()))

    number_ord_file_df = pd.DataFrame.from_dict(word_list_num_ord, orient="index")
    number_ord_file_df.to_csv(f'output/{name}_word_list_num_ord.csv')

    alpha_ord_file_df = pd.DataFrame.from_dict(word_list_alpha_ord, orient="index")
    alpha_ord_file_df.to_csv(f'output/{name}_word_list_alpha_ord.csv')

def word_counter(phrase,word_list):

    for word in re.split(r'\W|\d', phrase):

        if word:
            if word in word_list:
                word_list.update({word: word_list[word]+1})
            else:
                word_list.update({word: 1})

    return word_list



if __name__ == '__main__':

    fire.Fire(process)
