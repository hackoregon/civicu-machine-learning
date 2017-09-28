# Multivariate Regression, Ethics, and Git

In every class we're going to learn about a new Machine Learning model and train it on some data.
By the end of the class you should have developed some habits for working with data and producing Machine Learning models in seconds.
We'll also spend some time in each class working on the logistics of Data Science and Machine Learning:

* Data ETL
  * **E**xtract data from a data source
      * csv: `df = pd.read_csv('file.csv', header=0)`
      * html: `df = pd.read_html('wikipedia.org/page', header=0)[-1]`
      * json: `df = pd.normalize_json('totalgood.org/bicycle/')`
      * database: `df = pd.io.sql.psql.frame_query('SELECT * FROM tbl', sqla.create_engine('postgresql://me@localhost:5432/db'))`
  * **Transform** data
      * convert units
      * normalize or standardize (to help the ML fit)
      * combine or split columns
      * join/merge tables
      * clean the data (remove or correct errors)
      * deal with missing values
        * delete rows: `df.dropna(thresh=N)` (can you use a mask?)
        * delete columns: `df.dropna(thresh=N, axis=1)`
        * fill with a constant value: `df.fillna()`
            * 0, -1, 1 or any other arbitrary value not in your dataset
            * +INF
            * -INF
            * mean
            * median
            * min or min "-1"
            * max or max "+1"
            * arbitrary valuesome new value to create ML **features**
        * imputation: `model.fit_transform()`
  * **L**oad data into your model or pipeline
    * `df.to_csv()... df = `pd.read_csv()`
* data cleaning

## Multivariate Linear Regression

A line passing through a scatter plot is a great way to display the results of a linear regression.
How should we display the results of a multivariate linear regression with 2 "features" (height and gender) and one target variable (weight)?

## Teaching Machines Ethics

* What ethical questions might arise in our multivariate model to predict weight from height and gender?
* Should machines be held to the same ethical standards as humans?
* Who is the responsible "parent" when a machine behaves illegally?
* Is maintaining data provenance (pedigree or ancestry) a professional best practice or a moral responsibility? 
* Is "default to open" a business decision? A business "value"? An ethical decision?

* What additional questions should you ask yourself when you are training a machine to make predictions?

If you want to think about this more deeply, check out the draft of a presentation on (AI Morality](../ai-morality.md).


