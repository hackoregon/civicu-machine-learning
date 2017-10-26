# Neural Nets

1. review linear regression homework
2. Motivation
3. introduce neural nets (Rosenblatt's Perceptron)
4. build a single-layer neural net to classify flowers
5. use keras to classify MNIST digits

### Advantages

+ "automatic" nonlinear feature engineering
+ inherently parallel (scalable)

### Disadvantages

- less data efficient
- less cpu efficient
- less RAM efficient
- harder to tune
- less explainable
- provide less data "insight"

That may seem like more disadvantages than advantages, but if you have the procesing power (preferably parallel, like a GPU) and the data, then Neural Nets can do some magical things that weren't possible before.

And sometimes, when a neural net solves a problem with "magic" that gives us the data scientists ideas about how to formulate a data science problem and do feature engineering the conventional way, to do things the "old" way.  
For example, word2vec accomplished word embedding that enabled us to do math with words.  
But a year later scientists reverse engineered the word2vec neural net to discover a way to do it with PCA (LSA).  

### Applications

Any high dimensional data without obvious features or "representations"

+ Natural Language (NLP)
+ Images, Video
+ Time Series (Finance, Speech, Music)
+ GIS (Weather)
+ Planning (Games, Self-driving, UAVs)

Game play "policies" (move plans) can be very high dimensional.

### NLP

+ Finance News
+ Headline Writing
+ Autocomplete
+ Middle Button meme
+ Fake news
+ Finance forecasting (Banjo)
+ Horror Script writing
+ Chatbots
+ Lawyer Bots

### Image Processing

+ BVI assistance
+ Radioology
+ Self-driving cars
+ OCR (Mail sorting)

### Time Series

+ Stock Forecasting
+ High- Frequencty Trading
+ Speech recognition (Restricted Boltzmann Machines)
+ Speech generation?

### NLP

+ Segmentation (Sentence, Phrase, Paragraph)
+ Word2Vec
+ Sentiment Analysis
+ POS Tagging
+ Predictive Text
+ Search? Siri? Google?
+ Google SmartReply

### Planning

+ Go (AlphaGo Lee, AlphaGo Master, AlphaGo Zero)
+ Self-Driving Cars
+ UAV piloting (helicopter upside down!)
+ War planning
+ Cruise Missiles
+ Heat-seeking missiles

References:

* [A great perceptron tutorial](http://www.bogotobogo.com/python/scikit-learn/Perceptron_Model_with_Iris_DataSet.php)