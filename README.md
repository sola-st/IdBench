# IdBench
## About the dataset
This dataset is for evaluating to what extent word embeddings of identifiers represent semantic relatedness and similarity. The dataset contains identifier pairs annotated with similarity, relatedness and contextual similarity ratings tagged by developers. IdBench is an effort to provide a gold standard to guide the development of novel embeddings. 

The repository contains the following:
1. Tagged dataset of identifier pairs.
2. Trained identifier embedding models.

## Tagged dataset
For each of the three tasks, we provide a small, medium, and large benchmark, which differ by the thresholds used during data cleaning. The smaller benchmarks use stricter thresholds and hence provide higher agreements between the participants, whereas the larger benchmarks offer more pairs.

|Size|Relatedn.|Simil.|Context. simil.|Ground truth|
|:-----:|:----:|:-----:|:----:|:--:|
|Small  |  167|167|115 | [small_pair_wise.csv](small_pair_wise.csv)|
|Medium |  247|247|145 | [medium_pair_wise.csv](medium_pair_wise.csv)|
|Large  |  291|291|176 | [large_pair_wise.csv](large_pair_wise.csv)|


## Embedding Models
We evaluate the existing embedding methods on how they represent relatedness and similarity of identifiers, we evaluate five vector representations:
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

## Survey Conducted to Build the Dataset
IdBench is build based on a survey of 500 software developers. The following gives shows the instructions shown to participants, examples of questions asked, and details about the distribution of participants.

The following instructions were given to participants for the direct survey, which asks developers about the relatedness and similarity of pairs of identifiers:

![](https://raw.githubusercontent.com/sola-st/IdBench/master/images/instructions_direct_survey.png | width=300)

Here is an example of a question asked during the direct survey:

![](https://raw.githubusercontent.com/sola-st/IdBench/master/images/example_direct_survey.png | width=300)

The following instructions were given to participants for the indirect survey, which indireclty asks developers about contextual similarity of pairs of identifiers:

![](https://raw.githubusercontent.com/sola-st/IdBench/master/images/instructions_indirect_survey.png | width=300)

Here is an example of a question asked during the indirect survey:

![](https://raw.githubusercontent.com/sola-st/IdBench/master/images/example_indirect_survey.png | width=300)

Finally, some statistics about the geographical distribution and previous experience of the participants:

![](https://raw.githubusercontent.com/sola-st/IdBench/master/images/participants.png | width=300)