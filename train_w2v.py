import gensim
from time import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--source', help="Path to folder containing all extracted json files.", required=True)
parser.add_argument(
    '--destination', help="File to store the trained model in.", required=True)
parser.add_argument(
    '--cbow', help="Use cbow as training algoritm. Default value False", action='store_true', required=False)


def train_w2v(source_file, destination, cbow):
    try:
        is_sg = 1  # True for skipgram
        if cbow:
            is_sg = 0
        w2v_model = gensim.models.Word2Vec(
            min_count=3, window=5, size=100, sample=6e-5, alpha=0.03, min_alpha=0.0007, negative=20, workers=6, sg=is_sg)

        # -ws 5 -epoch 15 -dim 100 -minCount 3
        sentences = gensim.models.word2vec.LineSentence(source_file)

        #w2v_model = gensim.models.Word2Vec(sentences, min_count=3, size=100, window=5, sg=1,hs=1)

        t = time()

        w2v_model.build_vocab(sentences, progress_per=1000)
        print('Time to build vocab: {} mins'.format(
            round((time() - t) / 60, 2)))

        t = time()

        w2v_model.train(
            sentences, total_examples=w2v_model.corpus_count, epochs=15, report_delay=1)

        print('Time to train the model: {} mins'.format(
            round((time() - t) / 60, 2)))

        w2v_model.save(destination)
    except Exception as e:
        raise


if __name__ == "__main__":
    args = parser.parse_args()

    train_w2v(args.source, args.destination, args.cbow)
