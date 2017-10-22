## Scaling

Two kinds of scaling challenges come up a lot with NLP.

1. Too much data to fit in RAM (memory) at one time
2. Too much data or algorithm complexity to process in a reasonble amount of time.

### 1. RAM 

We need to process data in batches rather than all at once.

The "brue force" approach to calculating TFIDF is to count up all the frequencies in all the documents and keep that all in a master term-document matrix (table of vectors or a DataFrame).  
Then we could just do `df_tfidf = df_tf / df_tf.sum()` to normalize or TFIDF term-document matrix.  

But what if we don't have enough RAM to laod that entire table into memory?  
We'd just need to keep track of the term document frequencies in a separate vector and discard each document as we went through the set of documents.  

For some algorithms, like calculating TFIDF, this is pretty straight-forward, but for things like PCA on TFIDF matrices (LSA), this is really hard.  
And this is a really common challenge.  
Let's build a chatbot that can be trained on millions of statements (documents) rather than the 20k "documents" that we used in our example.  
We'll use a package called gensim that implements an incremental-PCA and incremental TFIDF. It only needs to process a small number of documents at a time.  


### 2. CPU

Our algortihm to search for the closest match among all the possible statements in our Ubuntu copurs is very inefficient.  
It's alglorithmic complexity is high (even though its code complexity is low).  
This is true of any "brute force" search with nested for loops.  
So we have 2 options.  

1. be smarter
2. do it in parallel

We can be smarter about how we calculate the cosine distances by *"vectorizing"* the calcualtion so it uses compiled C code that runs 100x faster than a python for loop.

Or we can actually split the work into smaller parts and distribute it to multiple processors.

Gensim does both.  
It has algorithms that smartly use vectorized calculations on batches of data.  
So those calculations can be distributed to multiple CPUs or cores.  
And you don't have to load all the data at once!  
So you **save** two birds with one stone (by scaring away the cat with a well-played toss of the stone).  

