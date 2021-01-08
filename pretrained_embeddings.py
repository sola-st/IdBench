#!/usr/bin/python3

# Author: Michael Pradel
#
# Simple demo of how to load and query the pre-trained embeddings.
#

import argparse
import numpy
from os.path import basename
from gensim.models import KeyedVectors
from gensim.models import Word2Vec


parser = argparse.ArgumentParser()
parser.add_argument(
    '--embedding', help="Pre-trained embedding file (.vec, .model, or .bin)", required=True)


def load_embedding(path):
    if path.endswith(".vec"):
        return KeyedVectors.load_word2vec_format(path, encoding='utf8')
    elif path.endswith(".model"):
        return Word2Vec.load(path)
    elif path.endswith(".bin"):
        return KeyedVectors.load_word2vec_format(path, binary=True, encoding='utf8')
    else:
        raise Exception(f"Unsupported kind of embedding: {path}")


def cos_sim(x, y):
    temp = x / numpy.linalg.norm(x, ord=2)
    temp2 = y / numpy.linalg.norm(y, ord=2)
    return round(numpy.dot(temp, temp2), 2)


def look_up_word(embedding, word, wrap=False):
    if wrap:
        word = f"\"ID:{word}\""
    return embedding[word]


if __name__ == "__main__":
    args = parser.parse_args()
    embedding = load_embedding(args.embedding)

    # our pre-trained embeddings expect tokens to be wrapped with "ID:..."
    wrap = basename(args.embedding) in [
        "ft_cbow.vec", "ft_sg.vec", "w2v_cbow.model", "w2v_sg.model"]

    for w1, w2 in [["idx", "ridx"], ["click", "mousedown"], ["pushStackLiteral", "oldSelection"]]:
        v1 = look_up_word(embedding, w1, wrap)
        v2 = look_up_word(embedding, w2, wrap)

        sim = cos_sim(v1, v2)

        print(
            f"According to {basename(args.embedding)}, identifiers {w1} and {w2} have similarity {sim}")
