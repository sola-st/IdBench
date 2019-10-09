# IdBench
### About the dataset
The dataset is an effort for evaluating to what extent word embeddings of identifiers represent semantic relatedness and similarity. The dataset contains identifier pairs annotated with similarity, relatedness and contextual similarity ratings tagged by developers. IdBench is an effort to provide a gold standard to guide the development of novel embeddings. 

The repository contains following files.
1. Tagged dataset.
2. Trained identifier embedding models.
3. Cosine similarity scores for each model.

### Tagged dataset
For each of the three tasks, we provide a small, medium, and large benchmark, which differ by the thresholds used during data cleaning. The smaller benchmarks use stricter thresholds and hence provide higher agreements between the participants, whereas the larger benchmarks offer more pairs.
|size|Relatedn.|Simil.|Context. simil.|
|:-----:|:----:|:-----:|:----:|
|Small  |  167|167|115 |
|Medium |  247|247|145 |
|Large  |  291|291|176 |

### Embedding Models
We evaluate the existing embedding methods on how they represent relatedness and similarity of identifiers, we evaluate five vector representations
1. continuous bag of words and the skip-gram variants of Word2vec (“_w2v-cbow_” and “_w2v-sg_”)
2. sub-word extension of word2vec FastText (“_FT-cbow_” and “_FT-sg_”)
3. embeddings trained using tree-based representation of code (“_path-based_”)

### Cosine Similarity File
In addition to neural embeddings of identifiers, we also evaluate two string distance functions: Levenshtein’s edit distance and Needleman-Wunsch distance. For further investigation, we report all results for identifier pairs in **pair_wise_similarity_score.csv**
