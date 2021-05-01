#!/usr/bin/python3

# Author: Moiz Rauf
#
# Embedding training data pipeline script. This intermediate script, converts tokens into easily readable format for FastText training.
#

import argparse
import json
import os


parser = argparse.ArgumentParser()
parser.add_argument(
    '--source', help="Path to folder containing all extracted json files.", required=True)
parser.add_argument(
    '--destination', help="Path to folder where the transformed text file will be exported.", required=True)


def read_token_files(source):
    json_files = [x for x in os.listdir(source) if x.endswith("json")]
    print("read {0} json files".format(len(json_files)))
    total_sentences = 0
    file_sentence_map = {}
    for json_file in json_files:
        sentences = []
        json_file_path = os.path.join(source, json_file)

        with open(json_file_path, "r") as f:
            data = json.load(f, strict=False)
            for idx, sentence in enumerate(data):
                sentences.append(sentence)
                total_sentences += 1
        file_sentence_map[json_file] = sentences

    print('total files read {0}, sentences {1}'.format(
        len(file_sentence_map), total_sentences))
    return file_sentence_map


def write_to_ft_format(destination, file_sentence_map):
    out_file_path = os.path.join(destination, 'training_file.txt')

    with open(out_file_path, 'w', encoding='utf-8') as f:
        for f_name, sentences in file_sentence_map.items():
            for sentence in sentences:
                to_write = ' '.join('\"{}\"'.format(term)
                                    for term in sentence if term)
                f.write(to_write+'\n')


if __name__ == '__main__':
    args = parser.parse_args()

    # read all json files
    file_sentence_map = read_token_files(args.source)

    # writes all files into sentence structure
    write_to_ft_format(args.destination, file_sentence_map)
