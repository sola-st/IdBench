# IdBench
## About the dataset
The dataset is an effort for evaluating to what extent word embeddings of identifiers represent semantic relatedness and similarity. The dataset contains identifier pairs annotated with similarity, relatedness and contextual similarity ratings tagged by developers. IdBench is an effort to provide a gold standard to guide the development of novel embeddings. 

The repository contains following files.
1. Tagged dataset.
2. Trained identifier embedding models.

## Tagged dataset
For each of the three tasks, we provide a small, medium, and large benchmark, which differ by the thresholds used during data cleaning. The smaller benchmarks use stricter thresholds and hence provide higher agreements between the participants, whereas the larger benchmarks offer more pairs.

|Size|Relatedn.|Simil.|Context. simil.|Ground truth|
|:-----:|:----:|:-----:|:----:|:--:|
|Small  |  167|167|115 | [small_pair_wise.csv](small_pair_wise.csv)|
|Medium |  247|247|145 | [medium_pair_wise.csv](medium_pair_wise.csv)|
|Large  |  291|291|176 | [large_pair_wise.csv](large_pair_wise.csv)|


## Embedding Models
We evaluate the existing embedding methods on how they represent relatedness and similarity of identifiers, we evaluate five vector representations
1. continuous bag of words and the skip-gram variants of Word2vec (“_w2v-cbow_” and “_w2v-sg_”)
2. sub-word extension of word2vec FastText (“_FT-cbow_” and “_FT-sg_”)
3. embeddings trained using tree-based representation of code (“_path-based_”)


### Hyperparameters
To report the best possible results that each model can achieve, we tune each of them against IdBench. We evaluated the following hyperparameters:
 * Size of context window: 2-6
 * Embedding dimensionality: 50, 100, 150, 200, 250, 300
 * Number of iterations (epochs): 5-50
 * Learning rate: 0.1, 0.01, 0.001, 0.0001
 * Minimum word occurrence: 1-5

The following are the best found configurations:

|Model|Window size|Dimensionality|Iterations|Learning rate|Minimum word occurrence|
|:---:|:---:|:---:|:---:|:---:|:---:|
|FT-cbow|5|100|15|0.1|3|
|FT-sg   |  5  |   300  |   15  |   0.1    | 3|
|w2v-cbow |    5 |    100  |   15  |   0.1  |   3|
|w2v-sg    | 5    | 50    | 15 |    0.1    | 3| 
