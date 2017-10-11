# Principle Component Analysis (PCA)

Principle Component Analysis was [described in the 30's by Harold Hotelling at Columbia University](https://babel.hathitrust.org/cgi/pt?id=wu.89097139406;view=1up;seq=5).
He was looking for an underlying pattern in the correlation between student's scores on various math and reading problems.
He had a table of these test scores with many different scores for each student and noticed that they were highly correlated for some things and not other. For instance students that were good at addition were often also good at multiplication, but students that did poorly on a reading comprehension test often did well on algebra problems. 
Hotelling was looking for a simple underlying representation (an abstraction or vector model) of each student that could approximately represent (predict) their scores on tests.
He recognized that this would be useful for anyon looking or an "underlying" (latent) representation of the rows of data (vectors) in tables of numerical data.

In natural language processing, PCA is called ["Latent Semantic Analysis"](https://en.wikipedia.org/wiki/Latent_semantic_analysis) or "Latent Semantic Indexing." However, the "indexing" part is a bit of a misnomer, as the continuous high-dimensional vectors produced are too low density to be efficiently indexed for semantic search, so fruther dimension reduction or discretization is required to produce practical indexing for semantic search and information retrieval applications.

## Applications

Today, PCA is often the first feature transformation performed in any machine learning pipeline with high dimensional data, like image processing, music and speech recognition.

- biometric face recognition: log onto accounts
- biometric iris recognition: unlock doors at high security facilities
- biometric hand recognition: admission to parties at 1996 Olympics in Atlanta
- biometric fingerprint recognition: unlock your smartphone
- image object recognition: self-driving cars recognizing stop signs
- time series prediction: weather forecasting
- speech transcription: Google Home and Amazon Echo interaction
- voice recognition: unlock your laptop 
- image enhancement: spy cameras that see through fog and cloud)
- laser scanner point cloud recognition: satellite ID and tracking
- radar: aircraft classificaiton and tracking

You may not realize it but your purchase and click behavior can also be processed using PCA in recommendation engines to suggest products or services for you:

- Netflix: movies
- Spotify: songs
- Amazon: books
- CNET: electronics
- Dark Horse: graphic novels
- eBay: pre-owned stuff
- Zillow: houses
- Google: ads
- Google: search terms
- Facebook friends
- Pinterest: household goods
- Etsy art
- LinkedIn contacts
- Yelp restaurants

## References

- [Relationship Between PCA and SVD](https://intoli.com/blog/pca-and-svd/)
- [sklearn.decomposition.PCA](http://scikit-learn.org/stable/modules/decomposition.html#pca)
- [sklearn PCA User Guide](http://scikit-learn.org/stable/modules/decomposition.html#pca)
- [sklearn.decomposition.PCA](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
- [sklearn.decomposition.IncrementalPCA](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html)
- [sklearn.decomposition.KernelPCA](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html)
- [sklearn.decomposition.SparsePCA](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html)
- [sklearn.decomposition.TruncatedSVD](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html)
